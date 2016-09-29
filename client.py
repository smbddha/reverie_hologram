import socket

HOST = 'localhost'
PORT = 9876
ADDR = (HOST, PORT)
BUFSIZE = 4096

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

while True:
	
	try:
		bytes = raw_input("Message: ")
		client.send(bytes)
	except KeyboardInterrupt:
		client.close()
		exit()
