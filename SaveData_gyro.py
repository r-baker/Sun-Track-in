#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''!
  # @file demo_get_sensor_data.py
  # @brief Get the sensor's gyroscope, accelerometer and onboard temperature.
  # @n Hardware conneted table in SPI
  # @n --------------------------------------------------------------
  # @n  Sensor      |             MCU                | raspberry pi |
  # @n --------------------------------------------------------------
  # @n FSY          | connected to the IO pin of MCU |      X       |
  # @n INT          | not connected, floating        |      X       |
  # @n CS           | connected to the IO pin of MCU |    22(BCM)   |
  # @n SDO          | connected to miso of MCU'spi   |  MI/9(BCM)   |
  # @n SDI          | connected to mosi of MCU'spi   |  MO/10(BCM)  |
  # @n SCK          | connected to sck of MCU'spi    |  SCL/11(BCM) |
  # @n GND          | GND                            |      GND     |
  # @n 3V3/VCC      | 3V3/VCC                        |   3V3/VCC    |
  # @n --------------------------------------------------------------
  # @n Hardware conneted table in IIC
  # @n --------------------------------------------------------------
  # @n  Sensor      |              MCU               | raspberry pi |
  # @n --------------------------------------------------------------
  # @n TSET         | not connected, floating        |      X       |
  # @n INT          | not connected, floating        |      X       |
  # @n SDA          | connected to sda of MCU's IIC  |  SDA/2(BCM)  |
  # @n SCL          | connected to scl of MCU's IIC  |  SCL/3(BCM)  |
  # @n GND          | GND                            |      GND     |
  # @n 3V3/VCC      | 3V3/VCC                        |   3V3/VCC    |
  # @n --------------------------------------------------------------
  #
  # @Copyright   Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
  # @license     The MIT License (MIT)
  # @author [Arya](xue.peng@dfrobot.com)
  # @version  V1.0
  # @date  2021-06-04
  # @url from https://github.com/DFRobot/DFRobot_ICG20660L
'''

import sys
import os
import time
import xlsxwriter

workbook = xlsxwriter.Workbook('case3.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write('A1', 'Accel X')
worksheet.write('B1', 'Accel Y')
worksheet.write('C1', 'Accel Z')
worksheet.write('D1', 'Gyro X')
worksheet.write('E1', 'Gyro Y')
worksheet.write('F1', 'Gyro Z')
i = 0

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from DFRobot_ICG20660L import *

'''!
  @brief The constructor of the ICG20660L sensor using IIC communication.
  @param addr:  7-bit IIC address, controlled by SDO pin.
  @n     IIC_ADDR_SDO_H or 0x69:  SDO pull high.(default)
  @n     IIC_ADDR_SDO_L or 0x68:  SDO pull down.
'''
icg = DFRobot_ICG20660L_IIC(addr=DFRobot_ICG20660L_IIC.IIC_ADDR_SDO_H)
'''!
  @brief The constructor of the ICG20660L sensor using SPI communication.
  @param cs:  SPI chip select pin, connected to IO pin of raspberry pi.
'''
# icg = DFRobot_ICG20660L_SPI(cs = 22)

if __name__ == "__main__":
    '''!
    @brief Initialize the sensor. After initialization, all sensors are turned off, and the corresponding configuration needs to be turned on through enableSensor.
    @param mode: Configure to read sensor data from FIFO or register?
    @n     eREG_MODE :   Read sensor data from data register.
    @n     eFIFO_MODE:   Read sensor data from 512 bytes FIFO. 
    @note  Read from FIFO, accelerometer, gyroscope and temperature must all be enabled,
    @n and the internal sampling rate must be configured to be consistent.
    @return status:
    @n      0 : Initialization success.
    @n      -1: Interface initialization failed(IIC or SPI).
    @n      -2: Failed to read the device ID, the ID is not 0x91
  '''
    while icg.begin(icg.eREG_MODE) != 0:
        print("Initialization 6-axis sensor failed.")
        time.sleep(1)
    print("Initialization 6-axis sensor sucess.")
    print("ICG20660L Device ID: %#x" % icg.read_id())
    '''!
    @brief Enable sensor, including Accel of xyz axis, Gyro of xyz, temperature and fifo low power enable bit. 
    @param bit: 8-bit byte data. Each bit represents enabling a function bit, as shown in the following table:
    @n -------------------------------------------------------------------------------------------------------------------
    @n |        bit7      |     bit6     |      bit5   |    bit4     |     bit3    |     bit2   |    bit1    |    bit0    |
    @n -------------------------------------------------------------------------------------------------------------------
    @n |     reserve     |    reserve    |eACCEL_AXIS_X|eACCEL_AXIS_Y|eACCEL_AXIS_Z|eGYRO_AXIS_X|eGYRO_AXIS_Y|eGYRO_AXIS_Z|
    @n |                                 |            eACCEL_AXIS_XYZ              |           eGYRO_AXIS_XYZ             |
    @n |                                 |                                eAXIS_ALL                                       |
    @n -------------------------------------------------------------------------------------------------------------------
    @n   bit0:  Z-axis of gyro and temperature.
    @n   bit1:  Y-axis of gyro and temperature.
    @n   bit2:  X-axis of gyro and temperature.
    @n   bit3:  Z-axis of acceleration.
    @n   bit4:  Z-axis of acceleration.
    @n   bit5:  Z-axis of acceleration.
    @n   bit6:  reserve.
    @n   bit7:  reserve.
    @note Enabling any axis of the gyroscope will automatically enable the on-board temperature sensor.
    @n   eGYRO_AXIS_Z: The bit0 of the bit, enable gyro's z axis and temperature.
    @n   eGYRO_AXIS_Y: The bit1 of the bit, enable gyro's y axis and temperature.
    @n   eGYRO_AXIS_X: The bit2 of the bit, enable gyro's X axis and temperature.
    @n   eACCEL_AXIS_Z: The bit3 of the bit, enable accel's z axis.
    @n   eACCEL_AXIS_Y: The bit4 of the bit, enable Accel's y axis.
    @n   eACCEL_AXIS_X: The bit5 of the bit, enable Accel's X axis.
    @n   eGYRO_AXIS_XYZ or eGYRO_AXIS_X|eGYRO_AXIS_Y|eGYRO_AXIS_Z: The bit0/bit1/bit2 of the bit, enable gyro's xyz axis and temperature.
    @n   eACCEL_AXIS_XYZ or eACCEL_AXIS_X|eACCEL_AXIS_Y|eACCEL_AXIS_Z: The bit3/bit4/bit5 of the bit, enable Accel's xyz axis.
    @n   eAXIS_ALL or eGYRO_AXIS_Z|eGYRO_AXIS_Y|eGYRO_AXIS_X|eACCEL_AXIS_Z|eACCEL_AXIS_Y|eACCEL_AXIS_Z: The bit0/bit1/bit2/bit3/bit4/bit5 of the bit, enable temperature, Accel's and gyro's xyz axis. 
  '''
    icg.enable_sensor(bit=icg.eAXIS_ALL)
    # icg.enable_sensor(bit = icg.eGYRO_AXIS_XYZ | icg.eACCEL_AXIS_XYZ)
    # icg.enable_sensor(bit = icg.eGYRO_AXIS_Z|icg.eGYRO_AXIS_Y|icg.eGYRO_AXIS_X|icg.eACCEL_AXIS_Z|icg.eACCEL_AXIS_Y|icg.eACCEL_AXIS_Z)
    '''!
    @brief Config of gyro's full scale, dlpf bandwidth and internal sample rate. 
    @param scale  The full scale of gyro, unit: dps(Degrees per second).
    @n     eFSR_G_125DPS:  The full scale range is ±125 dps.
    @n     eFSR_G_250DPS:  The full scale range is ±250 dps.
    @n     eFSR_G_500DPS:  The full scale range is ±500 dps.
    @param bd  Set 3-db bandwidth.
    @n     eGYRO_DLPF_8173_32KHZ:  When the signal is equal to or greater than 8173Hz, there will be obvious attenuation, 3-db attenuation, and the internal sampling rate is 32KHz.
    @n     eGYRO_DLPF_3281_32KHZ: When the signal is equal to or greater than 3281Hz, there will be obvious attenuation, 3-db attenuation, and the internal sampling rate is 32KHz.
    @n     eGYRO_DLPF_250_8KHZ:   When the signal is equal to or greater than 250Hz, there will be obvious attenuation, 3-db attenuation, and the internal sampling rate is 8KHz.
    @n     eGYRO_DLPF_176_1KHZ:   When the signal is equal to or greater than 176Hz, there will be obvious attenuation, 3-db attenuation, and the internal sampling rate is 1KHz.
    @n     eGYRO_DLPF_92_1KHZ:    When the signal is equal to or greater than 92Hz, there will be obvious attenuation, 3-db attenuation, and the internal sampling rate is 1KHz.
    @n     eGYRO_DLPF_3281_8KHZ:  When the signal is equal to or greater than 3281Hz, there will be obvious attenuation, 3-db attenuation, and the internal sampling rate is 8KHz.
    @note When the gyroscope and accelerometer are both enabled, if the sensor data is read through the FIFO, 
    @n the internal sampling rate of the gyroscope and accelerometer must be the same.
  '''
    icg.config_gyro(scale=icg.eFSR_G_500DPS, bd=icg.eGYRO_DLPF_176_1KHZ)
    '''!
    @brief Config of accel's full scale, dlpf bandwidth and internal sample rate. 
    @param scale  The full scale of accel, unit: g(1g = 9.80665 m/s²).
    @n     eFSR_A_2G:  The full scale range is ±2g.
    @n     eFSR_A_4G:  The full scale range is ±4g.
    @n     eFSR_A_8G:  The full scale range is ±8g.
    @n     eFSR_A_16G:  The full scale range is ±16g.
    @param bd  Set 3-db bandwidth.
    @n     eACCEL_DLPF_5_1KHZ or 0:    When the signal is less than or equal to 5Hz, there will be obvious attenuation, 3-db attenuation, and the internal sampling rate is 1KHz.
    @n     eACCEL_DLPF_10_1KHZ or 1:   When the signal is less than or equal to 10Hz, there will be obvious attenuation, 3-db attenuation, and the internal sampling rate is 1KHz.
    @n     eACCEL_DLPF_21_1KHZ or 2:   When the signal is less than or equal to 21Hz, there will be obvious attenuation, 3-db attenuation, and the internal sampling rate is 1KHz.
    @n     eACCEL_DLPF_44_1KHZ or 3:   When the signal is less than or equal to 44Hz, there will be obvious attenuation, 3-db attenuation, and the internal sampling rate is 1KHz.
    @n     eACCEL_DLPF_99_1KHZ or 4:   When the signal is less than or equal to 99Hz, there will be obvious attenuation, 3-db attenuation, and the internal sampling rate is 1KHz.
    @n     eACCEL_DLPF_218_1KHZ or 5:  When the signal is less than or equal to 218Hz, there will be obvious attenuation, 3-db attenuation, and the internal sampling rate is 1KHz.     @n Support low power consumption mode
    @n     eACCEL_DLPF_420_1KHZ or 6:  When the signal is less than or equal to 420Hz, there will be obvious attenuation, 3-db attenuation, and the internal sampling rate is 1KHz.     @n Support low power consumption mode
    @n     eACCEL_DLPF_1046_4KHZ or 7: When the signal is less than or equal to 1046Hz, there will be obvious attenuation, 3-db attenuation, and the internal sampling rate is 4KHz.   @n Support low power consumption mode
    @n     eACCEL_DLPF_55_1KHZ or 8:   When the signal is less than or equal to 55Hz, there will be obvious attenuation, 3-db attenuation, and the internal sampling rate is 1KHz.     @n Only support low power consumption mode
    @n     eACCEL_DLPF_110_1KHZ or 9:  When the signal is less than or equal to 110Hz, there will be obvious attenuation, 3-db attenuation, and the internal sampling rate is 1KHz.     @n Only support low power consumption mode
    @note When the gyroscope and accelerometer are both enabled, if the sensor data is read through the FIFO,
    @n the internal sampling rate of the gyroscope and accelerometer must be the same.
    @param odr:  Set the frequency of waking up the chip to take a sample of accel data – the low power accel Output Data Rate.
    @n     eODR_125HZ or 9:    The low power accel Output Data Rate: 125Hz
    @n     eODR_250HZ or 10:   The low power accel Output Data Rate: 250Hz
    @n     eODR_500HZ or 11:   The low power accel Output Data Rate: 500Hz
    @param low_power_flag:  Whether to configure the Acceleration to low power mode.
    @n     True:          Enter low power mode.
    @n     False:         Not configure the Acceleration to low power mode.(default)
  '''
    icg.config_accel(scale=icg.eFSR_A_16G, bd=icg.eACCEL_DLPF_218_1KHZ)
    '''!
    @brief Set sample rate divider. 
    @param div  Sample rate divider, the range is 0~255.
    @n    Sampling rate = internal sampling rate/(div+1)
    @note If the accelerometer configuration is in low power consumption mode, that is, the formal parameter lowPowerFlag of the configAccel function is true, \
    @n the sampling rate must match the output rate of the formal parameter odr of configAccel, as shown in the following table:
    @n ----------------------------------------------------------------------------
    @n |                        config_accel                      | set_sample_div |
    @n ----------------------------------------------------------------------------|
    @n |            bd             |      odr      | lowPowerFlag |      div       |
    @n ----------------------------------------------------------------------------|
    @n |            X              |       X       |    false     |      0~255     |
    @n ----------------------------------------------------------------------------|
    @n |                           |  eODR_125Hz   |    true      |        7       |
    @n |                           |-----------------------------------------------|
    @n |bd of supporting low power |  eODR_250Hz   |    true      |        3       |
    @n |consumption mode           |-----------------------------------------------|
    @n |                           |  eODR_500Hz   |    true      |        1       |
    @n |---------------------------------------------------------------------------|
  '''
    icg.set_sample_div(div=19)

    while i < 50:
        '''
      @brief Get Sensor's accel, gyro and temperature data.
      @return Dictionary format: {'accel':{'x':0, 'y':0, 'z':0}, 'gyro':{'x':0, 'y':0, 'z':0}, 'temp':0.0}
    '''
        sensor = icg.get_sensor_data()
        # print(sensor)
        print("Accel:  x: %.3f g,  y: %.3f g,  z:%.3f g" % (
        sensor['accel']['x'], sensor['accel']['y'], sensor['accel']['z']))
        print("Gyro:  x: %.3f dps,  y: %.3f dps,  z:%.3f dps" % (
        sensor['gyro']['x'], sensor['gyro']['y'], sensor['gyro']['z']))
        print("Temp:   t: %.3f C" % (sensor['temp']))
        print(i)
        print("")
        i = i + 1
        worksheet.write(i, 0, sensor['accel']['x'])
        worksheet.write(i, 1, sensor['accel']['y'])
        worksheet.write(i, 2, sensor['accel']['z'])

        worksheet.write(i, 3, sensor['gyro']['x'])
        worksheet.write(i, 4, sensor['gyro']['y'])
        worksheet.write(i, 5, sensor['gyro']['z'])

        time.sleep(1)

workbook.close()
