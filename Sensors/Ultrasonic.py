'''
@task	: 	Obstacle Distance Measurement
@sensor	:	Ultrasonic Sensor (HC SR04)
'''

import RPi.GPIO as gpio
import time

class Ultrasonic:

	def __init__(self, PIN_GPIO_TRIGGER, PIN_GPIO_ECHO):
		self.PIN_GPIO_TRIGGER = PIN_GPIO_TRIGGER
		self.PIN_GPIO_ECHO = PIN_GPIO_ECHO
		gpio.setwarnings(False)
		gpio.setmode(gpio.BOARD)
		gpio.setup(self.PIN_GPIO_TRIGGER,gpio.OUT) #trigger output
		gpio.setup(self.PIN_GPIO_ECHO,gpio.IN) #echo input
		gpio.output(self.PIN_GPIO_TRIGGER, False) #initialize trigger pin to low

	def measure(self):
		gpio.output(self.PIN_GPIO_TRIGGER, True)
		time.sleep(0.00001)
		gpio.output(self.PIN_GPIO_TRIGGER, False)
		start = time.time()
		while gpio.input(self.PIN_GPIO_ECHO)==0:
			start = time.time()
		while gpio.input(self.PIN_GPIO_ECHO)==1:
			stop = time.time()

		return ((stop-start) * 34300)/2

	def __del__(self):
		gpio.cleanup()
