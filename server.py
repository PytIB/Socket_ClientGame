
import socket
import threading



s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((socket.gethostname(),27015))

s.listen(2)
clients = set()
clients_lock = threading.Lock()

th = []
def client_thread(clientsocket,address):
        with clients_lock:
            clients.add(clientsocket)
        try: 
        #receive and decode
            while True:
                data = clientsocket.recv(2048)
                if not data:
                    print("NO DATA")
                    break
                else:
                    print("Server Received:" + data.decode())
                    #send message
                    with clients_lock:
                        for c in clients:
                            if clientsocket != c and len(clients) != 1:
                                print("not equal")
                                c.sendall(data)
                
            
            
        finally:
            with clients_lock:
                clients.remove(clientsocket)
                print("Connection Closed")
                clientsocket.close()
            
   
print("Server is on and Listening: ")
while True:
    clientsocket, addr = s.accept()
    print("Connected to: ", addr)
    th.append(threading.Thread(target=client_thread,args=(clientsocket,addr)).start())
    

    

