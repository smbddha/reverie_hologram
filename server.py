import socket

HOST = ''
PORT = 9876
ADDR = (HOST,PORT)
BUFSIZE = 4096

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serv.bind(ADDR)
serv.listen(5)

print 'listening ...'

while True:
	conn, addr = serv.accept()
	print 'client connected ... ', addr

	while True:
		data = conn.recv(BUFSIZE)
		print data

	myfile.close()
	print 'finished writing file'
	conn.close()
