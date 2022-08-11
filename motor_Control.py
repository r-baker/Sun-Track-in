#!/usr/bin/python

import time
from ticlib import TicUSB
import ticlib
from ticlib import *

step_mode = 1 / 16


#  x axis  serial_number="00383845"
#  y axis   serial_number="00383851"


def motor_setup(motor_num):
    motor_num.reset()
    motor_num.clear_driver_error()
    motor_num.set_decay_mode(0)
    motor_num.set_current_limit(3000)
    motor_num.set_step_mode(2)  # 1/4 step, see wiki for full setup option
    motor_num.halt_and_set_position(0)
    motor_num.energize()
    motor_num.exit_safe_start()


def motor_calibration(motor_num, num):
    center_x = 104
    center_y = 194
    if num == 1:
        pos_to_center = center_y
    else:
        pos_to_center = center_x

    motor_num.go_home(0)  # verifier si 0 es vers l'avant ou l'arriere
    # 0 reverse, 1 forward
    flag_array = motor_num.get_misc_flags()
    flag = flag_array[1]
    while flag == 19:
        time.sleep(0.5)
        flag_array = motor_num.get_misc_flags()
        flag = flag_array[1]
    # unsertaing flag is 19
    position_center = distance_travel_to_motor_position(pos_to_center, motor_num)
    motor_position(motor_num, position_center)


def motor_position(motor_num, target_position):
    motor_num.set_target_position(target_position)
    while motor_num.get_current_position() != motor_num.get_target_position():
        time.sleep(0.1)

    # motor_num.deenergize()
    # motor_num.enter_safe_start()


def pos_to_distance_travel(last_x, last_z, new_x, new_z):
    distance_x = last_x - new_x
    distance_z = last_z - new_z
    return distance_x, distance_z


def distance_travel_to_motor_position(pos_mm, motor):
    stepSize = motor.get_step_mode()
    stepSizeConverted = step_mode_converter(stepSize)
    # 2mm/revolution, 200 step per revotion for full step, in mm 2 point passe the decimal point
    pos_motor = pos_mm * ((200 / stepSizeConverted) * 0.5)

    return pos_motor


def calibration_test():  # to be tested
    center_x = 104
    center_y = 194
    tic = TicUSB(product=TIC_36v4, serial_number="00383845")
    tic.go_home(0)  # verifier si 0 es vers l'avant ou l'arriere
    # 0 reverse, 1 forward
    flag_array = tic.get_misc_flags()
    flag = flag_array[1]
    while flag == 19:
        time.sleep(0.5)
        flag_array = tic.get_misc_flags()
        flag = flag_array[1]
    # unsertaing flag is 19
    position_center_y = distance_travel_to_motor_position(center_y, tic)
    motor_position(tic, position_center_y)
    tic.halt_and_set_position(0)


def test_motor():
    tic = TicUSB(product=TIC_36v4, serial_number="00383845")

    tic.halt_and_set_position(0)
    tic.energize()
    tic.exit_safe_start()

    positions = [500, 300, 800, 0]
    for position in positions:
        tic.set_target_position(position)
        while tic.get_current_position() != tic.get_target_position():
            time.sleep(0.1)

    tic.deenergize()
    tic.enter_safe_start()


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


test_motor()
