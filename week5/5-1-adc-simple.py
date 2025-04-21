import RPi.GPIO as gp
import time
gp.setmode(gp.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
troyka = 13
comp = 14
gp.setup(dac, gp.OUT)
gp.setup(comp, gp.IN)
gp.setup(troyka,gp.OUT,initial=gp.HIGH)

def to_binary(x):
    return [int(i) for i in bin(x)[2:].zfill(8)]

def adc():
    for i in range(256):
        gp.output(dac, to_binary(i))
        time.sleep(0.001)
        if gp.input(comp)==1:
            return i
    return 255

maxv=3.3

try:
    while True:
        n=adc()
        v=n/255*maxv
        print('voltage:',v,'V on number',n)
finally:
    gp.output(dac, 0)
    gp.output(troyka, 0)
    gp.cleanup()