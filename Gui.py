import Board
import pygame, sys, os
import time
from Game_loop import *

#zmienne globalne
BOARD_COLOR = (255, 195, 77)
PLAYER1_COLOR = (0, 0, 0)
PLAYER2_COLOR = (255, 255, 255)
TABLE_OF_POSITION = []

NUMBER_OF_PAWNS = 5

X_POS = 50 #startowa pozycja X
Y_POS = 50 #startowa pozycja Y
LINE_SIZE = 5 #szerkość przerwy
SIDE_SIZE = 50 #długość boku pola

OLD_XY = [0, 0]

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)

class Gui:

    def __init__(self, board, window):
        #inicjowanie biblioteki pyGame
        #pygame.init()
        #font
        pygame.font.init()  # you have to call this at the start, 
                            # if you want to use this module.
        

        self.run = True
        #inicjowanie zmiennych pomocniczych
        self.If_three = False
        self.If_move = False
        #inijowanie tablicy
        self.board = board
        #self.board.Printing_board()
        # definiowanie okna gry
        #self.win = pygame.display.set_mode((425, 425))
        self.win = window
        self.win.fill((0,0,0))
        # wyświetlanie okna gry
        pygame.display.set_caption("Moja Gra")
        #tworzenie tablicy pozycji
        self.Create_table_of_position()
        #uruchomienie głównej funckcji GUI
        self.Window_while()

    def create_text(self, contents, x, y, color):
        #set font
        font = pygame.font.Font('freesansbold.ttf', 20)
        text = font.render(contents, True, color, black)
        textRect = text.get_rect()
        textRect.center = (x, y)
        self.win.blit(text, textRect)
        #return text, textRect 

    def Window_while(self):
        self.win.fill(black)
        self.Draw_board()
        self.Pawn_draw()
        pygame.display.update()

    def setBoard(self, board, phase, player):
        self.board = board
        self.phase = phase
        self.player = player
        ###
        self.win.fill(black)
        #self.create_text("Ruch:", 450, 70, white)

        print("show get turn: ", self.phase, "turn" , self.player)
        if self.player == 1:
            self.create_text("Tura czarnych", 500, 70, white)
        else:
            self.create_text("Tura białych", 500, 70, white)

        if self.phase == 0:
            self.create_text("Faza stawiania", 500, 100, green)
        elif self.phase == 1:
            self.create_text("Faza ruchu", 500, 100, yellow)
        else:
            self.create_text("Faza zbijania", 500, 100, red)
        ###
        self.Draw_board()
        self.Pawn_draw()
        pygame.display.update()
 

    def Create_table_of_position(self):

        for i in range(0, 6):
            start_pos = X_POS + (i * (SIDE_SIZE + LINE_SIZE))
            end_pos = X_POS + SIDE_SIZE + (i * (SIDE_SIZE + LINE_SIZE))
            TABLE_OF_POSITION.append([start_pos, end_pos])

        #print("TABLE OF POSITION", TABLE_OF_POSITION)

    def Draw_board(self):
        x = X_POS
        y = Y_POS
        # funkcja rysująca kwadrat
        for i in range(0, 6):
            for j in range(0, 6):
                pygame.draw.rect(self.win, BOARD_COLOR, (x, y, SIDE_SIZE, SIDE_SIZE))
                x = x + SIDE_SIZE + LINE_SIZE
            y = y + SIDE_SIZE + LINE_SIZE
            x = X_POS
        # odświeżenie ekranu 
        #pygame.display.update()
    
    def Pawn_draw(self):
        
        radius = SIDE_SIZE / 2
        # funkcja rysująca kwadrat
        for i in range(0, 6):
            for j in range(0, 6):
                x = TABLE_OF_POSITION[j][0]
                y = TABLE_OF_POSITION[i][0]
                if self.board.board[i][j] == 1:
                    pygame.draw.circle(self.win, PLAYER1_COLOR, (x + radius, y + radius), radius)
                elif self.board.board[i][j] == 2:
                    pygame.draw.circle(self.win, PLAYER2_COLOR, (x + radius, y + radius), radius)
                x = x + SIDE_SIZE + LINE_SIZE
            y = y + SIDE_SIZE + LINE_SIZE
            x = X_POS
#Gui()