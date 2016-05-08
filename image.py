'''
@task	: 	Computer Vision
@sensor	:	Camera Module
'''

import cv2
import numpy as np
import base64
import time
import urllib2

class Camera:

    def __init__(self, camera=0):
		self.cam = cv2.VideoCapture(camera)
		if self.get_camera().isOpened() == False:
			raise Exception("Camera not accessible")

    def get_frame(self):
        _, frame = self.get_camera().read()
        return frame

    def get_camera(self):
        return self.cam

class IPCamera:

    def __init__(self, url, user=None, password=None):
        self.url = url
        auth_encoded = base64.encodestring("%s:%s" % (user, password))[:-1]
        self.req = urllib2.Request(self.url)
        self.req.add_header("Authorization", "Basic %s" % auth_encoded)

    def get_frame(self):
        try:
            response = urllib2.urlopen(self.req, timeout=1)
            bytes = ""
            while True:
                bytes+=response.read(1024)
                a = bytes.find("\xff\xd8")
                b = bytes.find("\xff\xd9")
                if a!=-1 and b!=-1:
                    jpg = bytes[a:b+2]
                    bytes= bytes[b+2:]
                    img_array = np.fromstring(jpg, dtype=np.uint8)
                    frame = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    return frame
        except urllib2.URLError as err:
            raise Exception("IP Camera Connection failed!")

def main():
    camera = IPCamera('http://192.168.1.37:8080/video')
    #camera = Camera()
    while(cv2.waitKey(1)):
        original = camera.get_frame()
        if original is None:
    		print "error: frame not read from webcam\n"
    		os.system("pause")
    		break
        gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        frame, threshold = cv2.threshold(blur,70,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

        image, contours, hierarchy = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        drawing = np.zeros(original.shape, np.uint8)

        max_area = 0

        for i in range(len(contours)):
            cnt = contours[i]
            area = cv2.contourArea(cnt)
            if(area>max_area):
                max_area = area
                ci = i

        cnt = contours[ci]
        hull = cv2.convexHull(cnt)
        moments = cv2.moments(cnt)

        if moments['m00']!=0:
            cx = int(moments['m10']/moments['m00']) # cx = M10/M00
            cy = int(moments['m01']/moments['m00']) # cy = M01/M00

        centre = (cx,cy)
        cv2.circle(original, centre, 5, [0,0,255], 2)
        cv2.drawContours(drawing,[cnt],0,(0,255,0),2)
        cv2.drawContours(drawing,[hull],0,(0,0,255),2)

        cnt = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
        hull = cv2.convexHull(cnt,returnPoints = False)

        if(1):
            defects = cv2.convexityDefects(cnt,hull)
            mind=0
            maxd=0
            for i in range(defects.shape[0]):
                s,e,f,d = defects[i,0]
                start = tuple(cnt[s][0])
                end = tuple(cnt[e][0])
                far = tuple(cnt[f][0])
                dist = cv2.pointPolygonTest(cnt,centre,True)
                cv2.line(original,start,end,[0,255,0],2)
                cv2.circle(original,far,5,[0,0,255],-1)

            #print(i)
            i=0

        cv2.namedWindow("output", cv2.WINDOW_NORMAL)
        cv2.imshow('output', drawing)  # show windows

        k = cv2.waitKey(10)
        if k == 27:
            break

    camera.get_camera().release()
    cv2.destroyAllWindows()   # remove windows from memory
    return

    '''camera = cv2.VideoCapture(0)

    if camera.isOpened() == False: # check if VideoCapture object was associated to webcam successfully
    	print "error: capWebcam not accessed successfully\n\n"
    	os.system("pause")
    	return

    while(cv2.waitKey(1) != 27 and camera.isOpened()): # until the Esc key is pressed or webcam connection is lost

    	frame, original = camera.read()

    	if not frame or original is None:  # if frame was not read successfully
    		print "error: frame not read from webcam\n"
    		os.system("pause")
    		break

    	gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
    	blur = cv2.GaussianBlur(gray, (5, 5), 0)
    	frame, threshold = cv2.threshold(blur,70,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

    	image, contours, hierarchy = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    	drawing = np.zeros(original.shape, np.uint8)

    	max_area = 0

    	for i in range(len(contours)):
    		cnt = contours[i]
    		area = cv2.contourArea(cnt)
    		if(area>max_area):
    			max_area = area
    			ci = i

    	cnt = contours[ci]
    	hull = cv2.convexHull(cnt)
    	moments = cv2.moments(cnt)

    	if moments['m00']!=0:
    		cx = int(moments['m10']/moments['m00']) # cx = M10/M00
    		cy = int(moments['m01']/moments['m00']) # cy = M01/M00

    	centre = (cx,cy)
    	cv2.circle(original, centre, 5, [0,0,255], 2)
    	cv2.drawContours(drawing,[cnt],0,(0,255,0),2)
    	cv2.drawContours(drawing,[hull],0,(0,0,255),2)

    	cnt = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
    	hull = cv2.convexHull(cnt,returnPoints = False)

    	if(1):
    		defects = cv2.convexityDefects(cnt,hull)
    		mind=0
    		maxd=0
    		for i in range(defects.shape[0]):
    			s,e,f,d = defects[i,0]
    			start = tuple(cnt[s][0])
    			end = tuple(cnt[e][0])
    			far = tuple(cnt[f][0])
    			dist = cv2.pointPolygonTest(cnt,centre,True)
    			cv2.line(original,start,end,[0,255,0],2)
    			cv2.circle(original,far,5,[0,0,255],-1)

    		#print(i)
    		i=0

    	cv2.namedWindow("output", cv2.WINDOW_NORMAL)
    	cv2.imshow('output', drawing)  # show windows

    	k = cv2.waitKey(10)
    	if k == 27:
    		break

    camera.release()
    cv2.destroyAllWindows()   # remove windows from memory
    return'''

if __name__ == "__main__":
    main()
