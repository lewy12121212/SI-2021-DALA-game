import Board
import pygame, sys, os
import time

#zmienne globalne
BOARD_COLOR = (255, 195, 77)
PLAYER1_COLOR = (0, 0, 0)
PLAYER2_COLOR = (25, 102, 255)
TABLE_OF_POSITION = []


X_POS = 50 #startowa pozycja X
Y_POS = 50 #startowa pozycja Y
LINE_SIZE = 5 #szerkość przerwy
SIDE_SIZE = 50 #długość boku pola


class Gui:
    def __init__(self):

        pygame.init()
        # definiowanie okna gry
        self.win = pygame.display.set_mode((425, 425))
        # wyświetlanie okna gry

        pygame.display.set_caption("Moja Gra")
        self.Create_table_of_position()
        self.Window_while(True)

    def Window_while(self, run):
       
        while run: # pętla główna okna gry
            self.Draw_board()
            for event in pygame.event.get(): # obsługa zdarzeń
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.Pawn_set(self.Mouse_check())

             # rysowanie planszy
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
    
    #def Pawn_draw(self):
        

    #stawianie pionków
    def Pawn_set(self, field):
        print("pawn set")
        radius = SIDE_SIZE / 2
        x = TABLE_OF_POSITION[field[0]][0]
        y = TABLE_OF_POSITION[field[1]][0]
        pygame.draw.circle(self.win, PLAYER1_COLOR, (x + radius, y + radius), radius)
        #pygame.display.update()

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
        print(field)
        return field


Gui()