#!/usr/bin/env python3
# Script to test out a Dueling Zero printer with two toolheads.
#
# To see arguments, invoke this script with:
#   ./duel.py -h
#
# Sample invocations:
#   python duel.py dz.local:7125 dz.local:7126 --duel
#   ./duel.py dz.local:7125 dz.local:7126 --input sample.gcode --home --home_after
#

import argparse
import cmd
import copy
import os
import random
import sys

from gcodeparser import GcodeParser, GcodeLine
import requests

from toolhead import LEFT_HOME_POS, RIGHT_HOME_POS, check_for_overlap, check_for_overlap_sweep


# Offset of T1 relative to T0, so that they align.
# Should roughly match the depth of the toolhead in X and width of the toolhead too.
DEF_TOOLHEAD_X_OFFSET = 0.0


# Default mode to use.
# - basic: use a ~120 x ~120 chunk of the workspace where T0 parks at the back left and T1 parks at the front right.
MODES = ['basic']
DEF_MODE = 'basic'


class Duel(cmd.Cmd, object):

    def __init__(self, left, right):
        self.left = left
        self.right = right
        super(Duel, self).__init__()

    @staticmethod
    def random_y():
        return random.randint(30, 90)

    def do_l(self, arg):
        print("Doing left")
        run_gcode(self.left, "G0 X15 F1200")
        run_gcode(self.left, "G0 X60 Y%s F6000" % self.random_y())

    def do_r(self, arg):
        print("Doing right")
        run_gcode(self.right, "G0 X100 F1200")
        run_gcode(self.right, "G0 X60 Y%s F6000" % self.random_y())


# Set this high enough to handle any command you'd run.
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
        self.left = args.left
        self.right = args.right
        self.toolhead_x_offset = float(args.toolhead_x_offset)
        self.args = args

    """Put away Toolhead T0"""
    def t0_park(self):
        for gcode in ["G0 X1", "G0 Y159", "M400"]:
            print("> ", gcode)
            self.run_gcode(self.left, gcode)

    """Put away Toolhead T1"""
    def t1_park(self):
        for gcode in ["G0 X159", "G0 Y1", "M400"]:
            print("> ", gcode)
            self.run_gcode(self.right, gcode)

    @staticmethod
    def is_toolchange_gcode(line):
        return line == T0 or line == T1

    def is_move_gcode(self, line):
        return line.command == ('G', 0) or line.command == ('G', 1)

    def run_gcode(self, instance, gcode_line):
        if not self.args.dry_run:
            run_gcode(instance, gcode_line)

    def play_gcodes(self, input_file):

        def get_active_printer_name(active_instance):
            if active_instance == 'left':
                return self.left
            else:
                return self.right

        def get_nonactive_instance(active_instance):
            if active_instance == 'left':
                return 'right'
            else:
                return 'left'

        with open(input_file, 'r') as f:
            gcode = f.read()

        lines = GcodeParser(gcode).lines

        active_instance = 'left'
        left_toolhead_pos = LEFT_HOME_POS.copy()
        right_toolhead_pos = RIGHT_HOME_POS.copy()

        for line in lines:
            print("> ", line.gcode_str)

            if self.is_toolchange_gcode(line):
                print("  *   completing all in-progress moves for %s before changing toolhead to %s (M400)" %
                      (active_instance, get_nonactive_instance(active_instance)))
                self.run_gcode(get_active_printer_name(active_instance), "M400")
                print("  *   parking other (%s) toolhead" % active_instance)
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

                next_toolhead_pos = toolhead_pos
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

                if overlap_rect:
                    print("!!! Bounding boxes overlap: %s %s.  Exiting." % (inactive_toolhead_pos, next_toolhead_pos))
                    sys.exit(1)

                # (2) Check swept area against inactive bounding box
                overlap_swept = check_for_overlap_sweep(toolhead_pos, next_toolhead_pos, inactive_toolhead_pos)

                if overlap_swept:
                    print("!!! Swept bounding boxes overlap: %s --> %s vs %s.  Exiting." %
                          (toolhead_pos, next_toolhead_pos, next_toolhead_pos))
                    sys.exit(1)

                # Apply offsets if this is the right toolhead.
                mod_line = line
                if active_instance == 'right':
                    if line.get_param('X'):
                        mod_line.update_param('X', line.get_param('X') + self.toolhead_x_offset)

                if not self.args.dry_run:
                    self.run_gcode(get_active_printer_name(active_instance), mod_line.gcode_str)

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

        print("Running:")
        left = args.left
        right = args.right

        if args.home and not args.dry_run:
            home(left)
            home(right)

        if args.input:
            self.play_gcodes(args.input)

        else:
            if args.meet and not args.dry_run:
                center(left)
                center(right)

            if args.duel:
                dz = Duel(left, right)
                dz.cmdloop()

        if args.home_after and not args.dry_run:
            home(left)
            home(right)

        print("Finished.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a multi-Klipper-instance test.")
    parser.add_argument('left', help="T0 (left) printer address - something like mainsailos.local")
    parser.add_argument('right', help="T1 (right) printer address - something like mainsailos.local")
    parser.add_argument('--duel', help="Begin duel!", action='store_true')
    parser.add_argument('--meet', help="Meet in center", action='store_true')
    parser.add_argument('--home', help="Home first", action='store_true')
    parser.add_argument('--home_after', help="Home after print", action='store_true')
    parser.add_argument('--dry-run', help="Dry run", action='store_true')
    parser.add_argument('--input', help="Input gcode filepath")
    parser.add_argument('--toolhead_x_offset', help="Toolhead X offset", default=DEF_TOOLHEAD_X_OFFSET)
    parser.add_argument('--mode', help="Toolhead X offset", default=DEF_MODE)
    parser.add_argument('--verbose', help="Use more-verbose debug output", action='store_true')

    args = parser.parse_args()

    dr = DuelRunner(args)
    dr.run()
