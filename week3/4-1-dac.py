import RPi.GPIO as gp
gp.setmode(gp.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
gp.setup(dac, gp.OUT)
def to_binary(x):
    return [int(i) for i in bin(x)[2:].zfill(8)]
try:
    a=0
    while True:
        try:
            a=input('Введите число от 0 до 255:')
            if a=='q':
                break
            if float(a)-round(float(a))!=0:
                a=float(a)/0
            b=int(a)
            c=0
            if b<0:
                c=1
                b=256
            gp.output(dac, to_binary(b))
            print('Предполагаемое текущее напряжение на выходе ЦАП:', '{:.2f}'.format(b/256*3.3),'В')
        except ValueError:
            print('its not a number')
        except RuntimeError:
            if c==0:
                print('number bigger than 255')
            else:
                print('number smaller than 0')
        except ArithmeticError:
            print('number is not integer')
finally:
    gp.output(dac, 0)
    gp.cleanup()