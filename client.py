import socket


class Client:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.host = socket.gethostname()
        self.port = 5050
        self.addr = (self.host,self.port)

    def connect(self):
        self.client.connect(self.addr)
        
    
    def receive(self):
        reply = self.client.recv(2048)
        reply_decode = reply.decode()
        print("Client_Received:"  + reply_decode)
        return reply_decode
    def send_data(self,data):
        try:
            self.client.send(str.encode(data))
        except socket.error as e:
            print("Connection Problem" + e)



