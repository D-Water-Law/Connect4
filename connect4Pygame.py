import pygame
from connect4 import Board

def genBoard(surface,sLength,sHeight):
    pass
    # board = Board.getBoard()
    # for row in range(len(board)):
    #     for col in row
        


pygame.init()
win_height = 700
win_width = 800 
DISPLAYSURF = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption('Connect 4')

run = True

genBoard(DISPLAYSURF)

while run: # main game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    
    activeKey = pygame.key.get_pressed()
    
    if activeKey[pygame.K_ESCAPE]:
        run = False    
    
    
    pygame.display.update()  
    

pygame.quit()
