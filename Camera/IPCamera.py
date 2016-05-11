import cv2
import numpy as np
import base64
import urllib2

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
