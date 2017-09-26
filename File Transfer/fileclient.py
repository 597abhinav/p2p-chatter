import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = raw_input("Enter hostname ")
port = input("Enter port no ")
s.connect((host, port))


while True:
	filename = raw_input("Filename? -> ")
	print filename
	if filename != 'q':
		s.send(filename)
		data = s.recv(1024)
        	if data[:6] == 'EXISTS':
		       	filesize = long(data[6:])
        		message = raw_input("File exists, " + str(filesize) +"Bytes, download? [Y/N]? -> ")
			if message == 'Y' or message == 'y':
        			s.send("OK")
        	       		f = open('new_'+filename, 'wb')
		 	        data = s.recv(1024)
        	    	        totalRecv = len(data)
        	       		f.write(data)
		            	while totalRecv < filesize:
        		       		data = s.recv(1024)
       		       			totalRecv += len(data)
		             		f.write(data)
       		        		print "{0:.2f}".format((totalRecv/float(filesize))*100)+ "% Done"
               			print "Download Complete!"
	                	f.close()
			else:
				break

		else:
			print "File Does Not Exist!"

	else:
		break
s.close()
