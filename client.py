#NAME:SUJAY NATARAJAN
#ID:1001086537

#from socket import *
import socket
import sys
import time
#inputs to command line argument should be in this order
server_host = sys.argv[1]
server_port = sys.argv[2]
filename = sys.argv[3]

host_port = "%s:%s" %(server_host, server_port)
try:
	client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#creating socket
	client_socket.connect((server_host,int(server_port)))
	header = {
	"first_header" : "GET /%s HTTP/1.1" %(filename),
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
	"Accept-Language": "en-us",
	"Host": host_port,
	"Keep-Alive": "timeout=%d,max=%d" %(20,80), #getting timeout
	
	
	}
	http_header = "\r\n".join("%s:%s" %(item,header[item]) for item in header)
	Hostname = socket.gethostname()	#getting host name
	Socket_Family = client_socket.family #getting socketfamily
	Socket_Type = client_socket.type #getting socket type
	Protocol = client_socket.proto #getting protocol
	#Timeout = client_socket.gettimeout()
	peer_name = client_socket.getpeername() #getting peer name
	start=time.time()#starting time to calculate RTT
	client_socket.send("%s\r\n\r\n Client Details\n Hostname:%s\n Socket_Family:%s\n socket_type:%s\n protocol:%s\n  Peername:%s\n" %(http_header,Hostname,Socket_Family,Socket_Type,Protocol,peer_name)) #client sending details to server

except IOError:
	sys.exit(1)
final=""
response_message=client_socket.recv(1024)
#print response_message
elapsed=(time.time())
rtt=(elapsed-start)# Calculating RTT
print "RTT IS :"
print str(rtt)
details=socket.getaddrinfo(server_host,server_port,socket.AF_INET,      # family
                                   socket.SOCK_STREAM,  # socktype
                                   socket.IPPROTO_TCP )#protocol
print " SERVER_DETAILS:"
print " SOCKET_FAMILY,SOCKET_TYPE,PROTOCOL,CANONICAL_NAME,HOST_IP,PORT"
print details # hostdetails,port,socketfamily,socket type,protocol
print " HOSTNAME is :" + socket.getfqdn(server_host)
print "PEERNAME"
print client_socket.getpeername()
while response_message:
	final += response_message
	response_message = client_socket.recv(1024)	
client_socket.close()

print "final:",final