import time
import datetime
import board
import adafruit_dht
import psutil
import xlsxwriter

#workbook = xlsxwriter.Workbook('DHT11_18C_expire.xlsx')
#worksheet = workbook.add_worksheet()
#worksheet.write('A1','DHT11 1 TEMP (C)')
#worksheet.write('B1','DHT11 1 HUM (%)')
#worksheet.write('C1','DHT11 2 TEMP (C)')
#worksheet.write('D1','DHT11 1 HUM (%)')
#worksheet.write('E1','DHT11 3 TEMP (C)')
#worksheet.write('F1','DHT11 1 HUM (%) ')
#worksheet.write('G1','TIME')
def humidy_and_temp_sensor():
    i = 0
    # We first check if a libgpiod process is running. If yes, we kill it!
    for proc in psutil.process_iter():
        if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
            proc.kill()
    sensor1 = adafruit_dht.DHT11(board.D4)
    sensor2 = adafruit_dht.DHT11(board.D17)
    #sensor3 = adafruit_dht.DHT11(board.D27)

    #while True:
    while i<10:
        try:
            temp1 = sensor1.temperature
            humidity1 = sensor1.humidity
            temp2 = sensor2.temperature
            humidity2 = sensor2.humidity
            #temp3 = sensor3.temperature
            #humidity3 = sensor3.humidity

            i = i + 1
            #worksheet.write(i,0,temp1)
            #worksheet.write(i,1,humidity1)

            #worksheet.write(i,2,temp2)
            #worksheet.write(i,3,humidity2)

            #worksheet.write(i,4,temp3)
            #worksheet.write(i,5,humidity3)
            #worksheet.write(i,6,str(datetime.datetime.now()))







            print("1: Temperature: {}*C   Humidity: {}% ".format(temp1, humidity1))
            print("2: Temperature: {}*C   Humidity: {}% ".format(temp2, humidity2))
            #print("3: Temperature: {}*C   Humidity: {}% ".format(temp3, humidity3))
            print(datetime.datetime.now())
        except RuntimeError as error:
            print(error.args[0])
            time.sleep(2.0)
            continue
        except Exception as error:
            sensor.exit()
            raise error
        time.sleep(2.0)
        return temp1, humidity1 #, temp2, humidity2
#workbook.close() 