# this will collect data and build daily log
import csv
import time
import os.path


# temperature: INT
# Humidity: INT

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



