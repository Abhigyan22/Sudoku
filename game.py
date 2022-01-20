import pygame
from sudoku import Sudoku
from sys import exit
pygame.init()
#Initializing the module

WIDTH = 504
HEIGHT = 504

SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
#Screen of the game
IMG = pygame.image.load('grid.png')
#Grid of the game

running = True

while running:
    for event in pygame.event.get(): #Event loop
        if event.type==pygame.QUIT: #If clicked on close
            running=False
    SCREEN.blit(IMG, (0,0))
    pygame.display.update() #Updates the screen
    pygame.display.flip()
pygame.quit()
exit()