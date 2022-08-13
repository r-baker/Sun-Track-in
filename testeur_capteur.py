#!/usr/bin/python3

# import DHT11
# import kp184
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


def test_ecriture():
    mode = "Ajusted position"
    angle_to_search = [0, 45, 90, 135, 180, 225, 270, 315]
    for rayon in range(1, 4):
        for angle in angle_to_search:
            present_mode = mode + " rayon=" + str(rayon) + " angle=" + str(angle)
            print(present_mode)

# testing_capteur()
# test_charge_active()
test_ecriture()
# test_utc_time()
