# patch code until reference data work

import pandas as pd


def readpdf():
    df = pd.read_excel("sun data/SunData.xlsx")
    print(df)

#readpdf()

def searchdata(time):
    data = pd.read_excel("sun data/SunData.xlsx")
    for i in range(0, 36):
        time_store = data.iloc[i, 0]
        if time == time_store:
            azimut = data.iloc[i, 1]
            altitude = data.iloc[i, 2]
            #print(azimut, ' ', altitude)
            return azimut, altitude


az, alt = searchdata(830)
print(az, ' ', alt)
