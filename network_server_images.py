import socket
import os

#Establish host
HOST = ""
PORT = 5000


#Opening Stream
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Bind
server_socket.bind(("", PORT))

#Listening for number of clients
server_socket.listen(5)

client_socket, ip_address = server_socket.accept()

print "Now connected to -", ip_address, "\n"

while True:
	data = client_socket.recv (1024)
	print data
	img = open (data, 'w')
	while True:
		string = client_socket.recv(512)
		if not string:
			break
		fp.write (string)
	img.close()
	print ("success")
	exit ()
