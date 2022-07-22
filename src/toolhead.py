#!/usr/bin/env python3

from shapely.geometry import Polygon

from point import Point

# Change these values to match your printer.
Y_HEIGHT = 160.0
Y_HIGH = 159.0
Y_LOW = 1.0
X_WIDTH = 165.0
X_HIGH = 164.0
X_LOW = 1.0

LEFT_ALT_Y = Y_LOW
RIGHT_ALT_Y = Y_HIGH

LEFT_HOME_POS = Point(X_LOW, Y_HIGH)
RIGHT_HOME_POS = Point(X_HIGH, Y_LOW)

SHUFFLE_SPEED = 15000
BACKAWAY_SPEED = 15000
PARK_SPEED = 15000

# Change these values to match your toolhead.  Values are for a MiniAB/MiniAS.
EXTRA_TOOLHEAD_CLEARANCE = 0.25
TOOLHEAD_X_WIDTH = 40.0 + EXTRA_TOOLHEAD_CLEARANCE * 2
TOOLHEAD_Y_HEIGHT = 53.0 + EXTRA_TOOLHEAD_CLEARANCE * 2

X_BACKAWAY_LEN = TOOLHEAD_X_WIDTH + 5
TO_X_BACKAWAY = 165.0 - X_BACKAWAY_LEN
T1_X_BACKAWAY = X_BACKAWAY_LEN


def get_shapely_rectangle(p1, p2):
    return Polygon([(p1.x, p1.y), (p2.x, p1.y), (p2.x, p2.y), (p1.x, p2.y)])


def get_toolhead_bounds(p):
    bottom_left = Point(p.x - TOOLHEAD_X_WIDTH / 2, p.y - TOOLHEAD_Y_HEIGHT / 2)
    top_right = Point(p.x + TOOLHEAD_X_WIDTH / 2, p.y + TOOLHEAD_Y_HEIGHT / 2)
    return get_shapely_rectangle(bottom_left, top_right)


# https://gis.stackexchange.com/questions/90055/finding-if-two-polygons-intersect-in-python
def check_for_overlap(p1, p2):
    poly1 = get_toolhead_bounds(p1)
    poly2 = get_toolhead_bounds(p2)
    overlap = poly1.intersects(poly2)
    return overlap


def check_for_overlap_sweep(toolhead_pos, next_toolhead_pos, inactive_toolhead_pos):
    return form_toolhead_sweep(toolhead_pos, next_toolhead_pos).intersects(
        get_toolhead_bounds(inactive_toolhead_pos))


# Not quite rect bounds, but most of it.  Rect bounds can cover the rest of the true swept area.
def form_toolhead_sweep(p_a, p_b):
    """Return Polygon with quad covering the area swept by the translated rectangle,
    but not the "far away" corners of it."""
    # Align points so that p1 is to left of p2
    if p_a.x < p_b.x:
        p1 = p_a
        p2 = p_b
    else:
        p1 = p_b
        p2 = p_a

    if p1.y > p2.y:
        # Top left to bottom right
        return Polygon([(p1.x - TOOLHEAD_X_WIDTH / 2, p1.y - TOOLHEAD_Y_HEIGHT / 2),
                        (p1.x + TOOLHEAD_X_WIDTH / 2, p1.y + TOOLHEAD_Y_HEIGHT / 2),
                        (p2.x + TOOLHEAD_X_WIDTH / 2, p2.y + TOOLHEAD_Y_HEIGHT / 2),
                        (p2.x - TOOLHEAD_X_WIDTH / 2, p2.y - TOOLHEAD_Y_HEIGHT / 2)])
    else:
        # Bottom left to top right, or left to right and flat.
        return Polygon([(p1.x - TOOLHEAD_X_WIDTH / 2, p1.y + TOOLHEAD_Y_HEIGHT / 2),
                        (p1.x + TOOLHEAD_X_WIDTH / 2, p1.y - TOOLHEAD_Y_HEIGHT / 2),
                        (p2.x + TOOLHEAD_X_WIDTH / 2, p2.y - TOOLHEAD_Y_HEIGHT / 2),
                        (p2.x - TOOLHEAD_X_WIDTH / 2, p2.y + TOOLHEAD_Y_HEIGHT / 2)])
