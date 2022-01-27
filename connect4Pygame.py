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
            pygame.draw.circle(surface,BLACK,(col*squareSize+(squareSize/2),row*squareSize+squareSize+(squareSize/2)),40)

def drawTopC(surface,x):
    pygame.draw.circle(surface,RED,(x,50),40)

def switchP(player):
    if player == 1:
        player += 1
    else:
        player -= 1
    
    return player
        
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


while run: # main game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (1,0,0):
                print("right click")
                ## continue from here


    
    
    activeKey = pygame.key.get_pressed()
    if activeKey[pygame.K_ESCAPE]:
        run = False 
    ## put this in event handler section##

    mousex, mousey = pygame.mouse.get_pos()
    drawTopC(DISPLAYSURF,mousex)

    genBoard(DISPLAYSURF,myBoard.getBoard())
    



    
    
    

    
    
    pygame.display.update()  
    DISPLAYSURF.fill(BLACK)

pygame.quit()
