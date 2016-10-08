import socket
import os

HOST = ""
PORT = 5000


#Opening Stream
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connect to Server
client_socket.connect(("", PORT))

while True:
	print "Type name of file"
	fname = raw_input()
	client_socket.send (fname)
	fp = open (fname, 'r')
	while True:
		line = fp.readline (512)
		if not line:
			break
		client_socket.send(line)
	fp.close
	print "Pulled "
	exit()

