#!/usr/bin/python3

import datetime
from datetime import datetime
from datetime import timezone
import Timed_Position
import motor_Control
import Adjusted_Position
import Data_collection
import DHT11
import kp184
from ticlib import TicUSB
from ticlib import *
import time

"""
track_the_sun() main code to get input on sun location and send motor control
INPUT: none
DO: each minute, will check time to see if it use preset sun position(15min) or sensor ajustment(1min)
RETURN: none
"""

motor_1_drive_serial_num = "00383845"  # x axis
motor_2_drive_serial_num = "00383851"  # y axis


def track_the_sun():
    charge_active = kp184.Kunkin_KP184()
    motor_1 = TicUSB(product=TIC_36v4, serial_number=motor_1_drive_serial_num)
    motor_2 = TicUSB(product=TIC_36v4, serial_number=motor_2_drive_serial_num)
    motor_Control.motor_setup(motor_1)  # setup the motor
    motor_Control.motor_setup(motor_2)
    # calibration comme here
    present_mode = "Calibration"
    motor_Control.motor_calibration(motor_1, 1)
    motor_Control.motor_calibration(motor_2, 2)
    pos_x_now = 0
    pos_y_now = 0
    while True:
        # temperature, humiditer = DHT11.humidy_and_temp_sensor() # temporary disable
        today_now = datetime.utcnow() # get time of day
        minute_now = int(today_now.strftime("%M"))
        # check altitude for the sun for nighttime
        if minute_now == 00 or minute_now % 5 == 0:
            present_mode = "Library position"
            pos_x, pos_y = Timed_Position.time_pos()
            print(pos_x, " ", pos_y)
            mm_x, mm_y = motor_Control.pos_to_distance_travel(pos_x_now, pos_y_now, pos_x, pos_y)  # motor code
            pos_x_now = pos_x
            pos_y_now = pos_y
            mm_x_inv = mm_x * (-1)
            pos_motor_x = motor_Control.distance_travel_to_motor_position(mm_x, motor_1)
            pos_motor_y = motor_Control.distance_travel_to_motor_position(mm_y, motor_2)
            motor_Control.motor_position(motor_1, pos_motor_x)
            motor_Control.motor_position(motor_2, pos_motor_y)
            # collect de donné
            wattage = charge_active.get_P_measure()
            amperage = charge_active.get_I_measure()
            inclinaison = 0
            cap_courant = 0
            temperature = 0  # temporaire
            humiditer = 0  # temporaire
            position_motor_1 = motor_1.get_current_position()
            position_motor_2 = motor_2.get_current_position()
            Data_collection.log_data(wattage, amperage, temperature, humiditer, inclinaison
                                     , cap_courant, position_motor_1, position_motor_2, present_mode, today_now)
        else:
            mode = "Ajusted position"
            angle_to_search = [0, 45, 90, 135, 180, 225, 270, 315]
            for rayon in range(1, 4):
                for angle in angle_to_search:
                    present_mode = mode + " rayon=" + str(rayon) + " angle=" + str(angle)
                    search_x, search_y = Adjusted_Position.circle_search_pts(rayon, angle)

                    search_pos_x = Adjusted_Position.circle_pos(pos_x_now, search_x)
                    search_motor_x = motor_Control.distance_travel_to_motor_position(search_pos_x, motor_1)
                    motor_Control.motor_position(motor_1, search_motor_x)

                    search_pos_y = Adjusted_Position.circle_pos(pos_y_now, search_y)
                    search_motor_y = motor_Control.distance_travel_to_motor_position(search_pos_y, motor_2)
                    motor_Control.motor_position(motor_2, search_motor_y)
                    wattage = charge_active.get_P_measure()
                    amperage = charge_active.get_I_measure()
                    inclinaison = 0
                    cap_courant = 0
                    temperature = 0 #temporaire
                    humiditer = 0 #temporaire
                    position_motor_1 = motor_1.get_current_position()
                    position_motor_2 = motor_2.get_current_position()
                    Data_collection.log_data(wattage, amperage, temperature, humiditer, inclinaison
                                             , cap_courant, position_motor_1, position_motor_2, present_mode, today_now)
        time.sleep(60)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    track_the_sun()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
