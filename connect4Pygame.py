######### Controls #########
# Space = reset
# Right Click = Place disc
# Esc = Close window


import pygame
import math
from connect4 import Board


def genBoard(surface,board):
    rowCount = len(board)
    colCount = len(board[0])
    
    
    
    
    squareSize = 100
    for row in range(rowCount):
        for col in range(colCount):

            pygame.draw.rect(surface,BLUE,(col*squareSize,row*squareSize+squareSize,squareSize,squareSize))

            
            if board[row][col] == "Y":
                color = YELLOW
            elif board[row][col] == "R":
                color = RED
            else:
                color = BLACK
            
            pygame.draw.circle(surface,color,(col*squareSize+(squareSize/2),row*squareSize+squareSize+(squareSize/2)),40)

def drawTopC(surface,x,user):
    if user == 1:
        colour = YELLOW
    else:
        colour = RED

    pygame.draw.circle(surface,colour,(x,50),40)

def switchP(p):
    if p == 1:
        p += 1
    else:
        p -= 1
    
    return p
        
########### Colours ##############

BLUE = (0,0,255)
RED = (255,0,0)
YELLOW = (255,255,0)
WHITE = (255,255,255)
BLACK = (0,0,0)

##################
pygame.init()
win_height = 700
win_width = 600 
DISPLAYSURF = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption('Connect 4')
run = True

myBoard = Board()
player = 1

while run: # main game loop
    mousex, mousey = pygame.mouse.get_pos()
    drawTopC(DISPLAYSURF,mousex,player)    
    
#### Event Handler #######
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            myBoard.showBoard()
            mouseKey = pygame.mouse.get_pressed()
            if mouseKey == (1,0,0):
                print("right click")

                if myBoard.checkTopCol(math.trunc(mousex/100)):
                    last_dc = myBoard.dropD(player, math.trunc(mousex/100))
                    player = switchP(player)

                    if myBoard.checkall(last_dc) == 1:
                        myBoard.resetBoard()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                myBoard.resetBoard()
        
                myBoard.showBoard()
                
                





    genBoard(DISPLAYSURF,myBoard.getBoard())
    



    
    
    

    
    
    pygame.display.update()  
    DISPLAYSURF.fill(BLACK)

pygame.quit()




####### Connect 4 game is now complete Now need to do few tests ########


################# Stuff ###############
    # activeKey = pygame.key.get_pressed()
    # if activeKey[pygame.K_ESCAPE]:
    #     run = False 
    ## put this in event handler section##