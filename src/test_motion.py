#!/usr/bin/env python3
# To run tests:
#   pip3 install nose
#   python3 -m nose test_motion.py

from duel import DuelRunner
from point import Point

# Assume back-left, front-right homing, w/o following motion after.
INITIAL_LEFT_POS = Point(0, 170)
INITIAL_RIGHT_POS = Point(170, 0)

# List of tuples: totals for each type:
# simple_shuffles
# backup_shuffles
# segmented_shuffles
test_data = [
    # Single line endzone, G0, no conflict
    (0, 0, 0, ["T0", "G0 Y0"], "single line endzone G0"),
    (0, 0, 0, ["T1", "G0 Y160"], "single line endzone G0"),
    # Single line endzone, G1, no conflict
    (0, 0, 0, ["T0", "G1 Y0"], "single line endzone G1"),
    (0, 0, 0, ["T1", "G1 Y160"], "single line endzone G1"),
    # Single line, no conflict
    (0, 0, 0, ["T0", "G0 X85"], "single line"),
    (0, 0, 0, ["T1", "G0 X160"], "single line"),
    # Single simple shuffle
    (1, 0, 0, ["T0", "G0 X170 Y0"], "simple single shuffle"),
    (1, 0, 0, ["T1", "G0 X0 Y170"], "simple single shuffle"),
    # Two moves that require a single backup shuffle
    (0, 1, 0, ["T0", "G0 X170 Y100", "G0 Y0"], "two moves > backup shuffle"),
    (0, 1, 0, ["T1", "G0 X0 Y100", "G0 Y170"], "two moves > backup shuffle"),
    # Two moves that require a single segmented shuffle (opposite sides of endzone)
    (0, 0, 1, ["T0", "G0 X170", "G0 Y0"], "two moves > segmented shuffle"),
    (0, 0, 1, ["T1", "G0 X0", "G0 Y170"], "two moves > segmented shuffle"),
    # Motion that requires a simple then a complex shuffle
    (0, 1, 1, ["T0", "G0 X170 Y100", "G0 Y0", "G0 Y170"], "simple + complex"),
    (0, 1, 1, ["T1", "G0 X0 Y100", "G0 Y170", "G0 Y0"], "simple + complex"),
    # Small (no-conflict) clockwise square
    (0, 0, 0, ["T0", "G0 X100", "G0 Y100", "G0 X0", "G0 Y170"], "small clockwise square"),
    (0, 0, 0, ["T1", "G0 X100", "G0 Y100", "G0 X170", "G0 Y0"], "small clockwise square"),
    # Small (no-conflict) counter-clockwise square
    (0, 0, 0, ["T0", "G0 Y100", "G0 X100", "G0 Y170", "G0 X0"], "small counter-clockwise square"),
    (0, 0, 0, ["T1", "G0 Y100", "G0 X100", "G0 Y0", "G0 X170"], "small counter-clockwise square"),
    # Large (conflict-inducing) clockwise square
    (0, 0, 1, ["T0", "G0 X170", "G0 Y0", "G0 X0", "G0 Y170"], "large clockwise square"),
    (0, 0, 1, ["T1", "G0 X0", "G0 Y170", "G0 X170", "G0 Y0"], "large clockwise square"),
    # Large (conflict-inducing) counter-clockwise square
    (1, 0, 1, ["T0", "G0 Y0", "G0 X170", "G0 Y170", "G0 X0"], "large counter-clockwise square"),
    (1, 0, 1, ["T1", "G0 Y170", "G0 X0", "G0 Y0", "G0 X170"], "large counter-clockwise square"),
    # TODO: less obvious, partial-overlap cases.
]


def check_motion_case(simple, backup, segmented, gcode, name):
    dr = DuelRunner(None)
    gcode_content = "\n".join(gcode)
    dr.play_gcodes(gcode_content)
    success = (simple == dr.simple_shuffles and
             backup == dr.backup_shuffles and
             segmented == dr.segmented_shuffles)
    assert success, "%s: simple: %s, backup: %s, segmented: %s, " % \
                                       (name, simple, backup, segmented)


NAME_FILTER = None
# Uncomment to test a subset of cases
#NAME_FILTER = 'large counter-clockwise square'


def test_motion_case():
    for test_input in test_data:
        simple, backup, segmented, gcode, name = test_input
        if not NAME_FILTER or (name == NAME_FILTER):
                yield check_motion_case, simple, backup, segmented, gcode, name
