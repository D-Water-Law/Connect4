import pygame
from connect4 import Board

def genBoard(surface,board):
    rowCount = len(board)
    colCount = len(board[0])
    
    
    
    
    squareSize = 100
    for row in range(rowCount):
        for col in range(colCount):
            pygame.draw.rect(surface,(0,0,255),(col*squareSize,row*squareSize+squareSize,squareSize,squareSize))#############
            pygame.draw.circle(surface,(0,0,0),(col*squareSize+(squareSize/2),row*squareSize+squareSize+(squareSize/2)),40)
        


pygame.init()
win_height = 700
win_width = 600 
DISPLAYSURF = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption('Connect 4')
run = True

myBoard = Board()

genBoard(DISPLAYSURF,myBoard.getBoard())

while run: # main game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    
    activeKey = pygame.key.get_pressed()
    
    if activeKey[pygame.K_ESCAPE]:
        run = False    
    
    
    pygame.display.update()  
    

pygame.quit()
