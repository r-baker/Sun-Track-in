#!/usr/bin/python

import time
import RPi.GPIO as GPIO
from drive_setup import setup_serial


def going_to_pos(last_x, last_z, new_x, new_z):
    distance_x = last_x - new_x
    distance_z = last_z - new_z
    return distance_x, distance_z


def pos_to_step(pos_mm):
    step = int(pos_mm / 0.01)  # un step equivalent a 2mm de mvt, mettre step arrondie
    if pos_mm > 0:
        turn_dir = 1
    else:
        turn_dir = 0

    return step, turn_dir


def do_a_step(pin_to_step):
    stepTime = 5 / float(1000)
    GPIO.output(pin_to_step, GPIO.HIGH)
    time.sleep(stepTime)
    GPIO.output(pin_to_step, GPIO.LOW)
    time.sleep(stepTime)


def set_direction(pin_to_dir, dir):
    dirTime = 3 / float(1000)
    time.sleep(dirTime)
    GPIO.output(pin_to_dir, dir)
    time.sleep(dirTime)


def step_to_motor(motor, step_need, dirtion):
    GPIO.setmode(GPIO.BOARD)  # BCM GPIO reference, go GPIO.BOARD for physical pin

    if motor == 1:  # drive M1
        stepPins = 11
        dirPins = 12
    else:  # drive M2
        stepPins = 32
        dirPins = 33

    print("Setup pins")
    GPIO.setup(stepPins, GPIO.OUT)
    GPIO.output(stepPins, GPIO.LOW)
    GPIO.setup(dirPins, GPIO.OUT)
    GPIO.output(dirPins, GPIO.LOW)

    waitTime = 20 / float(1000)

    counter = 0
    set_direction(dirPins, dirtion)
    while counter < step_need:
        print(counter)
        do_a_step(stepPins)
        counter += 1
        time.sleep(waitTime)

def test_them_motor():
    setup_serial()
    motor_M1_Pin = 11
    motor_M1_dir = 12
    motor_M2_Pin = 32
    motor_M2_dir = 33

    print("Pin setup Test")
    GPIO.setup(motor_M1_Pin,GPIO.OUT)
    GPIO.output(motor_M1_Pin,GPIO.LOW)
    GPIO.setup(motor_M1_dir, GPIO.OUT)
    GPIO.output(motor_M1_dir, GPIO.LOW)
    GPIO.setup(motor_M2_Pin, GPIO.OUT)
    GPIO.output(motor_M2_Pin, GPIO.LOW)
    GPIO.setup(motor_M2_dir, GPIO.OUT)
    GPIO.output(motor_M2_dir, GPIO.LOW)

    count = 0
    while count < 4:
        set_direction(motor_M1_dir, 0)
        m11 = 0
        m10 = 0
        m21 = 0
        m20 = 0
        while m11 < 3:
            do_a_step(motor_M1_Pin)
            m11 += 1
        set_direction(motor_M1_dir, 1)
        while m10 < 3:
            do_a_step(motor_M1_Pin)
            m10 += 1
        set_direction(motor_M2_dir, 0)
        while m21 < 3:
            do_a_step(motor_M1_Pin)
            m21 += 1
        set_direction(motor_M1_dir, 1)
        while m20 < 3:
            do_a_step(motor_M1_Pin)
            m20 += 1
        set_direction(motor_M2_dir, 0)
        print("loop numero:", count)
        count += 1
    print("We done, test Work!!")



