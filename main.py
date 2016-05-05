import distance
import motor
import time

if __name__ == "__main__":
	try:
		#bootstraping various required objects
		distance = Distance()
		motor = Motor()
		while True:
			print ("Distance : %2.1f cm" % (distance.measure()))
			time.sleep(0.5)
	finally:
		del distance
		del motor
