#!/usr/bin/env python3
# Script to test out a Dueling Zero printer with two toolheads.
#
# To see arguments, invoke this script with:
#   ./duel.py -h
#
# Sample invocation:
# python duel.py dz.local:7125 dz.local:7126 --duel
#

import argparse
import cmd
import json
import os
import pprint
import statistics
import random
import re
import sys
import time

import requests
from gcodeparser import GcodeParser, GcodeLine


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

    def random_y(self):
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
READ_TIMEOUT=180




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


def run_gcode_blocking(printer, gcode, verbose=False):
    """Run a gcode command to completion and return the result, along with an M400.
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

# # https://stackoverflow.com/questions/7685984/add-method-that-works-with-either-a-point-object-or-a-tuple
# class Point(tuple):
#     def __new__(cls, x, y):
#         return tuple.__new__(cls, (x, y))
#
#     def __add__(self, other):
#         return Point(self[0] + other[0], self[1] + other[1])
#
#     def __repr__(self):
#         return 'Point({0}, {1})'.format(self[0], self[1])
#

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        elif isinstance(other, tuple):
            return Point(self.x + other[0], self.y + other[1])
        else:
            raise TypeError("unsupported operand type(s) for +: 'Point' and '{0}'".format(type(other)))

    def __repr__(self):
        return 'Point ({0}, {1})'.format(self.x, self.y) # Remove the u if you're using Python 3



class DuelRunner():

    def __init__(self, args):
        self.left = args.left
        self.right = args.right
        self.toolhead_x_offset = float(args.toolhead_x_offset)
        self.args = args

    """Put away Toolhead T0"""
    def T0park(self):
        for gcode in ["G0 X1", "G0 Y159"]:
            print("> ", gcode)
            run_gcode(self.left, gcode)
        print("> ", "M400")
        run_gcode(self.left, "M400")

    """Put away Toolhead T1"""
    def T1park(self):
        for gcode in ["G0 X159", "G0 Y1"]:
            print("> ", gcode)
            run_gcode(self.right, gcode)
        print("> ", "M400")
        run_gcode(self.right, "M400")

    def play_gcodes(self, input):

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


        with open(input, 'r') as f:
            gcode = f.read()

        lines = GcodeParser(gcode).lines
        #pprint.pprint(lines)

        active_instance = 'left'
        toolhead_pos = Point(0, 0)
        left_toolhead_pos = None
        right_toolhead_pos = None
        for line in lines:
            if line == T0 or line == T1:
                print("*   completing all in-progress moves before changing toolhead to %s (M400)" % active_instance)
                if not self.args.dry_run:
                    run_gcode(self.left, "M400")
                    run_gcode(self.right, "M400")
                print("> ", line.gcode_str)
                print("*   parking other (%s) toolhead" % get_nonactive_instance(active_instance))
                if line == T0:
                    if not self.args.dry_run:
                        self.T1park()
                    active_instance = 'left'
                elif line == T1:
                    if not self.args.dry_run:
                        self.T0park()
                    active_instance = 'right'
            elif line.command == ('G', 0) or line.command == ('G', 1):
                print("> ", line.gcode_str)

                # Process move target.
                next_toolhead_pos = toolhead_pos
                if line.get_param('X') is not None:
                    next_toolhead_pos.x = line.get_param('X')
                if line.get_param('Y') is not None:
                    next_toolhead_pos.y = line.get_param('Y')

                # TODO: ensure safety of the move.
                # Check against bounding box.

                # Check against full move.

                # TODO: batch many gcodes into one command to maximize lookahead

                # Apply offsets if this is the right toolhead.
                mod_line = line
                if active_instance == 'right':
                    if line.get_param('X'):
                        mod_line.update_param('X', line.get_param('X') + self.toolhead_x_offset)

                if not self.args.dry_run:
                    run_gcode(get_active_printer_name(active_instance), mod_line.gcode_str)

                # Update position of toolhead after execution
                if line.get_param('X') is not None:
                    toolhead_pos.x = line.get_param('X')
                if line.get_param('Y') is not None:
                    toolhead_pos.y = line.get_param('Y')


    def run(self):
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
