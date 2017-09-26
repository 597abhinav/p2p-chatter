import socket 
import select

# Use these for binding our server
HOST = "127.0.0.1"
PORT = 7232

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server.bind((HOST, PORT))

server.listen(5)

clients = []

print("Host = 127.0.0.1\nPort = 7232\n")
# Create a list of clients to use on select
def getClients():
    to_use = []
    for client in clients:
        to_use.append(client[0])
    return to_use
        

# Server loop
while True:
    # Check for connection but not block
    read, write, error = select.select([server],[],[],0)


    # Check if any connections
    if len(read)!=0:
        client, address = server.accept()
        clients.append([client, address, []])

    to_use = getClients()

    # Try and read any data from the clients
    try:
        read, write,error = select.select(to_use,[],[],0)
        if len(read)!=0:
            for client in read:
                # Get the data from the client
                data = client.recv(4096)
                
                # Print the data so the server gets to see it
                print data
                if data == 0:
                    for c in clients:
                        if c[0] == client:
                            clients.remove(c)
                            break
                else:
                    # Add the data to every client's queue
                    for c in clients:
                        c[2].append(data)

    except:
        pass

    # Try and write data from the clients queue to the client
    try:
        to_use = getClients()
        read, write, error = select.select([], to_use, [], 0)

        if(len(write)):
            for client in write:
                for c in clients:
                    if c[0] == client:
                        # Send the data from the client quoue to the client
                        for data in c[2]:
                            sent = client.send(data)
                            if sent == len(data):
                               c[2].remove(data)
                        break
    except:
        pass

