from numpy import broadcast
import pygame
from client import Client
import threading

pygame.init()

client = Client()
HEIGHT = 800
WIDTH = 800
WHITE = (46,139,87)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 900
who_won = 0 
turn = True 

board = [[0,0,0],[0,0,0],[0,0,0]]
game_over = False
img_X = pygame.image.load("X.png")
img_X = pygame.transform.scale(img_X,(200,200))
img_O = pygame.image.load("O.png")
img_O = pygame.transform.scale(img_O,(200,200))
font = pygame.font.Font('freesansbold.ttf', 32)
text1 = font.render("X WINS",False,("RED"),(0,0,0))
text2 = font.render("O WINS",False,("RED"),(0,0,0))
text3 = font.render("DRAW",False,("RED"),(0,0,0))
text4 = font.render("NEW GAME",False,("RED"),(0,0,0))

sent_data = ""
received_data= ""

def connection():
    global received_data
    while True:
        received_data = client.receive()
        if received_data == "1":
            print("board changed")
            
            




        


def network_data(data):
    if data == "1":
        board[0][0] = 1

def send_message(x,y,data):
    if x == 0 and y == 0:
        data = "1"
        client.send_data(data)
        print("DATA SENT:" + data)

def display_board():
    margin = 5
    block_size = WIDTH //  3 - margin
    full_width,full_height = margin + block_size,margin + block_size
    for i in range(3):
        for j in range(3):
            pygame.draw.rect(Screen, WHITE,[full_width * j + margin, full_height * i + margin, block_size, block_size])
            if board[i][j] == 1:
                Screen.blit(img_X,(full_width * j + 20, full_height * i + 20 ))
            if board[i][j] == -1:
                Screen.blit(img_O,(full_width * j + 20, full_height * i + 20 )) 



def new_game():
    global board, game_over
    board = [[0,0,0],[0,0,0],[0,0,0]]
    game_over = False
def game_over_screen():
    if who_won == 1:
        Screen.blit(text1,(350,810))
    elif who_won == -1:
        Screen.blit(text2,(350,810))
    else:
        Screen.blit(text3,(350,810))
    Screen.blit(text4,(330,850))


       
def check_win():

    counter = 0
    if sum(board[0]) == 3 or sum(board[1]) == 3 or sum(board[2])  == 3:
        return 1
    if sum(board[0]) == -3 or sum(board[1]) == -3 or sum(board[2] ) == -3:
        return -1
    if board[0][0] + board[1][1] + board[2][2] == 3 or board[0][2] + board[1][1] + board[2][0] == 3:
        return 1
    if board[0][0] + board[1][1] + board[2][2] == -3 or board[0][2] + board[1][1] + board[2][0] == -3:
        return -1
    if board[0][0] + board[1][1] + board[2][2] == -3:
        return 1
    for i in range(3):
        
        if sum(([row[i] for row in board])) == 3:
            return 1
        if sum(([row[i] for row in board])) == -3:
            return -1
        if 0 not in board[i]:
            counter += 1 
    if counter == 3:
        return 0 



if __name__ == "__main__":
    client.connect()
    #t1 = threading.Thread(target=connection).start()
    Screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption("TIC_TAC_TOE")
    Clock = pygame.time.Clock()
    Screen.fill("black")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = list(pygame.mouse.get_pos())
                y = pos[0] // 261
                x = pos[1] // 261
                if event.button == 1:
                   if game_over == False:
                        if turn == True:
                            board[x][y] = 1
                            send_message(x,y,sent_data)
                            
                            turn = False
                            
                            
                        else:
                            board[x][y] = -1
                            turn = True
                        
                        
                   else:
                        mouse = pygame.mouse.get_pos()
                        if 333 <= mouse[0] <= 509 and 850 <= mouse[1] <= 878:
                            new_game()
                if event.button == 3:
                    received_data = client.receive()
        
        network_data(received_data)    
        display_board()
        if check_win() != None:
            game_over_screen()
        pygame.display.update()
        Clock.tick(60)