import socket
import threading
import os
 
def RetrFile(name, sock):
	while True:
		filename = sock.recv(1024)
    		print filename 
    		if os.path.isfile(filename):
        		sock.send("EXISTS " + str(os.path.getsize(filename)))
        		userResponse = sock.recv(1024)
        		if userResponse[:2] == 'OK':
        			f = open(filename, 'rb')
            			bytesToSend = f.read(1024)
		        	sock.send(bytesToSend)
            			while bytesToSend != "":
                			bytesToSend = f.read(1024)
                			sock.send(bytesToSend)
    		else:
        		sock.send("ERR")
 
    #sock.close()
 
host = '127.0.0.1'
port = 5000
 
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))

s.listen(5)
 
print "Server Started."
while True:
	c, addr = s.accept()
        print "client connected ip:<" + str(addr) + ">"
        t = threading.Thread(target=RetrFile, args=("RetrThread", c))
        t.start()
         
    #s.close()

