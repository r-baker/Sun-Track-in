#!/usr/bin/python3

# Altitude: FLOAT
# Azimut: FLOAT

from Reference_Data import get_sun_pos
import math

"""
time_pos(time_now) will take the time now and return a position the motor need to be
INPUT: time_now ; INT
DO: fetch azimut and altitude of sun, converte to position in 2D plane
RETURN: pos_x, pos_z ; FLOAT
"""


def time_pos():
    azmut, alt = get_sun_pos()  # retourne azimute et altitude
    pos_y = 93  # verifier comment l'axe va etre calculer dans le futur
    vec = math.tan(math.radians(90 - alt)) * pos_y  # determine le vecteur longueur
    angle = 270 - azmut
    pos_x = vec * math.cos(math.radians(angle))  # donne position x en mm
    pos_z = vec * math.sin(math.radians(angle))  # donne position z en mm
    return pos_x, pos_z


def confirm_angle():
    pass  # TODO
