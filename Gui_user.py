import Board
import pygame, sys, os
import time
from Game_loop import *
import Gui

USER_BOARD = []

def user_move(board, player, phase):
    USER_BOARD = board

    while True: 
        #obsługa zdarzeń
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                field = Mouse_check()
                print(phase)
                USER_BOARD.Printing_board(player)
                if check_move(field, player, phase):
                    if_board = Update_board(field)
                    return if_board
                else:
                    print("not legal user move!")
                    pass
                
        time.sleep(0.01)
    
    #return board
def check_move_putting(field, player, phase):
    if USER_BOARD.board[field[1]][field[0]] == 0:
        return True
    else:
        return False
    #print(board.Get_board())
    #print(board.board)
    #print(board.board[field[1]][field[0]])

def check_move_moving(field, player, phase):
    #if board.board[field[1]][field[0]] == 2:
    #    return True
    #else:
    #    return False
    pass

def check_move_taking_off(field, player, phase):
    #if board.board[field[1]][field[0]] == 1:
    #    return True
    #else:
    #    return False
    pass


def check_move(field, player, phase):
    if_legal_move = False

    if phase == 0:
        if_legal_move = check_move_putting(field, player, phase)
    elif phase == 1:
        if_legal_move = check_move_moving(field, player, phase)
    elif phase == 2:
        if_legal_move = check_move_taking_off(field, player, phase)

    return if_legal_move


def Update_board(field):
    #board.Printing_board(2)
    print("update!", USER_BOARD)
    USER_BOARD.Put_pawn(field[1], field[0], 2)

    #board[field[0]][field[1]] = 2
    

#obsługa zdarzeń myszy
def X_mouse_check(mouse_pos):
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

def Y_mouse_check(mouse_pos):
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

def Mouse_check():
    mouse_pos = pygame.mouse.get_pos()
    #print(mouse_pos[0], " ", mouse_pos[1])
    field_x = X_mouse_check(mouse_pos)
    field_y = Y_mouse_check(mouse_pos)
    field = [field_x, field_y]
    #print(field)
    print(field)
    return field