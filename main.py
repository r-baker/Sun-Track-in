#!/usr/bin/python3

import Mode
import datetime
from datetime import datetime
from datetime import timezone
import Timed_Position
import Motor_Control
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

motor_x_drive_serial_num = "00383845"  # x axis
motor_y_drive_serial_num = "00383851"  # y axis


def main():
    Mode.mode_selection()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/