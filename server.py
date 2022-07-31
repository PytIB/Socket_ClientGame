
import socket
from _thread import *



s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((socket.gethostname(),5050))

s.listen(2)
server_set = set()
client_counter = 1

def client_thread(clientsocket):
    while True:
        try: 
        #receive and decode
            data = clientsocket.recv(2048)
            if not data:
                print("NO DATA")
                break
            data_back = data.decode("utf-8")
            
            print("Server Received:" + data_back)
                #send message
            
            for c in server_set:
                c.sendall(data_back.encode())
                
            
            
        except socket.error as e:
            print("Broken connection")
            print(e)
            break
    print("Connection Closed")
    clientsocket.close()
print("Server is on and Listening: ")
while True:
    clientsocket, addr = s.accept()
    print("Connected to: ", addr)
    server_set.add(clientsocket)
    start_new_thread(client_thread, (clientsocket,))

    

