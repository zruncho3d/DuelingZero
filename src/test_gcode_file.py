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
    # Hand-crafted g-codes
    (0, 0, 0, "examples/single_move.gcode"),
    (2, 0, 2, "examples/large_square_counter_clockwise.gcode"),
    # Slicer-generated g-codes
    # Single large file.
    (2, 0, 2, "gcode/square_2_layer.gcode"),
    # T0 and T1 commands here.
    (4, 0, 4, "gcode/square_2_layer_alternating_4_layers_total.gcode"),

    (None, 0, None, "gcode/square_1_layer_filled_10_perim.gcode"),
    (None, 0, None, "gcode/square_1_layer_filled_1_perim.gcode"),
    (None, None, None, "gcode/square_1_layer_filled_fill_angle_0.gcode"),  # 3, 0, 1
    (None, None, None, "gcode/square_1_layer_filled_fill_angle_45.gcode"),  # 3, 0, 1
    (None, None, None, "gcode/square_1_layer_filled_fill_angle_90.gcode"), # 2, 0, 73
    (None, None, None, "gcode/cylinder_1_layer_filled_1_perim.gcode"), # 2, 2, 1
    (None, None, None, "gcode/cylinder_1_layer_filled_10_perim.gcode"), # 3, 10, 10
]

PRINT_STATS_FOR_NULL_TEST = True

def check_motion_case(simple, backup, segmented, gcode_file):
    dr = DuelRunner(None)
    dr.play_gcodes_file(gcode_file)
    if simple is not None and backup is not None and segmented is not None:
        success = (simple == dr.simple_shuffles and
                   backup == dr.backup_shuffles and
                   segmented == dr.segmented_shuffles)
        assert success, "%s:\nsimple: saw %s but expected %s;\n" \
                "backup: saw %s but expected %s;\n" \
                " segmented: saw %s but expected %s, " % \
                        (gcode_file, simple, dr.simple_shuffles,
                         backup, dr.backup_shuffles, segmented, dr.segmented_shuffles)
    elif  PRINT_STATS_FOR_NULL_TEST:
        print("Stats: %s, %s, %s" % (dr.simple_shuffles, dr.backup_shuffles, dr.segmented_shuffles))


GCODE_FILE_FILTER = None
# Uncomment to test a subset of cases
GCODE_FILE_FILTER = "gcode/square_2_layer.gcode"


def test_motion_case():
    for test_input in test_data:
        simple, backup, segmented, gcode_file = test_input
        if not GCODE_FILE_FILTER or (GCODE_FILE_FILTER in gcode_file):
            yield check_motion_case, simple, backup, segmented, gcode_file
