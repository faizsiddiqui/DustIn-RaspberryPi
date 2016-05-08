import threading
from socket import *
import time
import json
#import distance
#import motor

HOST = '192.168.1.34'
PORT = 8080

distance_data = " "
obstacle_detect = " "
location_data = " "

class Threads(object):

    '''def thread_distance():
    	global distance_data
        try:
            distance = Distance()
            while True:
                distance_data = distance.measure()
                print ("Distance : %2.1f cm" % (distance_data))
                time.sleep(0.5)
        except Exception as e:
            raise('Distance thread error!')
        finally:
            del distance

	def thread_obstacle():
		global obstacle_detect
		try:
			obstacle = Obstacle()
			obstacle_detect = obstacle.detect()
		except Exception as e:
			raise('Obstacle thread error!')
		finally:
			del obstacle'''

    def thread_GPS(host, port):
        print(host + ":" + str(port))
        s = socket(AF_INET, SOCK_STREAM)
        s.bind((host, port))
        s.listen(1)
        conn, addr = s.accept() #accept the connection
        print "Connected by: " , addr #print the address of the person connected
        while True:
            data = conn.recv(1024) #how many bytes of data will the server receive
            print "Received: ", repr(data)
            reply = raw_input("Reply: ") #server's reply to the client
            conn.sendall(reply)
        conn.close()

    GPS_thread = threading.Thread(target=thread_GPS, args=(HOST, PORT))
    GPS_thread.start()

    #distance_thread = threading.Thread(target=thread_distance, args=())
    #distance_thread.start()

	#obstacle_thread = threading.Thread(target=thread_obstacle, args=())
    #obstacle_thread.start()

if __name__ == "__main__":
	Threads()
