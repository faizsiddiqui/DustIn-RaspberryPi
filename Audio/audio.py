from Audio import IPAudio as audio

def main():
	aud = audio.IPAudio('http://192.168.43.1:8080/audio.wav')


'''import pyaudio
import wave
import urllib2

class Audio:

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
				f.write(url.read(1024))
				return bytes


req = urllib2.Request('http://192.168.1.37:8080/audio.wav')
response = urllib2.urlopen(req, timeout=1)
bytes = ""
while True:
	bytes+=response.read(1024)


wf = wave.open(response, 'rb')
p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()), channels=wf.getnchannels(), rate=wf.getframerate(), output=True)

data = wf.readframes(1024)

while data != '':
    stream.write(data)
    data = wf.readframes(1024)

stream.stop_stream()
stream.close()

p.terminate()
'''
