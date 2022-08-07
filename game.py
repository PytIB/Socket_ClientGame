
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

#turn = True 

board = [[0,0,0],[0,0,0],[0,0,0]]
game_over = False
img_X = pygame.image.load("X.png")
img_X = pygame.transform.scale(img_X,(200,200))
img_O = pygame.image.load("O.png")
img_O = pygame.transform.scale(img_O,(200,200))
img_grayX = pygame.image.load("grayX.png")
img_grayX = pygame.transform.scale(img_grayX,(200,200))
img_grayO = pygame.image.load("grayO.png")
img_grayO = pygame.transform.scale(img_grayO,(200,200))
font = pygame.font.Font('freesansbold.ttf', 32)
text1 = font.render("X WINS",False,("RED"),(43,49,89))
text2 = font.render("O WINS",False,("RED"),(43,49,89))
text3 = font.render("DRAW",False,("RED"),(43,49,89))
text4 = font.render("NEW GAME",False,("BLACK"),(43,49,89))
text5 = font.render("CHOOSE YOUR SIDE",False,("Black"),(43,49,89))
text6 = font.render("WAITING YOUR OPPONENT TO JOIN ...",False,("Black"),(43,49,89))
text7 = font.render("WAITING OPPONENT ...",False,("Black"),(43,49,89))
Newtork_choice = True

move_made = False

new_game_player = False
new_game_opponent = False

X_player = False
O_player = False

X_Opponent = False
O_Opponent = False

choice_X = False
choice_Y = False

sent_data = ""
received_data= ""

def connection():
    global received_data,move_made
    while True:
        received_data = client.receive()
        move_made = False




        


def network_data(data):
    global X_Opponent,O_Opponent, move_made,new_game_opponent
    if data == "NEW GAME":
        new_game_opponent = True
    if data == "X":
        X_Opponent = True
    if data == "O":
        O_Opponent = True
    if X_player == True:
        if data == "1" and board[0][0] == 0:
            board[0][0] = -1
            
        if data == "2" and board[0][1] == 0:
            board[0][1] = -1
            
        if data == "3" and board[0][2] == 0:
            board[0][2] = -1
            
        if data == "4" and board[1][0] == 0:
            board[1][0] = -1
            
        if data == "5"and board[1][1] == 0:
            board[1][1] = -1
            
        if data == "6" and board[1][2] == 0:
            board[1][2] = -1
            
        if data == "7" and board[2][0] == 0:
            board[2][0] = -1
            
        if data == "8" and board[2][1] == 0:
            board[2][1] = -1
            
        if data == "9" and board[2][2] == 0:
            board[2][2] = -1
            
    if O_player == True:
        if data == "1" and board[0][0] == 0:
            board[0][0] = 1
            
        if data == "2" and board[0][1] == 0:
            board[0][1] = 1
            
        if data == "3" and board[0][2] == 0:
            board[0][2] = 1
            
        if data == "4" and board[1][0] == 0:
            board[1][0] = 1
            
        if data == "5" and board[1][1] == 0:
            board[1][1] = 1
            
        if data == "6" and board[1][2] == 0:
            board[1][2] = 1
            
        if data == "7" and board[2][0] == 0:
            board[2][0] = 1
            
        if data == "8" and board[2][1] == 0:
            board[2][1] = 1
            
        if data == "9" and board[2][2] == 0:
            board[2][2] = 1
            
    
    
def send_message(x,y,data):
    if x == 100 and y == 100:
        data = "NEW GAME"
        client.send_data(data)
        print("DATA SENT:" + data)
    if x == -1 and y == -1:
        data = "O"
        client.send_data(data)
        print("DATA SENT:" + data)
    if x == -2 and y == -2:
        data = "X"
        client.send_data(data)
        print("DATA SENT:" + data)
    if x == 0 and y == 0:
        data = "1"
        client.send_data(data)
        print("DATA SENT:" + data)
    if x == 0 and y == 1:
        data = "2"
        client.send_data(data)
        print("DATA SENT:" + data)
    if x == 0 and y == 2:
        data = "3"
        client.send_data(data)
        print("DATA SENT:" + data)
    if x == 1 and y == 0:
        data = "4"
        client.send_data(data)
        print("DATA SENT:" + data)
    if x == 1 and y == 1:
        data = "5"
        client.send_data(data)
        print("DATA SENT:" + data)
    if x == 1 and y == 2:
        data = "6"
        client.send_data(data)
        print("DATA SENT:" + data)
    if x == 2 and y == 0:
        data = "7"
        client.send_data(data)
        print("DATA SENT:" + data)
    if x == 2 and y == 1:
        data = "8"
        client.send_data(data)
        print("DATA SENT:" + data)
    if x == 2 and y == 2:
        data = "9"
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
    global board, game_over,new_game_opponent,new_game_player,Newtork_choice,X_Opponent,O_Opponent,X_player,O_player,choice_X,choice_Y,move_made
    board = [[0,0,0],[0,0,0],[0,0,0]]
    game_over = False
    new_game_player = False
    new_game_opponent = False
    X_Opponent = False
    O_Opponent = False
    X_player = False
    O_player = False
    choice_Y =False
    choice_X = False
    move_made = False
    Newtork_choice = True
    
    



def game_over_screen():
    if check_win() == 1:
        Screen.blit(text1,(350,810))
    elif check_win() == -1:
        Screen.blit(text2,(350,810))
    else:
        Screen.blit(text3,(350,810))
    if new_game_player == False:
        Screen.blit(text4,(330,850))
    else:
        Screen.blit(text7,(200,850))


       
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

def Game_screen():
    if Newtork_choice == True:
        Screen.fill((43,49,89))
        
        
        if choice_X == False and choice_Y == False and X_Opponent == False and O_Opponent == False:
            Screen.blit(text5,(250,200))
            Screen.blit(img_grayX,(150,300))
            Screen.blit(img_O,(500,300))
        else:
            if choice_X == True or X_Opponent == True:
                if X_Opponent == True:
                    Screen.blit(text5,(250,200))
                    Screen.blit(img_X,(150,300))
                    Screen.blit(img_O,(500,300))
                else:
                    Screen.blit(text6,(100,200))
                    Screen.blit(img_X,(150,300))
                    Screen.blit(img_O,(500,300))
            if choice_Y == True or O_Opponent == True:
                if O_Opponent == True:
                    Screen.blit(text5,(250,200))
                    Screen.blit(img_grayO,(500,300))
                    Screen.blit(img_grayX,(150,300))
                else:
                    Screen.blit(text6,(100,200))
                    Screen.blit(img_grayO,(500,300))
                    Screen.blit(img_grayX,(150,300))
    else:   
        display_board()


client.connect()
t1 = threading.Thread(target=connection).start()
if __name__ == "__main__":
   
    
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
                   if Newtork_choice == True:
                      if 170 <= mouse[0] <= 335 and  316 <= mouse[1] <= 480 and X_Opponent == False:
                        if X_player == False and O_player == False:
                            choice_X = True
                            # user chose X 
                            send_message(-2,-2,sent_data)
                            X_player = True
                      if 509 <= mouse[0] <= 695 and  308 <= mouse[1] <= 478 and O_Opponent == False:
                        #checking if user made a choice already 
                        if X_player == False and O_player == False:
                            choice_Y = True
                            #user chose O 
                            send_message(-1,-1,sent_data)
                            O_player = True
                   if game_over == False and Newtork_choice == False:
                        if X_player == True and move_made == False:
                            if board[x][y] == 0:
                                board[x][y] = 1
                                send_message(x,y,sent_data)
                                move_made = True
                            
                            
                            
                            
                        if O_player == True and move_made == False:
                            if board[x][y] == 0:
                                board[x][y] = -1
                                send_message(x,y,sent_data)
                                move_made = True
                        
                        
                   else:
                        if 333 <= mouse[0] <= 509 and 850 <= mouse[1] <= 878:
                            new_game_player = True
                            send_message(100,100,sent_data)
                           
        Game_screen()
        network_data(received_data)
        if X_Opponent == True and O_player == True or X_player == True and O_Opponent == True:
            Newtork_choice = False 
        mouse = pygame.mouse.get_pos()
        if check_win() != None:
            game_over_screen()
            game_over = True
        if new_game_player and new_game_opponent == True:
            new_game()
        pygame.display.update()
        Clock.tick(60)