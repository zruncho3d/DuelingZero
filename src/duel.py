#!/usr/bin/env python3
# Script to run a Dueling Zero printer with two toolheads.
#
# To see arguments, invoke this script with:
#   ./duel.py -h
#
# Sample invocations:
#   python duel.py dz.local:7125 dz.local:7126 --duel
#   ./duel.py dz.local:7125 dz.local:7126 --input sample.gcode --home --home_after
#

import argparse
import os
import sys
import time

from gcodeparser import GcodeParser, GcodeLine
import requests

from toolhead import LEFT_HOME_POS, RIGHT_HOME_POS, check_for_overlap, check_for_overlap_sweep
from toolhead import Y_HEIGHT, TO_X_BACKAWAY, T1_X_BACKAWAY, Y_HIGH, Y_LOW, X_HIGH, X_LOW
from toolhead import X_BACKAWAY_LEN, BACKAWAY_SPEED, PARK_SPEED, SHUFFLE_SPEED, TOOLHEAD_Y_HEIGHT
from point import Point
from battle import Battle


# Modes:
# - simple: if a conflicting move were to occur, exit the program.
# - smart: intelligently handle conflicting moves, by inserting backups, splits, and shuffles.
MODES = ['simple', 'smart']
DEF_MODE = 'simple'


# Set this high enough to handle any command(s) you'd run.
# Note, however, that Moonraker by default throws a 200 after exactly
# one minute, even with this value set to exceed one minute.
READ_TIMEOUT = 180


def home(printer):
    run_gcode(printer, "G28 X Y")


def center(printer):
    run_gcode(printer, "G0 X60 Y60 F6000")


def run_gcode(printer, gcode, verbose=False):
    """Run a gcode command to completion and return the result.
    https://github.com/Arksine/moonraker/blob/master/docs/web_api.md#run-a-gcode
    """
    r = requests.post("http://" + printer + "/printer/gcode/script?script=" + gcode, timeout=(1, READ_TIMEOUT))
    if verbose:
        print(r.status_code)
    # Disable to workaround 60-second presumably-Moonraker timeout
    assert(r.status_code == 200)
    return r


T0 = GcodeLine(('T', 0), {}, "")
T1 = GcodeLine(('T', 1), {}, "")


class DuelRunner:

    def __init__(self, args):
        self.left = None
        self.right = None
        self.mode = 'smart'
        self.m400_always = False
        self.args = None
        self.dry_run = False
        if args is not None:
            self.left = args.left  # URL of left-side Moonraker instance
            self.right = args.right  # URL of left-side Moonraker instance
            self.mode = args.mode  # mode in MODES
            self.m400_always = args.m400_always
            self.args = args
            self.dry_run = args.dry_run
        # Use empty Args for regression testing, until this can be properly refactored.
        # Motion should be separate from execution.
        else:
            self.left = 'left'
            self.right = 'right'
            self.dry_run = True
        # Initialize metrics
        self.simple_shuffles = 0
        self.backup_shuffles = 0
        self.segmented_shuffles = 0

    def test_latency(self):
        times = []
        for i in range(3):
            start_time = time.time()
            for gcode in ["M400"]:
                run_gcode(self.left, gcode)
            elapsed = time.time() - start_time
            times.append(elapsed)
        print("Times: %s" % times)

    def t0_park(self):
        for gcode in ["G0 X%s F%s" % (X_LOW, PARK_SPEED), "G0 Y%s F%s" % (Y_HIGH, PARK_SPEED), "M400"]:
            self.run_gcode(self.left, gcode)

    def t1_park(self):
        for gcode in ["G0 X%s F%s" % (X_HIGH, PARK_SPEED), "G0 Y%s F%s" % (Y_LOW, PARK_SPEED), "M400"]:
            self.run_gcode(self.right, gcode)

    def t0_backaway(self):
        for gcode in ["G0 X%s F%s" % (TO_X_BACKAWAY, BACKAWAY_SPEED), "M400"]:
            self.run_gcode(self.left, gcode)

    def t1_backaway(self):
        for gcode in ["G0 X%s F%s" % (T1_X_BACKAWAY, BACKAWAY_SPEED), "M400"]:
            self.run_gcode(self.right, gcode)

    def t0_shuffle(self, pos):
        assert pos.y == Y_HIGH or pos.y == Y_LOW
        new_y = None
        if pos.y == Y_LOW:
            new_y = Y_HIGH
        elif pos.y == Y_HIGH:
            new_y = Y_LOW
        for gcode in ["G0 Y%s F%s" % (new_y, SHUFFLE_SPEED), "M400"]:
            self.run_gcode(self.left, gcode)
        return Point(pos.x, new_y)

    def t1_shuffle(self, pos):
        assert pos.y == Y_HIGH or pos.y == Y_LOW
        new_y = None
        if pos.y == Y_LOW:
            new_y = Y_HIGH
        elif pos.y == Y_HIGH:
            new_y = Y_LOW
        for gcode in ["G0 Y%s F%s" % (new_y, SHUFFLE_SPEED), "M400"]:
            self.run_gcode(self.right, gcode)
        return Point(pos.x, new_y)

    def t0_go_to(self, pos):
        for gcode in ["G0 X%s Y%s" % (pos.x, pos.y), "M400"]:
            self.run_gcode(self.left, gcode)

    def t1_go_to(self, pos):
        for gcode in ["G0 X%s Y%s" % (pos.x, pos.y), "M400"]:
            self.run_gcode(self.right, gcode)

    @staticmethod
    def is_toolchange_gcode(line):
        return line == T0 or line == T1

    @staticmethod
    def is_move_gcode(line):
        return line.command == ('G', 0) or line.command == ('G', 1)

    def run_gcode(self, instance, gcode_line):
        if instance == self.left:
            print("  left>  ", gcode_line)
        elif instance == self.right:
            print("  right> ", gcode_line)
        if not self.dry_run:
            run_gcode(instance, gcode_line)

    @staticmethod
    def get_corresponding_x(toolhead_pos, next_toolhead_pos, target_y):
        """Get the corresponding x for a target y; useful for splitting moves for segmented avoidance."""

        # Handle vertical case.
        if toolhead_pos.x == next_toolhead_pos.x:
            return toolhead_pos.x

        # Compute the new path portion that gets us clear of the future parked inactive extruder in the Y.
        # y = mx + b; slope (m); intercept (b);
        m = (next_toolhead_pos.y - toolhead_pos.y) / (next_toolhead_pos.x - toolhead_pos.x)
        b = (toolhead_pos.y - m) / toolhead_pos.x
        # Find point on line where Y-val = min to clear.
        # x = (<Y val> - b) / m
        x = (target_y - b) / m
        return x

    def do_right_segmented_sequence(self, toolhead_pos, target_y, next_toolhead_pos, inactive_toolhead_pos):
        # If a simple backup-X move, followed by resume-X, were to cause a collision,
        # then execute enough of the move to clear the shuffled inactive extruder, back it away,
        # do the shuffle, then resume with the second part of the move.

        # TODO: handle extrusion in the move split and retain the g-code used for the move (G0 vs G1, etc.)
        x = self.get_corresponding_x(toolhead_pos, next_toolhead_pos, target_y)
        mid_pos = Point(x, target_y)
        print("  ! Segmented sequence")
        print("  ! Doing first part of move sequence")
        self.t0_go_to(mid_pos)
        print("  ! Backing up t0")
        self.t0_backaway()
        print("  ! Shuffling inactive 1")
        right_toolhead_pos = self.t1_shuffle(inactive_toolhead_pos)
        print(" ! Restoring t0 to mid_pos after backup: %s" % mid_pos)
        self.t0_go_to(mid_pos)
        print(" ! Doing second part of move sequence : %s" % mid_pos)
        self.t0_go_to(next_toolhead_pos)
        return right_toolhead_pos

    def do_right_backup_sequence(self, toolhead_pos, inactive_toolhead_pos, active_instance, line):
        print("  ! Backup sequence")
        print("  ! Backup sequence: t0 Backing up")
        self.t0_backaway()
        print("  ! Shuffling inactive t1")
        right_toolhead_pos = self.t1_shuffle(inactive_toolhead_pos)
        # Restore original x for active instance
        print(" ! Resuming after backup: t0 restoring to %s" % toolhead_pos)
        self.t0_go_to(toolhead_pos)
        print(" ! Running original move.")
        self.run_gcode(self.get_active_printer_name(active_instance), line.gcode_str)
        return right_toolhead_pos

    def do_left_segmented_sequence(self, toolhead_pos, target_y, next_toolhead_pos, inactive_toolhead_pos):
        # If a simple backup-X move, followed by resume-X, were to cause a collision,
        # then execute enough of the move to clear the shuffled inactive extruder, back it away,
        # do the shuffle, then resume with the second part of the move.

        # TODO: handle extrusion in the move split and retain the g-code used for the move (G0 vs G1, etc.)
        x = self.get_corresponding_x(toolhead_pos, next_toolhead_pos, target_y)
        mid_pos = Point(x, target_y)
        print("  ! Segmented sequence")
        print("  ! Doing first part of move sequence")
        self.t1_go_to(mid_pos)
        print("  ! Backing up t0")
        self.t1_backaway()
        print("  ! Shuffling inactive 1")
        left_toolhead_pos = self.t0_shuffle(inactive_toolhead_pos)
        print("  ! Restoring t0 to mid_pos after backup: %s" % mid_pos)
        self.t1_go_to(mid_pos)
        print("  ! Doing second part of move sequence : %s" % mid_pos)
        self.t1_go_to(next_toolhead_pos)
        return left_toolhead_pos

    def do_left_backup_sequence(self, toolhead_pos, inactive_toolhead_pos, active_instance, line):
        print("  ! Backup sequence")
        print("  ! Backup shuffle: t0 Backing up")
        self.t1_backaway()
        print("  ! Shuffling inactive t1")
        left_toolhead_pos = self.t0_shuffle(inactive_toolhead_pos)
        # Restore original x for active instance
        print("  ! Resuming after backup: t0 restoring to %s" % toolhead_pos)
        self.t1_go_to(toolhead_pos)
        print("  ! Running original move.")
        self.run_gcode(self.get_active_printer_name(active_instance), line.gcode_str)
        return left_toolhead_pos

    def get_active_printer_name(self, active_instance):
        if active_instance == 'left':
            return self.left
        else:
            return self.right

    @staticmethod
    def get_nonactive_printer_name(active_instance):
        if active_instance == 'left':
            return 'right'
        else:
            return 'left'

    def play_gcodes_file(self, gcode_file):
        file_content = None
        with open(gcode_file, 'r') as f:
            file_content = f.read()
        self.play_gcodes(file_content)

    def play_gcodes(self, input_file_content):
        """Execute all G-codes from file content, inserting backups/shuffles/splits as needed."""
        lines = GcodeParser(input_file_content).lines

        active_instance = 'left'
        left_toolhead_pos = LEFT_HOME_POS.copy()
        right_toolhead_pos = RIGHT_HOME_POS.copy()

        for line in lines:
            print(line.gcode_str)
            # TODO: ignore Tx when x is already active; save a few M400s and maybe moves that way.

            if self.is_toolchange_gcode(line):
                next_instance = None
                if line == T0:
                    next_instance = 'left'
                elif line == T1:
                    next_instance = 'right'
                print("  *   draining moves for %s, then changing to %s (M400)" %
                      (active_instance, next_instance))
                self.run_gcode(self.get_active_printer_name(active_instance), "M400")
                print("  *   parking currently active toolhead (%s) " % active_instance)
                if line == T0:
                    self.t1_park()
                    right_toolhead_pos = RIGHT_HOME_POS
                    active_instance = 'left'
                elif line == T1:
                    self.t0_park()
                    left_toolhead_pos = LEFT_HOME_POS
                    active_instance = 'right'

            elif self.is_move_gcode(line):

                # Form target of move.
                if active_instance == 'left':
                    toolhead_pos = left_toolhead_pos
                elif active_instance == 'right':
                    toolhead_pos = right_toolhead_pos

                next_toolhead_pos = toolhead_pos.copy()
                if line.get_param('X') is not None:
                    next_toolhead_pos.x = float(line.get_param('X'))
                if line.get_param('Y') is not None:
                    next_toolhead_pos.y = float(line.get_param('Y'))

                inactive_toolhead_pos = None
                if active_instance == 'left':
                    inactive_toolhead_pos = right_toolhead_pos
                elif active_instance == 'right':
                    inactive_toolhead_pos = left_toolhead_pos

                # Ensure move is safe.
                # (1) Check against destination bounding box.
                overlap_rect = check_for_overlap(inactive_toolhead_pos, next_toolhead_pos)
                # (2) Check swept area against inactive bounding box
                overlap_swept = check_for_overlap_sweep(toolhead_pos, next_toolhead_pos, inactive_toolhead_pos)

                if self.mode == 'simple':
                    if overlap_rect:
                        print("  ! Bounding boxes overlap: %s %s.  Exiting." % (inactive_toolhead_pos, next_toolhead_pos))
                        sys.exit(1)
                    if overlap_swept:
                        print("  ! Swept bounding boxes overlap: %s --> %s vs %s.  Exiting." %
                              (toolhead_pos, next_toolhead_pos, next_toolhead_pos))
                        sys.exit(1)

                elif self.mode == 'smart':
                    # Check if a single move will suffice.
                    if overlap_rect or overlap_swept:
                        self.run_gcode(self.get_active_printer_name(active_instance), "M400")

                        min_y_to_clear_inactive_toolhead = TOOLHEAD_Y_HEIGHT
                        max_y_to_clear_inactive_toolhead = Y_HEIGHT - min_y_to_clear_inactive_toolhead

                        if active_instance == 'left':
                            # Target must be on the right.

                            # Simple shuffle if we're not in the end zone yet.
                            if toolhead_pos.x < TO_X_BACKAWAY:
                                self.simple_shuffles += 1
                                print("  ! Simple shuffle")
                                print("  ! Shuffling inactive t1")
                                right_toolhead_pos = self.t1_shuffle(inactive_toolhead_pos)
                                self.run_gcode(self.get_active_printer_name(active_instance), line.gcode_str)

                            # Segmented move: active is now in the front, and would conflict with a back-to-front shuffled inactive toolhead
                            elif toolhead_pos.y <= min_y_to_clear_inactive_toolhead:
                                self.segmented_shuffles += 1
                                right_toolhead_pos = self.do_right_segmented_sequence(toolhead_pos, min_y_to_clear_inactive_toolhead,
                                                                                      next_toolhead_pos, inactive_toolhead_pos)

                            # Segmented move: active is in the rear
                            elif toolhead_pos.y >= max_y_to_clear_inactive_toolhead:
                                self.segmented_shuffles += 1
                                right_toolhead_pos = self.do_right_segmented_sequence(toolhead_pos, max_y_to_clear_inactive_toolhead,
                                                                                      next_toolhead_pos, inactive_toolhead_pos)

                            # Backup move.
                            else:
                                self.backup_shuffles += 1
                                right_toolhead_pos = self.do_right_backup_sequence(toolhead_pos, inactive_toolhead_pos, active_instance, line)

                        elif active_instance == 'right':
                            # Target must be on the left.

                            # Simple shuffle if we're not in the end zone yet.
                            if toolhead_pos.x > X_BACKAWAY_LEN:
                                self.simple_shuffles += 1
                                print("  ! Simple shuffle")
                                print("  ! Shuffling inactive t0")
                                left_toolhead_pos = self.t0_shuffle(inactive_toolhead_pos)
                                self.run_gcode(self.get_active_printer_name(active_instance), line.gcode_str)

                            # Segmented move: active is in the front
                            elif toolhead_pos.y <= min_y_to_clear_inactive_toolhead:
                                self.segmented_shuffles += 1
                                left_toolhead_pos = self.do_left_segmented_sequence(toolhead_pos, min_y_to_clear_inactive_toolhead,
                                                                                      next_toolhead_pos, inactive_toolhead_pos)

                            # Segmented move: active is in the rear
                            elif toolhead_pos.y >= max_y_to_clear_inactive_toolhead:
                                self.segmented_shuffles += 1
                                left_toolhead_pos = self.do_left_segmented_sequence(toolhead_pos, max_y_to_clear_inactive_toolhead,
                                                                                      next_toolhead_pos, inactive_toolhead_pos)

                            # Backup move.
                            else:
                                self.backup_shuffles += 1
                                right_toolhead_pos = self.do_left_backup_sequence(toolhead_pos, inactive_toolhead_pos, active_instance, line)

                    # If no overlap, just do the straight line.
                    else:
                        self.run_gcode(self.get_active_printer_name(active_instance), line.gcode_str)

                # Should not be necessary... workaround to test, despite M400 insertion bugs.
                if self.m400_always:
                    for instance in [self.left, self.right]:
                        self.run_gcode(self.left, "M400")

                # Update position of toolhead after execution
                if active_instance == 'left':
                    left_toolhead_pos = next_toolhead_pos
                elif active_instance == 'right':
                    right_toolhead_pos = next_toolhead_pos

        for instance in [self.left, self.right]:
            self.run_gcode(instance, "M400")

    def run(self):
        if args.input and not os.path.exists(args.input):
            print("Invalid input file path: %s" % args.input)
            sys.exit(1)

        if args.latency_test:
            dr.test_latency()

        print("Running:")
        left = args.left
        right = args.right

        if (args.home or args.input) and not args.dry_run:
            home(left)
            home(right)

        if args.input:
            self.play_gcodes_file(args.input)

        else:
            if args.meet and not args.dry_run:
                center(left)
                center(right)

            if args.battle:
                dz = Battle(run_gcode, left, right)
                dz.cmdloop()

        if args.home_after and not args.dry_run:
            home(left)
            home(right)

        print("Finished.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a Dual Gantry printer.")
    parser.add_argument('left', help="T0 (left) printer address - something like dz.local")
    parser.add_argument('right', help="T1 (right) printer address - something like dz.local")
    parser.add_argument('--battle', help="Begin battle!", action='store_true')
    parser.add_argument('--meet', help="Meet in center", action='store_true')
    parser.add_argument('--home', help="Home first", action='store_true')
    parser.add_argument('--home-after', help="Home after print", action='store_true')
    parser.add_argument('--dry-run', help="Dry run", action='store_true')
    parser.add_argument('--m400-always', help="Always run M400 after input moves", action='store_true')
    parser.add_argument('--input', help="Input gcode filepath")
    parser.add_argument('--output', help="Output gcode filepath")
    parser.add_argument('--mode', help="Interference mode: simple fails, smart splits moves", default=DEF_MODE)
    parser.add_argument('--latency-test', help="Measure latency of command exec", action='store_true')
    parser.add_argument('--verbose', help="Use more-verbose debug output", action='store_true')

    args = parser.parse_args()

    dr = DuelRunner(args)
    dr.run()
