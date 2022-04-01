import serial
from ticlib import TicSerial
from ticlib import TicUSB
# from src.ticlib import TicSerial
import time


def setup_usb():
    #port = serial.Serial("/dev/ttyS0", 115200, timeout=0.1, write_timeout=0.1)
    #  port1 = serial.Serial()
    # tic = TicSerial(port)
    tic = TicUSB(product="TIC_36v4")  # , serial_number=
    tic.reset()
    tic.clear_driver_error()
    tic.set_decay_mode(0)  # TicDecayMode auto_mixed
    tic.set_current_limit(1000)  # en mA
    # step mode: 0 = full, 1 = 1/2, 2 = 1/4, 3 = 1/8, 4 = 1/16, 5 = 1/32, 7 = 1/64, 8 = 1/128, 9 = 1/256
    # WARNING setting 6 is not in use on the 36V4
    tic.set_step_mode(5)  # 5= 1/32
    tic.energize()
