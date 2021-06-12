import Board
import pygame, sys, os
import time
from Game_loop import *
import Gui


class Gui_user:
    def __init__(self, board, player) -> None:
        self.board = board
        self.player = player
        self.start_normal_game = False
        self.middle_fields = ([2,2],[3,2],[3,3],[2,3])

    def user_move(self, board, player, phase):
        self.board = board
        self.player = player
        self.phase = phase
        self.good_move = True
        self.field = None

        self.set_up_start_normal_game()

        print("phase:", phase)
        while self.good_move: 
            #obsługa zdarzeń
            if self.start_normal_game == False:
                self.good_move = self.if_putting_first_four()
            elif self.phase == 0:
                self.good_move = self.if_putting()
            elif self.phase == 1:
                self.good_move = self.if_move()
            elif self.phase == 2:
                self.good_move = self.if_remove()
            else:
                pass
            time.sleep(0.01)
        
        print("user move end!")
        #dodaje możliwosć zliczania pionków użytkownika
        if(self.phase == 0):
            self.board.players[player-1].placed_pawns += 1

        return self.board, self.field[0], self.field[1]

    def search(self, list, platform):
        for i in range(len(list)):
            if list[i] == platform:
                return True
        return False

    def set_up_start_normal_game(self):
        for i in self.middle_fields:
            print(i,": ", self.board.board[i[1]][i[0]])
            if self.board.board[i[1]][i[0]] == 0:
                return 0

        self.start_normal_game = True

    def if_putting_first_four(self):
        #1 one moves
        if_click = True

        while if_click:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    self.field = self.Mouse_check()
                    if_click = False
            time.sleep(0.001)

        if self.search(self.middle_fields, self.field):
            print("prawadoto")
        else:
            print("nieprawdato")
            return 1

        print(self.field[1], ":", self.field[0])
        if self.board.board[self.field[1]][self.field[0]] == 0:
            self.board.board[self.field[1]][self.field[0]] = self.player
            self.start_normal_game = False
            return 0
        else:
            return 1

    def if_putting(self):
        #1 one moves
        if_click = True

        while if_click:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    self.field = self.Mouse_check()
                    if_click = False
            time.sleep(0.001)

        print(self.field[1], ":", self.field[0])
        if self.board.board[self.field[1]][self.field[0]] == 0:
            self.board.board[self.field[1]][self.field[0]] = self.player
            return 0
        else:
            return 1

    def if_move(self):
        #2 moves
        if_click = True

        while if_click:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    self.field = self.Mouse_check()
                    if_click = False
            time.sleep(0.001)
        
        if not self.board.board[self.field[1]][self.field[0]] == self.player:
            return 1

        self.old_field = self.field
        if_click = True

        while if_click:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    self.field = self.Mouse_check()
                    if_click = False
            time.sleep(0.001)

        if self.board.board[self.field[1]][self.field[0]] == 0 and self.if_neighbours():
            self.board.board[self.old_field[1]][self.old_field[0]] = 0
            self.board.board[self.field[1]][self.field[0]] = self.player
            return 0
        else:
            return 1

    def if_remove(self):
        #1 move
        if_click = True

        while if_click:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    self.field = self.Mouse_check()
                    if_click = False
            time.sleep(0.001)

        print(self.field[1], ":", self.field[0])
        if self.board.board[self.field[1]][self.field[0]] == 1:
            self.board.board[self.field[1]][self.field[0]] = 0
            self.board.players[0].pawns_on_board -= 1 #UWAGA PLAYER NA SZYWNO! :/
            self.board.players[0].SubtractPawn()
            return 0
        else:
            return 1

    def if_neighbours(self):

        x_bool = False
        y_bool = False
        #sprawdzenie X
        if self.old_field[0] == self.field[0] - 1 or self.old_field[0] == self.field[0] + 1:
            x_bool = True
            
        #sprawdzenie Y
        if self.old_field[1] == self.field[1] - 1 or self.old_field[1] == self.field[1] + 1:
            y_bool = True
        
        if x_bool and y_bool or not x_bool and not y_bool:
            return False
        else:
            return True

    #obsługa zdarzeń myszy
    def X_mouse_check(self, mouse_pos):
        field_x = 0
        #X
        if mouse_pos[0] >= Gui.TABLE_OF_POSITION[0][0] and mouse_pos[0] <= Gui.TABLE_OF_POSITION[0][1]: #X
            field_x = 0
        elif mouse_pos[0] >= Gui.TABLE_OF_POSITION[1][0] and mouse_pos[0] <= Gui.TABLE_OF_POSITION[1][1]:
            field_x = 1
        elif mouse_pos[0] >= Gui.TABLE_OF_POSITION[2][0] and mouse_pos[0] <= Gui.TABLE_OF_POSITION[2][1]:
            field_x = 2
        elif mouse_pos[0] >= Gui.TABLE_OF_POSITION[3][0] and mouse_pos[0] <= Gui.TABLE_OF_POSITION[3][1]:
            field_x = 3
        elif mouse_pos[0] >= Gui.TABLE_OF_POSITION[4][0] and mouse_pos[0] <= Gui.TABLE_OF_POSITION[4][1]:
            field_x = 4
        elif mouse_pos[0] >= Gui.TABLE_OF_POSITION[5][0] and mouse_pos[0] <= Gui.TABLE_OF_POSITION[5][1]:
            field_x = 5
        return field_x

    def Y_mouse_check(self, mouse_pos):
        field_y = 0
        #Y
        if mouse_pos[1] >= Gui.TABLE_OF_POSITION[0][0] and mouse_pos[1] <= Gui.TABLE_OF_POSITION[0][1]: #Y
            field_y = 0
        elif mouse_pos[1] >= Gui.TABLE_OF_POSITION[1][0] and mouse_pos[1] <= Gui.TABLE_OF_POSITION[1][1]:
            field_y = 1
        elif mouse_pos[1] >= Gui.TABLE_OF_POSITION[2][0] and mouse_pos[1] <= Gui.TABLE_OF_POSITION[2][1]:
            field_y = 2
        elif mouse_pos[1] >= Gui.TABLE_OF_POSITION[3][0] and mouse_pos[1] <= Gui.TABLE_OF_POSITION[3][1]:
            field_y = 3
        elif mouse_pos[1] >= Gui.TABLE_OF_POSITION[4][0] and mouse_pos[1] <= Gui.TABLE_OF_POSITION[4][1]:
            field_y = 4
        elif mouse_pos[1] >= Gui.TABLE_OF_POSITION[5][0] and mouse_pos[1] <= Gui.TABLE_OF_POSITION[5][1]:
            field_y = 5
        return field_y

    def Mouse_check(self):
        mouse_pos = pygame.mouse.get_pos()
        #print(mouse_pos[0], " ", mouse_pos[1])
        field_x = self.X_mouse_check(mouse_pos)
        field_y = self.Y_mouse_check(mouse_pos)
        field = [field_x, field_y]
        #print(field)
        print(field)
        return field