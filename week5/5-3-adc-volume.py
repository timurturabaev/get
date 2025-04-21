import RPi.GPIO as gp
import time
gp.setmode(gp.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
troyka = 13
comp = 14
leds = [2, 3, 4, 17, 27, 22, 10, 9]
gp.setup(leds, gp.OUT)
gp.setup(dac, gp.OUT)
gp.setup(comp, gp.IN)
gp.setup(troyka,gp.OUT,initial=gp.HIGH)

def to_binary(x):
    return [int(i) for i in bin(x)[2:].zfill(8)]

def adc():
    s=[0,0,0,0,0,0,0,0]
    n=0
    for i in range(8):
        s[i]=1
        gp.output(dac, s)
        time.sleep(0.001)
        if gp.input(comp)==1:
            s[i]=0
        else:
            n+=2**(7-i)
    return n

maxv=3.3

try:
    while True:
        n=adc()
        l=n/255*8
        m=[]
        for i in range(8):
            if l>=i+1:
                m.append(1)
            else:
                m.append(0)
        m=m[::-1]
        v=n/255*maxv
        print('voltage:',v,'V on number',n)
        gp.output(leds,m)
        
finally:
    gp.output(leds,0)
    gp.output(dac, 0)
    gp.output(troyka, 0)
    gp.cleanup()