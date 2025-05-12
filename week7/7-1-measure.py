import RPi.GPIO as GPIO
import matplotlib.pyplot as plt
import time

def dectobin(value):
    return [int(i) for i in bin(value)[2:].zfill(8)]

def adc():
    k = 0
    for i in range(7, -1, -1):
        k += 2 ** i
        dac_val = dectobin(k)
        GPIO.output(dac, dac_val)
        time.sleep(0.0012)
        cmp = GPIO.input(comp)

        if cmp == GPIO.HIGH:
            k -= 2 ** i
    return k

def num2_dac_leds(value):
    signal = dectobin(value)
    GPIO.output(dac, signal)
    return signal

dac = [8, 11, 7, 1, 0, 5, 12, 6]
leds = [2, 3, 4, 17, 27, 22, 10, 9]
comp = 14
troyka = 13
bits = len(dac)
levels = 2 ** bits
maxV = 3.3

GPIO.setmode(GPIO.BCM)

GPIO.setup(troyka, GPIO.OUT)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)

GPIO.output(troyka, 0)

data_volts = []
data_times = []
data_val   = []

try:

    val = 0
    GPIO.output(troyka, 1)
    start_time = time.time()

    while(val < 207):
        val = adc()
        voltage = val / levels * maxV
        data_volts.append(voltage)


    discharge_start = len(data_volts)

    GPIO.output(troyka, 0)


    while(val > 64):
        val = adc()
        voltage = val / levels * maxV
        data_volts.append(voltage)


    end_time = time.time()


    with open("./settings.txt", "w") as file:
        file.write(str((end_time - start_time) / len(data_volts)))
        file.write(("\n"))
        file.write(str(maxV / 256))

    print("the duration of the experiment:", end_time - start_time, " secs\n", "average sampling step:", len(data_volts) / (end_time - start_time), "\n", "quantization step:", maxV / 256)

finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.output(troyka, GPIO.LOW)
    GPIO.cleanup()


with open("data.txt", "w") as file:
    for i in range(discharge_start):
        print(f"{data_volts[i]}", file=file)
    for i in range(discharge_start, len(data_volts)):
        print(f"{data_volts[i]}", file=file)


plt.plot(data_volts)
plt.show()
