import RPi.GPIO as gpio
import time
dac = [8,11,7,1,0,5,12,6]
number = [0,0,0,0,0,1,0,1]
gpio.setmode(gpio.BCM)
gpio.setup(dac,gpio.OUT)
gpio.output(dac,number)
time.sleep(15)
gpio.output(dac,0)
gpio.cleanup()