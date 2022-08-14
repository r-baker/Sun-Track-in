# patch code until reference data work

import pandas as pd

"""
readpdf() read and print data from excel spreadsheet
INPUT: none
DO: Print list on console
RETURN: none
"""
def readpdf():
    df = pd.read_excel("sun data/SunData.xlsx")
    print(df)


# readpdf()
"""
searchdata(time) take a time of the day and return altitude and azimut of sun
INPUT: time ; INT
DO: search excel spreadsheet
RETURN: azimut, altidue ; FLOAT
"""
def searchdata(time):
    data = pd.read_excel("sun data/SunData.xlsx")
    for i in range(0, 36):
        time_store = data.iloc[i, 0]
        if time == time_store:
            azimut = data.iloc[i, 1]
            altitude = data.iloc[i, 2]
            return azimut, altitude