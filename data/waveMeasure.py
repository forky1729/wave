import waveFunctions as b
import time

import RPi.GPIO as GPIO
def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

def abc():
    a_1=0
    for i in range(7, -1, -1):
        a=1
        for j in range(i):
            a = a*2
        a_1=a_1+a
        number = dec2bin(a_1)
        GPIO.output(dac, number)
        time.sleep(0.005)
        if GPIO.input(comp)==0:
            a_1=a_1-a
    return a_1

def u_troyka(value):
        return n

dac = [26,19,13,6,5,11,9,10]
leds=[21,20,16,12,7,8,25,24]
comp = 4
troyka = 17
spisok = []
t = []
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac,GPIO.OUT)
GPIO.setup(leds,GPIO.OUT)
GPIO.setup(troyka,GPIO.OUT)
GPIO.setup(comp,GPIO.IN)

t_z=float(input())

GPIO.setup(2, GPIO.IN)
print('GPIO initialized. Wait for door opening...')
while GPIO.input(2) < 1:
    pass

t0 = time.time()
t=t0
samples =[]
while (t-t0<t_z):
    t = time.time()
    n=abc()
    samples.append(n)
    print(n)
b.save(samples, t0, t)
b.deinitSpiAdc()