#!/usr/bin/python3

import time
from ticlib import TicUSB
import ticlib
from ticlib import *

#  x axis  serial_number="00383845"
#  y axis   serial_number="00383851"

"""
motor_setup
INPUT: motor number to setup
DO: initial setup before motor use
RETURN: none
"""


def motor_setup(motor_num):
    motor_num.reset()
    motor_num.clear_driver_error()
    motor_num.set_current_limit(3000)
    motor_num.set_step_mode(2)  # 1/4 step, see wiki for full setup option
    motor_num.halt_and_set_position(0)
    motor_num.energize()
    motor_num.exit_safe_start()


"""
both motor calibre
INPUT: both motor reference
DO: calibrate both motor to center
RETURN: none
"""


def both_motor_calibration(motor_x, motor_y):
    motor_calibration(motor_x, 1)
    motor_calibration(motor_y, 2)


"""
motor calibre
INPUT: motor reference and reference number
DO: calibrate selected motor to center
RETURN: none
"""


def motor_calibration(motor_num, num):
    center_x = 140
    center_y = 59
    if num == 1:
        pos_to_center = center_x
    else:
        pos_to_center = center_y

    motor_num.go_home(0)  # verifier si 0 es vers l'avant ou l'arriere
    # 0 reverse, 1 forward
    encoder_motor = motor_num.get_encoder_position()
    time.sleep(0.2)

    while encoder_motor == 0:
        time.sleep(2)
        encoder_motor = motor_num.get_encoder_position()
    motor_num.halt_and_set_position(0)

    position_center = distance_travel_to_motor_position(pos_to_center, motor_num)
    motor_position(motor_num, position_center)
    motor_num.halt_and_set_position(0)


"""
motor position
INPUT: motor reference and target position
DO: send a target position to reach for the motor to go to
RETURN: none
"""


def motor_position(motor_num, target_position):
    motor_num.set_target_position(target_position)
    while motor_num.get_current_position() != motor_num.get_target_position() and motor_num.get_current_velocity() != 0:
        time.sleep(0.1)


def pos_to_distance_travel(last_x, last_z, new_x, new_z):
    distance_x = last_x - new_x
    distance_z = last_z - new_z
    return distance_x, distance_z


def distance_travel_to_motor_position(pos_mm, motor):
    stepSize = motor.get_step_mode()
    stepSizeConverted = step_mode_converter(stepSize)
    # 2mm/revolution, 200 step per revotion for full step, in mm 2 point passe the decimal point
    # pos_motor = pos_mm * ((200 / stepSizeConverted) * 0.5)
    pos_motor = (pos_mm / 2) * 100

    return int(pos_motor)


def step_mode_converter(step):
    if step == 0:
        step_mode_converted = 1  # full step
    elif step == 1:
        step_mode_converted = 0.5  # 1/2 step
    elif step == 2:
        step_mode_converted = 0.25  # 1/4 step
    elif step == 3:
        step_mode_converted = 0.125  # 1/8 step
    elif step == 4:
        step_mode_converted = 0.0625  # 1/16 step
    elif step == 5:
        step_mode_converted = 0.03125  # 1/32 step
    elif step == 6:
        step_mode_converted = 0.015625  # 1/64 step
    elif step == 7:
        step_mode_converted = 0.0078125  # 1/128 step
    elif step == 8:
        step_mode_converted = 0.00390625  # 1/256 step
    elif step == 9:
        step_mode_converted = 0.001953125  # 1/512 step
    return step_mode_converted
