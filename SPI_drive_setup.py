import spidev
import time


def do_transaction(device_name, device_numb, data):
    device_name.open(0, device_numb)
    device_name.max_speed_hz = 500000
    device_name.mode = 0
    value = device_name.xfer(data)  # try [data] to force a list
    time.sleep(0.1)
    device_name.close()
    return value


def do_transaction2(device_name2, device_numb2, data2):
    device_name2.open(0, device_numb2)
    value2 = device_name2.xfer2(data2)
    time.sleep(0.1)
    device_name2.close()
    return value2


def do_transaction3(device_name3, device_numb3, data3):
    device_name3.open(0, device_numb3)
    value3 = device_name3.xfer2(data3)
    time.sleep(0.1)
    device_name3.close()
    return value3


def test_spi():
    spi = spidev.SpiDev()
    ctrl_test = [0x0C, 0x10]
    torque_test = [0x11, 0x45]
    off_test = [0x20, 0x30]
    blank_test = [0x30, 0x80]
    decay_test = [0x45, 0x10]
    stall_test = [0x50, 0x40]
    drive_test = [0x6A, 0x59]
    ctrl_enable_32_test = [0x0C, 0x2D]
    time.sleep(0.1)
    print("testing xfer")
    a = do_transaction(spi, 0, ctrl_test)
    a1 = do_transaction(spi, 0, torque_test)
    a2 = do_transaction(spi, 0, off_test)
    a3 = do_transaction(spi, 0, blank_test)
    a4 = do_transaction(spi, 0, decay_test)
    a5 = do_transaction(spi, 0, stall_test)
    a6 = do_transaction(spi, 0, drive_test)
    a7 = do_transaction(spi, 0, ctrl_enable_32_test)
    # print(a)
    print("done testing xfer")
    print("testing xfer2")
    b = do_transaction2(spi, 0, ctrl_test)
    b1 = do_transaction2(spi, 0, torque_test)
    b2 = do_transaction2(spi, 0, off_test)
    b3 = do_transaction2(spi, 0, blank_test)
    b4 = do_transaction2(spi, 0, decay_test)
    b5 = do_transaction2(spi, 0, stall_test)
    b6 = do_transaction2(spi, 0, drive_test)
    b7 = do_transaction2(spi, 0, ctrl_enable_32_test)
    # print(b)
    print("done testing xfer2")
    print("testing xfer3")
    c = do_transaction3(spi, 0, ctrl_test)
    c1 = do_transaction3(spi, 0, torque_test)
    c2 = do_transaction3(spi, 0, off_test)
    c3 = do_transaction3(spi, 0, blank_test)
    c4 = do_transaction3(spi, 0, decay_test)
    c5 = do_transaction3(spi, 0, stall_test)
    c6 = do_transaction3(spi, 0, drive_test)
    c7 = do_transaction3(spi, 0, ctrl_enable_32_test)
    # print(c)
    print("done testing xfer3")
    print("done all test")


def setup_spi():
    motor_m1 = spidev.SpiDev()
    motor_m2 = spidev.SpiDev()
    motor_m1.open(0, 0)  # verifier, presentement bus 0, device 0
    motor_m2.open(0, 1)
    motor_m1.max_speed_hz = 32000000  # verifier max speed du rasberry
    motor_m2.max_speed_hz = 32000000
    time.sleep(0.1)
    ctrl_default = [0x0C, 0x10]  # 0b0000110000010000
    torque_default = [0x11, 0xFF]  # 0b0001000111111111
    off_default = [0x20, 0x30]  # 0b0010000000110000
    blank_default = [0x30, 0x80]  # 0b0011000010000000
    decay_default = [0x45, 0x10]  # 0b0100010100010000
    stall_default = [0x50, 0x40]  # 0b0101000001000000
    drive_default = [0x6A, 0x59]  # 0b0110101001011001
    status_default = [0x70, 0x00]  # 0b0111000000000000  # write only to clear all temperature fault
    ctrl_enable_32 = [0x0C, 0x29]  # 0b0000110000101001
    motor_m1.writebytes(ctrl_default)
    time.sleep(0.1)
    motor_m2.writebytes(ctrl_default)
    time.sleep(0.1)
    motor_m1.writebytes(torque_default)
    time.sleep(0.1)
    motor_m2.writebytes(torque_default)
    time.sleep(0.1)
    motor_m1.writebytes(off_default)
    time.sleep(0.1)
    motor_m2.writebytes(off_default)
    time.sleep(0.1)
    motor_m1.writebytes(blank_default)
    time.sleep(0.1)
    motor_m2.writebytes(blank_default)
    time.sleep(0.1)
    motor_m1.writebytes(decay_default)
    time.sleep(0.1)
    motor_m2.writebytes(decay_default)
    time.sleep(0.1)
    motor_m1.writebytes(stall_default)
    time.sleep(0.1)
    motor_m2.writebytes(stall_default)
    time.sleep(0.1)
    motor_m1.writebytes(drive_default)
    time.sleep(0.1)
    motor_m2.writebytes(drive_default)
    time.sleep(0.1)
    motor_m1.writebytes(ctrl_enable_32)
    time.sleep(0.1)
    motor_m2.writebytes(ctrl_enable_32)
    time.sleep(0.1)
