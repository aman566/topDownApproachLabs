# Import socket module
from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 1139
# Prepare a server socket

serverSocket.bind(('10.0.37.251', serverPort))
serverSocket.listen(5)
while True:
	# Establish the connection
	print('Ready to serve...')
	connectionSocket, addr = serverSocket.accept()
	print(addr)
	try:
		message = connectionSocket.recv(2048) 
		print(message.decode())
		if(message):
			print(f"{message.split()[0]}:{message.split()[1]}")
			filename = message.split()[1]
			print(f"{filename}||{filename[1:]}")
			f = open(filename[1:])
			outputdata = f.read()
			print(outputdata)
			# Send one HTTP header line into socket
			connectionSocket.send('\nHTTP/1.1 200 OK\n\n'.encode())
			connectionSocket.send(outputdata.encode())
		# Send the content of the requested file to the client
	#	for i in range(0, len(outputdata)):
	#		connectionSocket.send(outputdata[i].encode())
			connectionSocket.close()
	except IOError:
		connectionSocket.send('\nHTTP/1.1 404 Not Found\n\n'.encode())
		connectionSocket.send('\nHTTP/1.1 404 Not Found\n\n'.encode())
