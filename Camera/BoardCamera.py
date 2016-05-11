import cv2

class BoardCamera:

    def __init__(self, camera=0):
		self.cam = cv2.VideoCapture(camera)
		if self.get_camera().isOpened() == False:
			raise Exception("Camera not accessible")

    def get_frame(self):
        _, frame = self.get_camera().read()
        return frame

    def get_camera(self):
        return self.cam
