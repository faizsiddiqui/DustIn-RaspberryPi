import cv2
import numpy as np
import base64
import urllib2

class IPAudio:

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
                return bytes
        except urllib2.URLError as err:
            raise Exception("IP Audio Connection failed!")
