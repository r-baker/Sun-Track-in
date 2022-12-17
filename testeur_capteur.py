#!/usr/bin/python3

# import DHT11
# import kp184
import time
import matplotlib.pyplot as plt
import numpy
from pysolar.solar import *
import datetime
from datetime import datetime
from datetime import timezone
import datetime
import Reference_Data
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import scipy
from scipy import signal

latitude = 45.377
longitude = -71.941



def testing_capteur():
    temp, humidity = DHT11.humidy_and_temp_sensor()
    print('temperature est: ', temp)
    print('humidité est: ', humidity)


def test_charge_active():
    charge_active = kp184.Kunkin_KP184()
    time.sleep(0.2)
    wattage = charge_active.get_P_measure()
    amperage = charge_active.get_I_measure()
    time.sleep(0.2)
    print('wattage est : ', wattage)
    print('Courant est : ', amperage)


def test_utc_time():
    current_utc_time = datetime.datetime.utcnow()
    print(current_utc_time)


def test_ecriture():
    mode = "Ajusted position"
    angle_to_search = [0, 45, 90, 135, 180, 225, 270, 315]
    for rayon in range(1, 4):
        for angle in angle_to_search:
            present_mode = mode + " rayon=" + str(rayon) + " angle=" + str(angle)
            print(present_mode)


def get_sun_azimuth_test(date):
    azimuth = get_azimuth(latitude, longitude, date)
    return azimuth


def get_sun_altitude_test(date):
    altitude = get_altitude(latitude, longitude, date)
    return altitude


def test_position_soleil():
    x = np.linspace(0, 144, 144)
    hour = 8
    minute = 0


    data_azi = []
    data_alt = []
    while hour < 20:
        date = datetime.datetime(2022, 1, 15, hour, minute, 1, 130320, tzinfo=datetime.timezone.utc)
        azimut = get_sun_altitude_test(date)
        altitud = get_sun_altitude_test(date)
        print('altitude is: ',get_sun_altitude_test(date),' at hours: ', hour,'and minute:', minute)
        print('date is: ',date)
        data_azi.append(azimut)
        data_alt.append(altitud)
        minute = minute+5
        if minute == 60:
            hour = hour+1
            minute = 0

    # array_azi = numpy.array(data_azi)
    # array_alt = numpy.array(data_alt)
    x1 = x
    y1 = data_azi
    # plotting the line 1 points
    plt.subplot(211)
    plt.scatter(x1, y1, label="azimuth")

    x2 = x
    y2 = data_alt
    # plotting the line 2 points
    plt.subplot(212)
    plt.scatter(x2, y2, label="altitude")

    # naming the x axis
    plt.xlabel('x time of day 8 to 20')
    # naming the y axis
    plt.ylabel('y degree sun position')
    # giving a title to my graph
    plt.title('sun data')

    plt.legend()

    # function to show the plot
    plt.show()

# testing_capteur()
# test_charge_active()
# test_ecriture()
# test_utc_time()
test_position_soleil()

