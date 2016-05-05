import RPi.GPIO as gpio
import time

class Obstacle:

	IR_PIN = 7

	def __init__():
		gpio.setmode(GPIO.BCM)
		gpio.setup(IR_PIN, gpio.IN)
		time.sleep(2)

	def detect():
		try:
			gpio.add_event_detect(PIR_PIN, gpio.RISING, callback=MOTION)
			while 1:
				time.sleep(100)
		except KeyboardInterrupt:
           print “ Quit”
           gpio.cleanup()

	def callback(IR_PIN):
		print “Motion Detected!”
