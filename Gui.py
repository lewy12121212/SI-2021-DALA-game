import Board
import pygame, sys, os
import time
from Game_loop import *

#zmienne globalne
BOARD_COLOR = (255, 195, 77)
PLAYER1_COLOR = (0, 0, 0)
PLAYER2_COLOR = (255, 255, 255)
TABLE_OF_POSITION = []

X_POS = 50 #startowa pozycja X
Y_POS = 50 #startowa pozycja Y
LINE_SIZE = 5 #szerkość przerwy
SIDE_SIZE = 50 #długość boku pola

OLD_XY = [0, 0]

class Gui:
    def __init__(self, board):
        #inicjowanie biblioteki pyGame
        pygame.init()
        #inicjowanie zmiennych pomocniczych
        self.If_three = False
        self.If_move = False

        #inijowanie tablicy
        self.board = board
        self.board.Printing_board()
        # definiowanie okna gry
        self.win = pygame.display.set_mode((425, 425))
        # wyświetlanie okna gry
        pygame.display.set_caption("Moja Gra")
        #tworzenie tablicy pozycji
        self.Create_table_of_position()
        #uruchomienie głównej funckcji GUI
        self.Window_while(True)

    def Window_while(self, run):
       
        #pętla główna okna gry
        while run: 
            self.Draw_board()
            self.Pawn_draw()

            #obsługa zdarzeń
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.Click_operation()

            #rysowanie planszy
            pygame.display.update()
            time.sleep(0.1) # odciążenie procesora

    def Create_table_of_position(self):

        for i in range(0, 6):
            start_pos = X_POS + (i * (SIDE_SIZE + LINE_SIZE))
            end_pos = X_POS + SIDE_SIZE + (i * (SIDE_SIZE + LINE_SIZE))
            TABLE_OF_POSITION.append([start_pos, end_pos])

        print("TABLE OF POSITION", TABLE_OF_POSITION)

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
        #x = X_POS
        #y = Y_POS

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

    def Click_operation(self):

        #sprwdzenie czy usuwamy pionek
        if self.If_three:
            #pozostawienie tury, graczowi, który utworzył trójkę
            #self.board.Split_turn()
            if self.board.Take_off_pawn(self.Mouse_check()):
                self.If_three = False # zrczucenie przekaźnika IF_THREE
                self.board.Split_turn() 

        elif self.board.Get_players_placed_pawns(1)!=5 or self.board.Get_players_placed_pawns(2)!=5:
            print("putting")
            self.Pawn_set(self.Mouse_check())

        elif self.board.Get_players_pawns_on_board(1)>2 or self.board.Get_players_pawns_on_board(2)>2:
            print("sliding")
            if self.If_move:
                print("if move good")
                if self.board.Move_pawn(OLD_XY[1], OLD_XY[0], self.Mouse_check()[1], self.Mouse_check()[0]):
                    print("if move good tak", self.If_three)

                    self.If_move = False
                    self.If_three = self.board.If_three_pawns(self.Mouse_check()[1], self.Mouse_check()[0])
                    if self.If_three:
                        print("is three")
                        self.board.Split_turn()
                else:
                    self.If_three = False
                    print("if move good nie ")
                                    

            else:
                self.Pawn_move(self.Mouse_check())

        else:
            print("END GAME")

        self.board.Printing_board()
        #elif TYPE_OF_MOVE == 0:
        #    self.Pawn_set(self.Mouse_check())
        #elif TYPE_OF_MOVE == 1:
        #    self.Pawn_remove(self.Mouse_check())
        #elif TYPE_OF_MOVE == 2:
        #    self.Pawn_move(self.Mouse_check())
        #elif TYPE_OF_MOVE == 3:
        #    print("end of GAME")

    #stawianie pionków 0
    def Pawn_set(self, field):
        print("pawn set")
        print(field)
        print("putting")
        if Putting(self.board, field[0], field[1]):
            self.If_three = self.board.If_three_pawns(field[1], field[0])
            if self.If_three:
                self.board.Split_turn()
        else: 
            self.If_three = False
        
        print(self.If_three)
        self.board.Printing_board()

        #self.Pawn_draw()
        #pygame.display.update()
        #self.board.If_three_pawns(field[1], field[0])
        #radius = SIDE_SIZE / 2
        #x = TABLE_OF_POSITION[field[0]][0]
        #y = TABLE_OF_POSITION[field[1]][0]
        #pygame.draw.circle(self.win, PLAYER1_COLOR, (x + radius, y + radius), radius)
        #pygame.display.update()

    #przesuwanie pionków 2
    def Pawn_move(self, field):
        print("pawn set")
        print(field)
        print("sliding")
        if Sliding(self.board, field[0], field[1]):
            OLD_XY[0] = field[0]
            OLD_XY[1] = field[1]
            self.If_move = True
            print(self.If_move)
        else: 
            self.If_move = False
        #if Sliding(self.board, field[0], field[1]):
        #    self.If_three = self.board.If_three_pawns(field[1], field[0])
        #    
        #    if self.If_three:
        #        self.board.Split_turn()
#
        #    self.If_move = True
        #    OLD_XY[0] = field[0]
        #    OLD_XY[1] = field[1]
        #    #self.board.Split_turn()
        #else:
        #    self.If_move = False
        #    self.If_three = False

#       
        #self.board.Printing_board()
        #self.If_three = self.board.If_three_pawns(field[1], field[0])
        #print(self.If_three)

    #obsługa zdarzeń myszy
    def X_mouse_check(self, mouse_pos):
        field_x = 0
        #X
        if mouse_pos[0] >= TABLE_OF_POSITION[0][0] and mouse_pos[0] <= TABLE_OF_POSITION[0][1]: #Y
            field_x = 0
        elif mouse_pos[0] >= TABLE_OF_POSITION[1][0] and mouse_pos[0] <= TABLE_OF_POSITION[1][1]:
            field_x = 1
        elif mouse_pos[0] >= TABLE_OF_POSITION[2][0] and mouse_pos[0] <= TABLE_OF_POSITION[2][1]:
            field_x = 2
        elif mouse_pos[0] >= TABLE_OF_POSITION[3][0] and mouse_pos[0] <= TABLE_OF_POSITION[3][1]:
            field_x = 3
        elif mouse_pos[0] >= TABLE_OF_POSITION[4][0] and mouse_pos[0] <= TABLE_OF_POSITION[4][1]:
            field_x = 4
        elif mouse_pos[0] >= TABLE_OF_POSITION[5][0] and mouse_pos[0] <= TABLE_OF_POSITION[5][1]:
            field_x = 5

        return field_x

    def Y_mouse_check(self, mouse_pos):
        field_y = 0
        #Y
        if mouse_pos[1] >= TABLE_OF_POSITION[0][0] and mouse_pos[1] <= TABLE_OF_POSITION[0][1]: #Y
            field_y = 0
        elif mouse_pos[1] >= TABLE_OF_POSITION[1][0] and mouse_pos[1] <= TABLE_OF_POSITION[1][1]:
            field_y = 1
        elif mouse_pos[1] >= TABLE_OF_POSITION[2][0] and mouse_pos[1] <= TABLE_OF_POSITION[2][1]:
            field_y = 2
        elif mouse_pos[1] >= TABLE_OF_POSITION[3][0] and mouse_pos[1] <= TABLE_OF_POSITION[3][1]:
            field_y = 3
        elif mouse_pos[1] >= TABLE_OF_POSITION[4][0] and mouse_pos[1] <= TABLE_OF_POSITION[4][1]:
            field_y = 4
        elif mouse_pos[1] >= TABLE_OF_POSITION[5][0] and mouse_pos[1] <= TABLE_OF_POSITION[5][1]:
            field_y = 5

        return field_y

    def Mouse_check(self):

        mouse_pos = pygame.mouse.get_pos()
        #print(mouse_pos[0], " ", mouse_pos[1])
        field_x = self.X_mouse_check(mouse_pos)
        field_y = self.Y_mouse_check(mouse_pos)
        field = [field_x, field_y]
        #print(field)
        return field


#Gui()