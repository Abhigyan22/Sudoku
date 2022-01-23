import pygame
import pygame_widgets as pw
from pygame_widgets.button import Button
from cells import *
from sudoku import Sudoku
from sys import exit
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox

pygame.init()
#Initializing the module

WIDTH = 500
HEIGHT = 500

SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
#Screen of the game
pygame.display.set_caption("Sudoku") #Sets the title of the window

LOGO = pygame.image.load('IMG/sudokuLogo.png')
pygame.display.set_icon(LOGO) #Set the logo of the game

FONT = pygame.font.Font('FONT/baars.ttf', 50)
#Custom font



def create_board(difficulty):
    puzzle =  Sudoku(3).difficulty(difficulty/10)
    board = puzzle.board
    current_position = 0
    for row in board:
        for num in row:
            cells[current_position].number = num
            if cells[current_position].number:
                cells[current_position].fill_by_user=False
            
            current_position+=1

def redraw_window():
    """Draws the parts of the window every frame"""
    SCREEN.fill((255,255,255)) #Fills the screen with white (so that there is no black border)
    for cell in cells: 
        pygame.draw.rect(SCREEN, cell.color, pygame.Rect(cell.x,cell.y,cell.distance,cell.distance))
        if cell.number: #I.e it isnt a falsy value
            text = FONT.render(str(cell.number), True, (000,000,000))
            SCREEN.blit(text, (cell.x+18, cell.y))
        #Draws a rect with color of the cell
    make_grid() # Makes the grid
     
def make_grid():
    """Makes a 9x9 grid for the sudoku game"""
    
    distance = (WIDTH//9)+1 #Distance between two lines in x axis
    current_place = distance #Current x of line

    for line in range(1,9):
        if line%3==0:
            pygame.draw.line(SCREEN, (000,000,000), (current_place, 0), (current_place, WIDTH), 3) #Horizontal
            pygame.draw.line(SCREEN, (000,000,000), (0, current_place), (HEIGHT, current_place), 3) #Vertical
            current_place+=distance
        else:
            pygame.draw.line(SCREEN, (000,000,000), (current_place, 0), (current_place, WIDTH)) #Horizontal
            pygame.draw.line(SCREEN, (000,000,000), (0, current_place), (HEIGHT, current_place)) #Vertical
            current_place+=distance
    
def start_game():
    global menu
    global game 
    menu = False
    game = True

start_button = Button(SCREEN, 125, 350, 250, 80, text='Start', inactiveColour=(255,255,255), 
hoverColour=(178, 247, 212), onClick=start_game,
font=FONT, textHAlign='centre', textVAlign='centre')
slider = Slider(SCREEN, 100, 170, 300, 30, min=1, max=9, step=1, handleRadius=30)
output = TextBox(SCREEN, 235,300, 0, 0, font=FONT)

output.disable() 

def main():
    """The main function of the game"""
    global menu
    global game 
    menu = True
    game = False
    while menu:
        events=pygame.event.get()
        for event in events: #Event loop
            if event.type==pygame.QUIT: #If clicked on close
                menu=False
        SCREEN.fill((255, 255, 255))
        text=FONT.render('Select Difficulty', True, (0,0,0))
        SCREEN.blit(text, (110,50))
        pw.update(events)
        pygame.draw.rect(SCREEN, (0,0,0), pygame.Rect(125,350, 250, 80), 3)
        pygame.display.update()
        output.setText(slider.getValue())
    create_board(int(slider.getValue()))
    while game:
        redraw_window()
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get(): #Event loop
            if event.type==pygame.QUIT: #If clicked on close
                game=False
            if event.type ==pygame.MOUSEBUTTONDOWN and event.button==1:
                                                        #Left mouse button
                for cell in cells:
                    if cell.is_over(pos):
                        if cell.fill_by_user:
                            cell.color = (87,250,115)
                        else:
                            cell.color = (219, 59, 59)
                    else:
                        cell.color = (255,255,255)

        pygame.display.update() #Updates the screen
        pygame.display.flip()
    pygame.quit()
    exit()


main()
