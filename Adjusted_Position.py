# send adjustement to position en between timed position back to the main
import numpy as np


# Power_Enough: BOOL

def MPPT():
    pass  # TODO


def circle_search_pts(rayon, angle):
    x = rayon * (np.cos(np.radians(angle)))
    y = rayon * (np.sin(np.radians(angle)))
    return x, y


def circle_pos(present_pos, adjustment_pos ):
    circle_posit = present_pos + adjustment_pos
    return circle_posit

