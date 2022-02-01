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
    """This functions creates a sudoku game and assigns the numbers to the cells

    Args:
        difficulty (int): The difficulty of the game
    """
    puzzle =  Sudoku(3).difficulty(difficulty/10) #Sudoku puzzle
    board = puzzle.board #puzzle in list version
    current_position = 0
    for row in board:
        for num in row:
            cells[current_position].number = num
            if cells[current_position].number:
                cells[current_position].fill_by_user=False
            
            current_position+=1

def redraw_window():
    """Draws the parts of the window every frame"""
    SCREEN.fill((255,255,255)) #Fills the screen with white 
    for cell in cells: 
        pygame.draw.rect(SCREEN, cell.color, pygame.Rect(cell.x,cell.y,cell.distance,cell.distance))
    if currently_selected:
        for idx,_ in enumerate(box):
            if currently_selected in box[idx]:
                for cell in box[idx]:
                    pygame.draw.rect(SCREEN,(255, 221, 153), pygame.Rect(cell.x,cell.y,cell.distance,cell.distance))
                break

                
        pygame.draw.rect(SCREEN, (255, 221, 153), pygame.Rect(0,currently_selected.y,WIDTH,currently_selected.distance))
        pygame.draw.rect(SCREEN, (255, 221, 153), pygame.Rect(currently_selected.x,0,currently_selected.distance,HEIGHT))
        pygame.draw.rect(SCREEN, currently_selected.color, pygame.Rect(currently_selected.x,currently_selected.y,currently_selected.distance,currently_selected.distance))
    for cell in cells:   
        if cell.number: #I.e it isnt a falsy value
            if cell.fill_by_user:
                text=FONT.render(str(cell.number), True, (57, 111, 237))
                SCREEN.blit(text, (cell.x+18, cell.y))
            else:
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
    """Starts the game when clicked the start button
    """
    global menu
    global game 
    menu = False
    game = True

start_button = Button(SCREEN, 125, 350, 250, 80, text='Start', inactiveColour=(255,255,255), 
hoverColour=(178, 247, 212), onClick=start_game,
font=FONT, textHAlign='centre', textVAlign='centre') #The start button

slider = Slider(SCREEN, 100, 170, 300, 30, min=1, max=9, step=1)
#The slider

output = TextBox(SCREEN, 235,300, 0, 0, font=FONT)
#The output of the slider

output.disable() #Disables typing in the output(TextBox)

currently_selected = None #Currently selected

def main():
    """The main function of the game"""
    global menu
    global game 
    global currently_selected
    menu = True
    game = False

    while menu:
        events=pygame.event.get()
        for event in events: #Event loop
            if event.type==pygame.QUIT: #If clicked on close
                menu=False
        SCREEN.fill((255, 255, 255)) #Fills the screen with white
        text=FONT.render('Select Difficulty', True, (0,0,0)) 
        SCREEN.blit(text, (110,50)) #Renders the text
        pw.update(events) #Update all pygame_widgets 
        pygame.draw.rect(SCREEN, (0,0,0), pygame.Rect(125,350, 250, 80), 3)
        #The border for the start button
        output.setText(slider.getValue()) #The value of the slider = value of TextBox
        pygame.display.update() #Updates the screen
    create_board(int(slider.getValue())) #creates a board with value of the slider as 
    #difficulty
    while game:
        redraw_window() #redraws window
        pos = pygame.mouse.get_pos() #position of mouse
        for event in pygame.event.get(): #Event loop
            if event.type==pygame.QUIT: #If clicked on close
                game=False
            if event.type ==pygame.MOUSEBUTTONDOWN and event.button==1:
                                                        #Left mouse button
                for cell in cells: #each cell in list of all cells
                    if cell.is_over(pos): #If mouse is over a particular cell
                        currently_selected = cell
                        if cell.fill_by_user: #If cell is to be filled by user
                            cell.color = (87,250,115) #Greenish
                        else:
                            cell.color = (219, 59, 59) #Red-ish 
                    else:
                        cell.color = (255,255,255) #white
            if event.type == pygame.KEYDOWN:
                if currently_selected and currently_selected.fill_by_user: #If it is not none
                    if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                        currently_selected.number = 1
                    if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                        currently_selected.number = 2
                    if event.key == pygame.K_3 or event.key == pygame.K_KP3:
                        currently_selected.number = 3
                    if event.key == pygame.K_4 or event.key == pygame.K_KP4:
                        currently_selected.number = 4
                    if event.key == pygame.K_5 or event.key == pygame.K_KP5:
                        currently_selected.number = 5
                    if event.key == pygame.K_6 or event.key == pygame.K_KP6:
                        currently_selected.number = 6                                                                                                
                    if event.key == pygame.K_7 or event.key == pygame.K_KP7:
                        currently_selected.number = 7
                    if event.key == pygame.K_8 or event.key == pygame.K_KP8:
                        currently_selected.number = 8
                    if event.key == pygame.K_9 or event.key == pygame.K_KP9:
                        currently_selected.number = 9                                               
        pygame.display.update() #Updates the screen
        pygame.display.flip()
    pygame.quit() 
    exit()
    #If out of menu or game loop, then quits the game

main()
