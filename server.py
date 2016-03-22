#NAME: SUJAY NATARAJAN
#ID:1001086537

from socket import *
from threading import current_thread
import datetime
import threading

class Threading(threading.Thread):
#multithreading
	def __init__(self, connect, address):
		threading.Thread.__init__(self)
		self.connectionSocket = connect
		self.addr = address
	def run(self):
		while True:
			try:
				thread_no = current_thread().getName()
				message = connectionSocket.recv(1024)
				#print message
				if not message:
					break
				print "message: \n", message
				filename = message.split()[1]
				f = open(filename[1:])
				outputdata = f.read() 
				print thread_no
				print "outputdata:", outputdata
				now = datetime.datetime.now()
				
				#Send one HTTP header line into socket
				
				Host_name = gethostname()

				Socket_family = connectionSocket.family

				Socket_type = connectionSocket.type
				peer_name = connectionSocket.getpeername()

				#Protocol = connectionSocket.proto
				header1 = "HTTP/1.1 200 OK"
				header_info = {
					"Content-Length": len(outputdata),
					"Keep-Alive": "timeout=%d,max=%d" %(20,80),
					"Connection": "Keep-Alive",
					"Content-Type": "text/html"
					
				}
				
				header2 = "\r\n".join("%s:%s" % (item, header_info[item]) for item in header_info)
				#print "following_header:", following_header
				connectionSocket.send("%s\r\n%s\r\n\r\n" %(header1,header2))
				#Send the content of the requested file to the client
				for i in range(0, len(outputdata)):
					connectionSocket.send(outputdata[i])
			except IOError:
				#Send response message for file not found
				
				connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n")

if __name__ == '__main__':
	serverSocket = socket(AF_INET, SOCK_STREAM) #Prepare a sever socket
	serverPort = 1234 #defining port number
	serverSocket.bind(('',serverPort)) #socket binding
	serverSocket.listen(5)
	threads=[]
	while True:
		#Establish the connection
		print 'Ready to serve...'
		connectionSocket, addr = serverSocket.accept()
		print "address:\n", addr
		

		#Threading
		client_thread = Threading(connectionSocket,addr)
		client_thread.setDaemon(True)
		client_thread.start()
		threads.append(client_thread)
	serverSocket.close()