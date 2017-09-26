import socket
import select

# Information of our server to connect to
HOST = raw_input("Enter hostname ")
PORT = input("Enter port NUMBER")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

# Client loop
username = raw_input("Please Enter your username ")
while True:
    # Let the user enter some data to send
    data = raw_input("Message>>")
    read, write, error = select.select([],[sock],[],0)
    if len(write)!=0:
        # Send the data to the server
        msg = username+">> "+data
        b = sock.send(msg)

    # The receiving loop
    while True:
        # When receiving, use the timeout of 1 to receive more data
        read, write, error = select.select([sock],[],[],1)

        # If there is data, print it
        if len(read)!=0:
            data = bytes.decode(sock.recv(1024))
            print data
           
        # Exit the loop if no more data
        else:
            break
           
