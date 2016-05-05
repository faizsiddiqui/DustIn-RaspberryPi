'''
@task	: 	4WD Motor Controller
@sensor	:	DC Motors and H-Bridge Motor Driver
'''

import RPi.GPIO as gpio
import time

class Motor:

	PIN_MOTOR_ONE = 31
	PIN_MOTOR_TWO = 33
	PIN_MOTOR_THREE = 35
	PIN_MOTOR_FOUR = 37

	def __init__(self):
		gpio.setwarnings(False)
		gpio.setmode(gpio.BOARD)
		gpio.setup(self.PIN_MOTOR_ONE, gpio.OUT) #motor1
		gpio.setup(self.PIN_MOTOR_TWO, gpio.OUT) #motor2
		gpio.setup(self.PIN_MOTOR_THREE, gpio.OUT) #motor3
		gpio.setup(self.PIN_MOTOR_FOUR, gpio.OUT) #motor4

	def forward(self):
		gpio.output(self.PIN_MOTOR_ONE, False) #motor1
		gpio.output(self.PIN_MOTOR_TWO, True) #motor2
		gpio.output(self.PIN_MOTOR_THREE, True) #motor3
		gpio.output(self.PIN_MOTOR_FOUR, False) #motor4

	def reverese(self):
		gpio.output(self.PIN_MOTOR_ONE, True) #motor1
		gpio.output(self.PIN_MOTOR_TWO, False) #motor2
		gpio.output(self.PIN_MOTOR_THREE, False) #motor3
		gpio.output(self.PIN_MOTOR_FOUR, True) #motor4

	def left(self):
		gpio.output(self.PIN_MOTOR_ONE, True) #motor1
		gpio.output(self.PIN_MOTOR_TWO, True) #motor2
		gpio.output(self.PIN_MOTOR_THREE, True) #motor3
		gpio.output(self.PIN_MOTOR_FOUR, False) #motor4

	def right(self):
		gpio.output(self.PIN_MOTOR_ONE, False) #motor1
		gpio.output(self.PIN_MOTOR_TWO, True) #motor2
		gpio.output(self.PIN_MOTOR_THREE, False) #motor3
		gpio.output(self.PIN_MOTOR_FOUR, False) #motor4

	def stop(self):
		gpio.output(self.PIN_MOTOR_ONE, False) #motor1
		gpio.output(self.PIN_MOTOR_TWO, False) #motor2
		gpio.output(self.PIN_MOTOR_THREE, False) #motor3
		gpio.output(self.PIN_MOTOR_FOUR, False) #motor4

	def __del__(self):
		stop()
		gpio.cleanup()
