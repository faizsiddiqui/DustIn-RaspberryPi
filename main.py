# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import cv2
import numpy as np
import threading
import time
import json

from ML import ObjectDetection as od
from Socket.Server import Server
from IOT.REST import REST
from Sensors import *

distance_data = " "
obstacle_detect = " "
location_data = " "

#loading configuration
with open('config.json') as configuration:
    config = json.load(configuration)

rest = REST(config["web-service"]["URL"], config["web-service"]["timeout"])

class Threads:

    def thread_ultrasonic(config):
        if config["sensors"]["ultrasonic"]["status"]:
            global distance_data
            try:
                distance = Ultrasonic(config["sensors"]["ultrasonic"]["PIN_GPIO_TRIGGER"], config["sensors"]["ultrasonic"]["PIN_GPIO_ECHO"])
                while True:
                    distance_data = distance.measure()
                    print ("Distance : %2.1f cm" % (distance_data))
                    time.sleep(0.5)
            except Exception as e:
                raise('Distance thread error!')
        else:
            print("\nUltrasonic Sensor is blocked from the setting.")

    def thread_IR(config, rest):
        if config["sensors"]["IR"]["status"]:
            global obstacle_detect
            try:
                obstacle = IR()
                obstacle_detect = obstacle.detect()
            except Exception as e:
                raise('Obstacle thread error!')
        else:
            print("\nIR Sensor is blocked from the setting.")

    def thread_GPS(config, rest):
        if config["socket"]["status"]:
            global location_data
            server = Server(config["socket"]["PORT"], config["socket"]["BACKLOG"])
            print("\nHost Address : {}".format(server.getAddress()))
            server.accept()
            try:
                print("\nClient {} connected.\n".format(server.client_addr))
                while True:
                    #locaiton data from socket connection
                    location_data = server.recv()
                    if not location_data: break
                    print("Location received from GPS : {}".format(location_data))

                    #posting location_data to the server
                    if config["web-service"]["status"]:
                        response = rest.post(config["web-service"]["API"]["location"], location_data)
                        print("Response from the server : {}\n".format(response["message"]))
                    else:
                        print("Web Service is blocked from the setting.")

            except KeyboardInterrupt:
                print "Quit!"
            finally:
                server.close()
        else:
            print("Socket is blocked from the setting.")

    def thread_ObjectDetection(config):
        obj_detection = od.ObjectDetection()
        face_cascade = cv2.CascadeClassifier('ML/cascade_xml/haarcascade_frontalface_default.xml')
        palm_cascade = cv2.CascadeClassifier('ML/cascade_xml/palm.xml')

        if config["camera"]["status"] == "IP":
            from Camera import IPCamera as camera
            cam = camera.IPCamera(config["camera"]["IP"]["host"] + ":" + str(config["camera"]["IP"]["port"]) + config["camera"]["IP"]["url"])
        else:
            from Camera import BoardCamera as camera
            cam = camera.BoardCamera()
        try:
            while True:
                original = cam.get_frame()
                if original is None:
                    print "error: frame not read from webcam\n"
                    os.system("pause")
                    break
                gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
                v_param1 = obj_detection.detectMultiScale(face_cascade, gray, original)
                v_param2 = obj_detection.detectMultiScale(palm_cascade, gray, original)
                print "Found {0} faces!".format(len(v_param1))
                print "Found {0} palm!".format(len(v_param2))

                cv2.namedWindow("output", cv2.WINDOW_NORMAL)
                cv2.imshow('output',original)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            if config["camera"]["status"] != "IP":
                cam.get_camera().release()

            cv2.destroyAllWindows()
        finally:
            print "Connection closed on Object detection thread."

    '''ultrasonic_thread = threading.Thread(target=thread_ultrasonic(config))
    ultrasonic_thread.start()

    IR_thread = threading.Thread(target=thread_IR(config, rest))
    IR_thread.start()

    GPS_thread = threading.Thread(target = thread_GPS(config, rest))
	GPS_thread.start()'''

    object_detection_thread = threading.Thread(target = thread_ObjectDetection(config))
    object_detection_thread.start()

if __name__ == '__main__':
    Threads()
