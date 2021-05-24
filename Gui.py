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

class Gui:
    
    
    def __init__(self, board):
        #inicjowanie biblioteki pyGame
        pygame.init()
        self.run = True
        
        #inicjowanie zmiennych pomocniczych
        self.If_three = False
        self.If_move = False
        
        #inijowanie tablicy
        self.board = board
        #self.board.Printing_board()
        # definiowanie okna gry
        self.win = pygame.display.set_mode((425, 425))
        # wyświetlanie okna gry
        pygame.display.set_caption("Moja Gra")
        #tworzenie tablicy pozycji
        self.Create_table_of_position()
        #uruchomienie głównej funckcji GUI
        self.Window_while()

    def Window_while(self):
        
        #pętla główna okna gry
        #while True: 
            self.Draw_board()
            self.Pawn_draw()

            #obsługa zdarzeń
            #for event in pygame.event.get():
            #    if event.type == pygame.QUIT:
            #        self.run = False
            #    elif event.type == pygame.MOUSEBUTTONUP:
            #        self.Click_operation()

            #rysowanie planszy
            pygame.display.update()
            #time.sleep(0.1) # odciążenie procesora

    def setBoard(self, board):
        self.board = board
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