#!/usr/bin/python3

#import DHT11
#import kp184
import time
import datetime


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


# testing_capteur()
# test_charge_active()

test_utc_time()
