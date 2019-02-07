import time
from socket import *

print("Running")

# Create a udp socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)

sequenceNumber = 1
while True:
	message = 'ping'
	start = time.time()
	message = str.encode(message)
	clientSocket.sendto(message, ('10.0.37.251', 12000))
	
	try:
		message, address = clientSocket.recvfrom(1024)
		elapsed = (time.time() - start)
		print(sequenceNumber)
		print(message.decode('utf-8'))
		print(f"round trip time is {round(elapsed, 6)} seconds")
	except timeout:
		print(sequenceNumber)
		print("Request timeout")
	sequenceNumber += 1
	if(sequenceNumber > 10):
		clientSocket.close()
		exit(0)

