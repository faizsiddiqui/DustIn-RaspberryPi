import json, socket

class SocketServer:

	HOST = ""
	PORT = 8080
	BACKLOG = 5
	client = None

	def __init__(self):
		self.HOST = socket.gethostname()
		self.socket = socket.socket()
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
	total = int(length_str)
	view = memoryview(bytearray(total))
	next_offset = 0
	while total - next_offset > 0:
		recv_size = socket.recv_into(view[next_offset:], total - next_offset)
		next_offset += recv_size
	try:
		deserialized = json.loads(view.tobytes())
	except (TypeError, ValueError), e:
		raise Exception('Data received was not in JSON format')
	return deserialized

'''sock = socket.socket() # Create a socket object
host = socket.gethostname() # Get local machine name
port = 8080  # Reserve a port for your service.
print("{}:{}".format(host, port))
sock.bind((host, port)) # Bind to the port
sock.listen(1) # Now wait for client connection.
connection, client_address  = sock.accept()     # Establish connection with client.
try:
	print("Connected by: {}".format(client_address)) #print the address of the person connected
	while True:
		data = connection.recv(1024) #how many bytes of data will the server receive
		if len(data) > 0:
			print "Received: ", repr(data)
		time.sleep(5)
except KeyboardInterrupt:
   print "Quit!"
finally:
	connection.close() # Close the connection'''
