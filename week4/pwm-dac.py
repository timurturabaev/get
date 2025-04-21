import RPi.GPIO as gp
import time
gp.setmode(gp.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
gp.setup(dac, gp.OUT)
gp.setup(20, gp.OUT)
gp.setup(9, gp.OUT)
def to_binary(x):
    return [int(i) for i in bin(x)[2:].zfill(8)]
dc = 0
p = gp.PWM(20,1000)
p.start(0)
r = gp.PWM(9,1000)
r.start(0)

try:
    while True:
        dc=int(input('enter duty cycle:'))
        p.ChangeDutyCycle(dc)
        r.ChangeDutyCycle(dc)
        print('current voltage:',dc/100*3.3,'V')
finally:
    gp.cleanup()