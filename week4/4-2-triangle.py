import RPi.GPIO as gp
import time
gp.setmode(gp.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
gp.setup(dac, gp.OUT)
def to_binary(x):
    return [int(i) for i in bin(x)[2:].zfill(8)]
try:
    period=int(input('enter period (seconds):'))
    while True:
        t=period/512
        for b in range(256):
            gp.output(dac, to_binary(b))
            print('Предполагаемое текущее напряжение на выходе ЦАП:', '{:.2f}'.format(b/256*3.3),'В')
            time.sleep(t)
        for b in range(256):
            b=255-b
            gp.output(dac, to_binary(b))
            print('Предполагаемое текущее напряжение на выходе ЦАП:', '{:.2f}'.format(b/256*3.3),'В')
            time.sleep(t)
except KeyboardInterrupt:
    print('end')
finally:
    gp.output(dac, 0)
    gp.cleanup()