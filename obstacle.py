import RPi.GPIO as gpio
import time

class Obstacle:

	PIN_IR = 18

	def __init__():
		gpio.setwarnings(False)
		gpio.setmode(gpio.BOARD)
		gpio.setup(PIN_IR, gpio.IN)
		time.sleep(2)

	def detect():
		try:
			time.sleep(2)
			while True:
				if gpio.input(PIN_IR):
					print "Motion Detected!"
				time.sleep(1)
		except KeyboardInterrupt:
           print "Quit"

	def __del__(self):
		gpio.cleanup()
