#!/usr/bin/python3


from pysolar.radiation import get_radiation_direct
from pysolar.solar import *
import datetime
from datetime import datetime
from datetime import timezone


latitude = 45.377
longitude = -71.941

"""
get_sun_pos()
INPUT: date, time, position in latitude longitude
DO: get the sun position in the sky
RETURN: azimuth and altitude
"""
def get_sun_pos():
    date_now = datetime.now(timezone.utc)
    minute_now = int(date_now.strftime("%M"))
    print("date now utc:", date_now)
    file = date_now.strftime("%d")+"_"+date_now.strftime("%m")+"_"+date_now.strftime("%Y")+".csv"
    #  print("Nom de fichier: ", file)
    #  print("minute now:", minute_now)
    azimuth = get_azimuth(latitude, longitude, date_now)
    altitude = get_altitude(latitude, longitude, date_now)
    #  print("azimuth: ", azimuth)
    #  print("altitude: ", altitude)
    return azimuth, altitude

"""
get_sun_azimuth()
INPUT: date, time, position in latitude longitude
DO: get the sun azimuth
RETURN: azimuth 
"""
def get_sun_azimuth():
    date_now = datetime.now(timezone.utc)
    azimuth = get_azimuth(latitude, longitude, date_now)
    return azimuth

"""
get_sun_altitude()
INPUT: date, time, position in latitude longitude
DO: get the sun altitude()
RETURN: altitude()
"""
def get_sun_altitude():
    date_now = datetime.now(timezone.utc)
    altitude = get_altitude(latitude, longitude, date_now)
    return altitude

"""
estimated_groud_watt()
INPUT: date, time, position in latitude longitude
DO: estimated_groud_watt()
RETURN: ground wattage 
"""
def estimated_groud_watt():
    date_today = datetime.now(timezone.utc)
    altitude_deg = get_altitude(latitude, longitude, date_today)
    g_watt = get_radiation_direct(date_today, altitude_deg)
    return g_watt
