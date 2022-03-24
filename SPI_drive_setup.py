import spidev
import time


def setup_spi():
    motor_m1 = spidev.SpiDev()
    motor_m2 = spidev.SpiDev()
    motor_m1.open(0, 0)  # verifier, presentement bus 0, device 0
    motor_m2.open(0, 1)
    motor_m1.max_speed_hz = 32000000  # verifier max speed du rasberry
    motor_m2.max_speed_hz = 32000000
    time.sleep(0.1)
    ctrl_default = 0x0C10  # 0b0000110000010000
    torque_default = 0x11FF  # 0b0001000111111111
    off_default = 0x2030  # 0b0010000000110000
    blank_default = 0x3080 #0b0011000010000000
    decay_default = 0x4510 #0b0100010100010000
    stall_default = 0x5040 #0b0101000001000000
    drive_default = 0x6A59 #0b0110101001011001
    status_default = 0x7000 #0b0111000000000000  # write only to clear all temperature fault
    ctrl_enable_32 = 0x0C29 #0b0000110000101001
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
