import RPi.GPIO as gpio
import time

class IR:

	def __init__(self, PIN_IR):
		self.PIN_IR = PIN_IR
		gpio.setwarnings(False)
		gpio.setmode(gpio.BOARD)
		gpio.setup(self.PIN_IR, gpio.IN)
		time.sleep(2)

	def detect():
		try:
			time.sleep(2)
			while True:
				if gpio.input(self.PIN_IR):
					print "Motion Detected!"
				time.sleep(1)
		except KeyboardInterrupt:
           print "Quit"

	def __del__(self):
		gpio.cleanup()
