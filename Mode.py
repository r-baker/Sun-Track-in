#!/usr/bin/python3

import datetime
from datetime import datetime
from datetime import timezone
import Reference_Data
import Timed_Position
import Motor_Control
import Adjusted_Position
import Data_collection
import DHT11
import kp184
from ticlib import TicUSB
from ticlib import *
import time

motor_x_drive_serial_num = "00383845"  # x axis
motor_y_drive_serial_num = "00383851"  # y axis


def mode_selection():
    x = input(" Mode automatique : press 1, mode manuel : press 2 ")
    if x == '1':
        print('Mode automatic')
        automatic()
    elif x == '2':
        print('Mode manuel')
        manuel()
    else:
        print('...')
        motor_x = TicUSB(product=TIC_36v4, serial_number=motor_x_drive_serial_num)
        motor_y = TicUSB(product=TIC_36v4, serial_number=motor_y_drive_serial_num)
        motor_x.deenergize()
        # motor_1.safe_start()

        motor_y.deenergize()
        # motor_2.safe_start()


def automatic():
    charge_active = kp184.Kunkin_KP184()
    motor_x = TicUSB(product=TIC_36v4, serial_number=motor_x_drive_serial_num)
    motor_y = TicUSB(product=TIC_36v4, serial_number=motor_y_drive_serial_num)
    Motor_Control.motor_setup(motor_x)  # setup the motor
    Motor_Control.motor_setup(motor_y)
    # calibration comme here
    present_mode = "Calibration"
    Motor_Control.both_motor_calibration(motor_x, motor_y)
    pos_x_now = 0
    pos_y_now = 0
    while True:
        night_time_mode()
        temperature, humiditer = DHT11.humidy_and_temp_sensor()  # temporary disable
        today_now = datetime.utcnow()  # get time of day
        minute_now = int(today_now.strftime("%M"))
        # check altitude for the sun for nighttime
        if minute_now == 00 or minute_now % 5 == 0:
            present_mode = "Library position"
            pos_x, pos_y = Timed_Position.time_pos()
            print(pos_x, " ", pos_y)
            mm_x, mm_y = Motor_Control.pos_to_distance_travel(pos_x_now, pos_y_now, pos_x, pos_y)  # motor code
            pos_x_now = pos_x
            pos_y_now = pos_y
            mm_x_inv = mm_x * (-1)
            pos_motor_x = Motor_Control.distance_travel_to_motor_position(mm_x, motor_x)
            pos_motor_y = Motor_Control.distance_travel_to_motor_position(mm_y, motor_y)
            Motor_Control.motor_position(motor_x, pos_motor_x)
            Motor_Control.motor_position(motor_y, pos_motor_y)
            # collect de donné
            position_motor_x = motor_x.get_current_position()
            position_motor_y = motor_y.get_current_position()
            charge_active.set_load_mode("CW")
            print("mode de la charge artive presentement: ", charge_active.get_load_mode())
            charge_active.set_CW_setting(60)
            print("setting du mode CW: ", charge_active.get_CW_setting())
            wattage = charge_active.get_P_measure()
            amperage = charge_active.get_I_measure()
            Data_collection.save_data(wattage, amperage, position_motor_x, position_motor_y, temperature, humiditer,
                                      present_mode, today_now)

        else:
            mode = "Ajusted position"
            angle_to_search = [0, 45, 90, 135, 180, 225, 270, 315]
            for rayon in range(1, 4):
                for angle in angle_to_search:
                    present_mode = mode + " rayon=" + str(rayon) + " angle=" + str(angle)
                    search_x, search_y = Adjusted_Position.circle_search_pts(rayon, angle)

                    search_pos_x = Adjusted_Position.circle_pos(pos_x_now, search_x)
                    search_motor_x = Motor_Control.distance_travel_to_motor_position(search_pos_x, motor_x)
                    Motor_Control.motor_position(motor_x, search_motor_x)

                    search_pos_y = Adjusted_Position.circle_pos(pos_y_now, search_y)
                    search_motor_y = Motor_Control.distance_travel_to_motor_position(search_pos_y, motor_y)
                    Motor_Control.motor_position(motor_y, search_motor_y)
                    # collect de donner
                    position_motor_x = motor_x.get_current_position()
                    position_motor_y = motor_y.get_current_position()
                    charge_active.set_load_mode("CW")
                    print("mode de la charge artive presentement: ", charge_active.get_load_mode())
                    charge_active.set_CW_setting(60)
                    print("setting du mode CW: ", charge_active.get_CW_setting())
                    wattage = charge_active.get_P_measure()
                    amperage = charge_active.get_I_measure()
                    Data_collection.save_data(wattage, amperage, position_motor_x, position_motor_y, temperature,
                                              humiditer,
                                              present_mode, today_now)

        time.sleep(60)


def manuel():
    charge_active = kp184.Kunkin_KP184()
    present_mode = "Manuel"
    motor_x = TicUSB(product=TIC_36v4, serial_number=motor_x_drive_serial_num)
    motor_y = TicUSB(product=TIC_36v4, serial_number=motor_y_drive_serial_num)
    Motor_Control.motor_setup(motor_x)  # setup the motor
    Motor_Control.motor_setup(motor_y)
    # calibration comme here

    # motor_Control.motor_calibration(motor_1, 1)
    # motor_Control.motor_calibration(motor_2, 2)

    commande = 0

    while commande != 'p':

        commande = input('Step pls (int, 10 = 1mm env.)')
        commande2 = 0
        while commande2 != 'p':
            temperature, humiditer = DHT11.humidy_and_temp_sensor()
            today_now = datetime.utcnow()

            if commande2 == 'w':
                print('commande w reçu')
                motor_x.set_target_position(motor_x.get_current_position() + int(commande))

            elif commande2 == 'a':
                print('commande a reçu')
                motor_y.set_target_position(motor_y.get_current_position() - int(commande))

            elif commande2 == 's':
                print('commande s reçu')
                motor_x.set_target_position(motor_x.get_current_position() - int(commande))

            elif commande2 == 'd':
                print('commande d reçu')
                motor_y.set_target_position(motor_y.get_current_position() + int(commande))

            elif commande2 == 'i':
                print('commande d reçu')
                position_motor_x = motor_x.get_current_position()
                position_motor_y = motor_y.get_current_position()
                charge_active.set_load_mode("CW")
                print("mode de la charge artive presentement: ", charge_active.get_load_mode())
                charge_active.set_CW_setting(60)
                print("setting du mode CW: ", charge_active.get_CW_setting())
                wattage = charge_active.get_P_measure()
                amperage = charge_active.get_I_measure()
                Data_collection.save_data(wattage, amperage, position_motor_x, position_motor_y, temperature, humiditer,
                                          present_mode, today_now)

            elif commande2 == 'g':
                print('commande g reçu, ARRET DES MOTEUR')
                motor_x.halt_and_hold()
                motor_y.halt_and_hold()

            elif commande2 == 'c':
                print('commande c reçu, Retour au choix de mode')
                mode_selection()

            elif commande2 == 'u':
                print('commande u reçu, Retour au centre')
                Motor_Control.both_motor_calibration(motor_x, motor_y)

            else:
                print('...')
            commande2 = input('Direction (WASD), sauvegarde donner(i), arret (g), retour au choix(c)')

    print('Commande non valide, deenergize')

    motor_x.deenergize()
    # motor_1.safe_start()

    motor_y.deenergize()
    # motor_2.safe_start()


def night_time_mode():
    altitud = Reference_Data.get_sun_altitude()
    while altitud < 20.0:
        time.sleep(0.1)
