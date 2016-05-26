import json, socket

class Server:

	HOST = ""
	client = None

	def __init__(self, PORT, BACKLOG):
		self.HOST = socket.gethostbyname(socket.gethostname())
		self.PORT = PORT
		self.BACKLOG = BACKLOG

		#creating socket
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.bind((self.HOST, self.PORT))
		self.socket.listen(self.BACKLOG)

	def accept(self):
		if self.client:
			self.client.close()
		self.client, self.client_addr = self.socket.accept()
		return self

	def send(self, data):
		if not self.client:
			raise Exception('Cannot send data, no client is connected')
		_send(self.client, data)
		return self

	def recv(self):
	    if not self.client:
			raise Exception('Cannot receive data, no client is connected')
	    return _recv(self.client)

	def getAddress(self):
		return "{}:{}".format(self.HOST, self.PORT)

	def close(self):
		if self.client:
			self.client.close()
			self.client = None
		if self.socket:
			self.socket.close()
			self.socket = None

	def __del__(self):
		self.close()

def _send(socket, data):
	try:
		serialized = json.dumps(data)
	except (TypeError, ValueError), e:
		raise Exception('You can only send JSON-serializable data')
	socket.send('%d\n' % len(serialized))
	socket.sendall(serialized)

def _recv(socket):
	length_str = ''
	char = socket.recv(1)
	while char != '\n':
		length_str += char
		char = socket.recv(1)
	total = int(length_str) + 1
	data = socket.recv(total)

	'''view = memoryview(bytearray(length_str))
	next_offset = 0
	while total - next_offset > 0:
		recv_size = socket.recv_into(view[next_offset:], total - next_offset)
		next_offset += recv_size'''

	try:
		deserialized = json.loads(data)
	except (TypeError, ValueError), e:
		raise Exception('Data received was not in JSON format')
	return deserialized

'''
TCP_IP = socket.gethostbyname(socket.gethostname())
TCP_PORT = 8080
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Host Address : {}:{}".format(TCP_IP, TCP_PORT))
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print 'Connection address:', addr
while 1:
	data = conn.recv(BUFFER_SIZE)
	if not data: break
	print "received data:", data
	conn.send(data)
conn.close()'''
