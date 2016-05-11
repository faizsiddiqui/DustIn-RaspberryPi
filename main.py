import cv2
import numpy as np
import threading
import time

from Camera import IPCamera as camera
from ML import ObjectDetection as od
from SocketServer import SocketServer

#import distance
#import motor

CLIENT_CAMERA = "http://192.168.1.36:8080/video"

CLIENT_PORT = 8080

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
			del obstacle

    distance_thread = threading.Thread(target=thread_distance, args=())
    distance_thread.start()

	obstacle_thread = threading.Thread(target=thread_obstacle, args=())
    obstacle_thread.start()'''

    def thread_GPS():
        sock = SocketServer()
        print(sock.getAddress())
        sock.accept()
        try:
            while True:
                data = sock.recv() #json formatted
                print("Received : {}", data)
                time.sleep(5)
        except KeyboardInterrupt:
            print "Quit!"
        finally:
            sock.close()

    GPS_thread = threading.Thread(target=thread_GPS, args=())
    GPS_thread.start()

if __name__ == "__main__":
	Threads()

        '''obj_detection = od.ObjectDetection()
        face_cascade = cv2.CascadeClassifier('ML/cascade_xml/haarcascade_frontalface_default.xml')

        cam = camera.IPCamera(CLIENT_CAMERA) #cam = Camera()
        while(cv2.waitKey(1)):
            original = cam.get_frame()
            if original is None:
        		print "error: frame not read from webcam\n"
        		os.system("pause")
        		break
            gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
            v_param1 = obj_detection.detect(face_cascade, gray, original)

            cv2.namedWindow("output", cv2.WINDOW_NORMAL)
            cv2.imshow('output',original)
            k = cv2.waitKey(10)
            if k == 27:
                break

        #cam.get_camera().release()
        cv2.destroyAllWindows()'''
