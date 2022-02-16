# time position set position need per time of day as pers Reference DATA

# Altitude: FLOAT
# Azimut: FLOAT
from PatchData import searchdata
from datetime import datetime
import math


def time_pos():
    azmut, alt = searchdata(830) # retourne azimute et altitude
    # finaliser datetime afin avoir access au l'horloge
    print('Azimut: ', azmut, ' ','Altitude: ' ,alt, 'sup')
    pos_y = 93 # verifier comment l'axe va etre calculer dans le futur
    Vec = math.tan(math.radians(90 - alt)) * pos_y # determine le vecteur longueur
    print('vect: ', Vec)
    angle = 270 - azmut
    pos_x = Vec * math.cos(math.radians(angle)) # donne position x en mm
    print('pos_x: ', pos_x,'mm')
    pos_z = Vec * math.sin(math.radians(angle)) # donne position z en mm
    print('pos_z: ', pos_z, 'mm')
    return pos_x, pos_z


def confirm_angle():
    pass  # TODO


# now = datetime.now()

# full_datetime = strftime("%d/%m/%y at %-H:%M") # day month years hour(24h) minute
# time_now = int(now.strftime("%-H%M"))
# print(time_now)

x, z = time_pos()
print(x,' ', z)
