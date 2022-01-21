import pygame
from cells import *
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

def redraw_window():
    """Draws the parts of the window everyframe"""
    SCREEN.fill((255,255,255)) #Fills the screen with white (so that there is no black border)
    for cell in cells: 
        pygame.draw.rect(SCREEN, cell.color, pygame.Rect(cell.x+1,cell.y+1,cell.distance-1,cell.distance-1))
        #Draws a rect with color of the cell
    make_grid() # Makes the grid
     
def make_grid():
    """Makes a 9x9 grid for the sudoku game"""
    
    distance = (WIDTH//9)+1 #Distance between two lines in x axis
    current_place = distance #Current x of line

    for line in range(1,9):
        if line%3==0:
            pygame.draw.line(SCREEN, (000,000,000), (current_place, 0), (current_place, WIDTH), 3) #Horizontal
            pygame.draw.line(SCREEN, (000,000,000), (0, current_place), (WIDTH, current_place), 3) #Vertical
            current_place+=distance
        else:
            pygame.draw.line(SCREEN, (000,000,000), (current_place, 0), (current_place, HEIGHT)) #Horizontal
            pygame.draw.line(SCREEN, (000,000,000), (0, current_place), (WIDTH, current_place)) #Vertical
            current_place+=distance

def main():
    """The main part of the game"""
    running = True

    while running:
        redraw_window()
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get(): #Event loop
            if event.type==pygame.QUIT: #If clicked on close
                running=False
            if event.type ==pygame.MOUSEBUTTONDOWN:
                for cell in cells:
                    if cell.is_over(pos):
                        cell.color = (255,0,0)
                    else:
                        cell.color = (255,255,255)

        pygame.display.update() #Updates the screen
        pygame.display.flip()
    pygame.quit()
    exit()
main()