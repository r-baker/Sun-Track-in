# time position set position need per time of day as pers Reference DATA

# Altitude: FLOAT
# Azimut: FLOAT
from PatchData import searchdata
import math

"""
time_pos(time_now) will take the time now and return a position the motor need to be
INPUT: time_now ; INT
DO: fetch azimut and altitude of sun, converte to position in 2D plane
RETURN: pos_x, pos_z ; FLOAT
"""
def time_pos(time_now):
    azmut, alt = searchdata(time_now) # retourne azimute et altitude
    print('Azimut: ', azmut, ' ','Altitude: ' ,alt, 'sup')
    pos_y = 93 # verifier comment l'axe va etre calculer dans le futur
    Vec = math.tan(math.radians(90 - alt)) * pos_y # determine le vecteur longueur
    print('vect: ', Vec)
    angle = 270 - azmut
    pos_x = Vec * math.cos(math.radians(angle)) # donne position x en mm
    print('pos_x: ', pos_x,'mm')  # remove in final version or put front end TBD
    pos_z = Vec * math.sin(math.radians(angle)) # donne position z en mm
    print('pos_z: ', pos_z, 'mm')  # remove in final version or put front end TBD
    return pos_x, pos_z


def confirm_angle():
    pass  # TODO