#!/usr/bin/python3

import time
import datetime
import board
import adafruit_dht
import psutil

"""
humidy_and_temp_sensor()
INPUT: NONE
DO: get the humidy and temperature
RETURN: humidy and temperature
"""
def humidy_and_temp_sensor():
    i = 0
    # We first check if a libgpiod process is running. If yes, we kill it!
    for proc in psutil.process_iter():
        if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
            proc.kill()
    sensor1 = adafruit_dht.DHT11(board.D4)

    # while True:
    while i < 2:
        try:
            temp1 = sensor1.temperature
            humidity1 = sensor1.humidity

            i = i + 1

            print("1: Temperature: {}*C   Humidity: {}% ".format(temp1, humidity1))


        except RuntimeError as error:
            print(error.args[0])
            time.sleep(2.0)
            continue

        except Exception as error:
            sensor.exit()
            raise error

        time.sleep(2.0)
        return temp1, humidity1  # , temp2, humidity2

