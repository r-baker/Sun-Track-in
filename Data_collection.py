#!/usr/bin/python3

import csv
import time
import os.path
from ticlib import *


# temperature: INT
# Humidity: INT
"""
log_data
INPUT: puissance charge active, courant charge active, temperature, humidité, inclinaison( a etre implimenter capteur gyro), capteur courant(pas implementer) position moteur, mode dutilisation, temps utc
DO: get input information, creat the file and save the information for later
RETURN: File with all pertinent information in csv format 
"""
def log_data(ca_pui, ca_cou, cap_temp, cap_hum, cap_incl, cap_cou, pos_x, pos_y, mode, temp_utc):
    date_today = time.strftime("%Y%m%d")
    file_time = '.csv'
    file_name = date_today + file_time
    print(file_name)
    file_exists = os.path.exists(file_name)

    fieldnames = ['charge_active_puissance', 'charge_active_courant', 'capteur_temperature', 'capteur_humidité',
                  'capteur_inclinaison',
                  'capteur_courant',
                  'moteur_position_x', 'moteur_position_y', 'mode_position', 'temps_utc']

    row = [ca_pui, ca_cou, cap_temp, cap_hum, cap_incl, cap_cou, pos_x, pos_y, mode, temp_utc]
    if file_exists:
        with open(file_name, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(row)
    else:
        with open(file_name, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(fieldnames)
            writer.writerow(row)

"""
save_data
INPUT: wattage, amperage, position_motor_x, position_motor_y, temperature, humiditer, present_mode, today_now
DO: used to call fonction save information to file
RETURN: none
"""
def save_data(wattage, amperage, position_motor_x, position_motor_y, temperature, humiditer, present_mode, today_now):
    # wattage = charge_act.get_P_measure()
    # amperage = charge_act.get_I_measure()
    inclinaison = 0
    cap_courant = 0
    # temperature = 0  # temporaire
    # humiditer = 0  # temporaire
    # position_motor_x = motor_x.get_current_position()
    # position_motor_y = motor_y.get_current_position()
    log_data(wattage, amperage, temperature, humiditer, inclinaison
             , cap_courant, position_motor_x, position_motor_y, present_mode, today_now)
