from mpsp import FLIGHT, GROUNDTEST
from mpsp.mpsp import MPSP

import pyb

# pyb.LED(1).on()                 # indicate we are waiting for switch press
# pyb.delay(2000)                 # wait for user to maybe press the switch
# switch_value = pyb.Switch()()   # sample the switch at end of delay
# pyb.LED(1).off()                # indicate that we finished waiting for the switch
#
# pyb.LED(4).on()                 # indicate that we are selecting the mode
#
# mode = GROUNDTEST if switch_value else FLIGHT
# pyb.LED(4).on()                 # indicate that we are selecting the mode

mode = FLIGHT
#mode = GROUNDTEST
m = MPSP(mode)
m.init()
m.run()

# from mpsp.drivers.ads1x15 import ADS1115
# i2c=pyb.I2C(1, pyb.I2C.MASTER)
# adc = ADS1115(i2c)
#
# for i in range(2000):
#     print('{:0.3f} {:0.3f} {:0.3f}'.format(adc.read(0),adc.read_voltage(0), adc.read_voltage(1)))
#     pyb.delay(1)
