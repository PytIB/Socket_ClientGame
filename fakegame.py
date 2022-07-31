import pygame
from client import Client
import threading
pygame.init()




       
SCREEN = pygame.display.set_mode((800,800))
client = Client()



clock = pygame.time.Clock()
data1 = "I'M DATA"

SCREEN.fill((100,25,58))

client.connect()
def connection():
    while True:
        client.receive()
        



t1 = threading.Thread(target=connection).start()
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                
                client.send_data(data1)
                SCREEN.fill((35,45,89))
            if event.button == 3:
                SCREEN.fill((144,58,115))
                
                client.send_data(data1)
    
    pygame.display.update() 
    clock.tick(60)




