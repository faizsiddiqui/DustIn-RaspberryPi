import cv2
import numpy as np

class ObjectDetection(object):

	def __init__(self):
		self.face = False;

	def detect(self, cascade_classifier, gray_image, image):

		# y camera coordinate of the target point 'P'
		y = 0

		#Detect object in the image
		cascade_obj = cascade_classifier.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=2)

		# Draw a rectangle around the faces
		for (x_pos, y_pos, width, height) in cascade_obj:
			cv2.rectangle(image, (x_pos+5, y_pos+5), (x_pos+width-5, y_pos+height-5), (255, 255, 255), 2)
			y = y_pos + height - 5

			#perform more action inside the detected object
			roi = gray_image[y_pos+10:y_pos + height-10, x_pos+10:x_pos + width-10]

		return y

	def detectMultiScale(elf, cascade_classifier, gray_image, image):
		y = 0
		cascade_obj = cascade_classifier.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=2)
		for (x_pos, y_pos, width, height) in cascade_obj:
			cv2.rectangle(image, (x_pos+5, y_pos+5), (x_pos+width-5, y_pos+height-5), (255, 255, 255), 2)
			y = y_pos + height - 5

			#perform more action inside the detected object
			roi = gray_image[y_pos+10:y_pos + height-10, x_pos+10:x_pos + width-10]

		return cascade_obj
