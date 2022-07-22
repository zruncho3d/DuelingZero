#!/usr/bin/env python3
# To run tests:
#   pip3 install nose
#   python3 -m nose test_gcode_file.py

from duel import DuelRunner

# List of tuples: totals for each type:
# simple_shuffles
# backup_shuffles
# segmented_shuffles
test_data = [
    (0, 0, 0, "examples/single_move.gcode"),
    (2, 0, 2, "examples/large_square_counter_clockwise.gcode"),
]


def check_motion_case(simple, backup, segmented, gcode_file):
    dr = DuelRunner(None)
    dr.play_gcodes_file(gcode_file)
    success = (simple == dr.simple_shuffles and
               backup == dr.backup_shuffles and
               segmented == dr.segmented_shuffles)
    assert success, "%s: simple: %s, backup: %s, segmented: %s, " % \
                    (gcode_file, simple, backup, segmented)


GCODE_FILE_FILTER = None
# Uncomment to test a subset of cases
# GCODE_FILE_FILTER = "examples/single_move.gcode"


def test_motion_case():
    for test_input in test_data:
        simple, backup, segmented, gcode_file = test_input
        if not GCODE_FILE_FILTER or (gcode_file == GCODE_FILE_FILTER):
            yield check_motion_case, simple, backup, segmented, gcode_file
