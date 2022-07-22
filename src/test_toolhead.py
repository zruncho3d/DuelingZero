#!/usr/bin/env python3
# To run tests:
#   pip3 install nose
#   python3 -m nose test_toolhead.py

from point import Point

from toolhead import form_toolhead_sweep, TOOLHEAD_X_WIDTH, TOOLHEAD_Y_HEIGHT, get_toolhead_bounds

test_data = [
    (Point(0.0, 0.0),
     Point(10.0, 10.0),
     Point(0, TOOLHEAD_X_WIDTH / 2 + 1.0),
     True),
    (Point(0.0, 10.0),
     Point(10.0, 0.0),
     Point(TOOLHEAD_X_WIDTH / 2 + 2.0, TOOLHEAD_Y_HEIGHT / 2 + 2.0),
     True),
    (Point(0.0, 0.0),
     Point(100.0, 100.0),
     Point(100.0 + (TOOLHEAD_X_WIDTH / 2 )- 1, 100.0 + (TOOLHEAD_Y_HEIGHT / 2) - 1),
     True)
]


def check_toolhead_sweep(start, end, inactive, desired_outcome):
    outcome = form_toolhead_sweep(start, end).intersects(get_toolhead_bounds(inactive))
    assert outcome == desired_outcome, "start: %s, end: %s, inactive: %s, desired: %s, actual, %s" % \
                                       (start, end, inactive, desired_outcome, outcome)


def test_toolhead_sweeps():
    for test_input in test_data:
        start, end, inactive, desired_outcome = test_input
        yield check_toolhead_sweep, start, end, inactive, desired_outcome
