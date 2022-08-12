#!/usr/bin/python3

import DHT11
import kp184


def testing_capteur():
    temp, humidity = DHT11.humidy_and_temp_sensor()
    print('temperature est: ', temp)
    print('humidité est: ', humidity)


testing_capteur()
