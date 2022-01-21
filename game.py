import pygame
from sudoku import Sudoku
from sys import exit
pygame.init()
#Initializing the module

WIDTH = 500
HEIGHT = 500

SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
#Screen of the game
pygame.display.set_caption("Sudoku") #Sets the title of the window

LOGO = pygame.image.load('sudokuLogo.png')
pygame.display.set_icon(LOGO) #Set the logo of the game

def make_grid():
    """Makes a 9x9 grid for the sudoku game"""
    
    distance = (WIDTH//9)+1 #Distance between two lines in x axis
    current_place = distance #Current x of line

    for line in range(1,9):
        if line%3==0:
            pygame.draw.line(SCREEN, (000,000,000), (current_place, 0), (current_place, HEIGHT), 3)
            pygame.draw.line(SCREEN, (000,000,000), (0, current_place), (WIDTH, current_place), 3)
            current_place+=distance
        else:
            pygame.draw.line(SCREEN, (000,000,000), (current_place, 0), (current_place, HEIGHT))
            pygame.draw.line(SCREEN, (000,000,000), (0, current_place), (WIDTH, current_place))
            current_place+=distance

def main():
    running = True

    while running:
        for event in pygame.event.get(): #Event loop
            if event.type==pygame.QUIT: #If clicked on close
                running=False
        SCREEN.fill((255,255,255))
        make_grid()
        pygame.display.update() #Updates the screen
        pygame.display.flip()
    pygame.quit()
    exit()
main()