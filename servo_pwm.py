#!/usr/bin/env python 

__author__ = 'MaYaSeVeN'

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)

hz = 50
degree0 = 0.0005
degree90 = 0.0015
degree180 = 0.0025

degree = [degree0, degree90 , degree0, degree180]

def pwm(a,b):
	for i in range(hz):
		GPIO.output(7,1)
		time.sleep(a)	
		GPIO.output(7,0)
		time.sleep(b)

if __name__ == "__main__":
	while 1:
        	for a in degree:
			b = (1 - (a * hz)) / hz
			print a, b
			pwm(a,b)
