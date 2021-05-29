import copy
import random

class State:
    empty_moves = 0
    def __init__(self, board, whose_move, game_phase, c_move=None):
        self.board = board
        self.whose_move = whose_move 
        self.game_phase = game_phase #0 - stawianie, 1 - ruch, 2 - zbijanko
        self.current_move = c_move
        self.empty_moves = 0
        self.start = 0

    #dodatkowe metody statusu gry
    def get_game_phase(self):
        pass

    ##################################
    #zwracanie listy dostępnych ruchów
    #0: {[2,2],[3,2]}
    #1: {[2,2],[3,2]}
    def putting_board_iterator(self):
        table_of_legal_action = []
        if self.start == 0:
            for i in self.board.init_board:
                if self.board.board[i[0]][i[1]] == 0:
                    table_of_legal_action.append(i)
            if not table_of_legal_action:
                self.start = 1
        if self.start == 1:
            for i in range(6):
                for j in range(6):
                    if self.board.board[i][j] == 0:
                        table_of_legal_action.append([i, j])
        if not table_of_legal_action:
            print('x0')
        return table_of_legal_action

    def moving_board_iterator(self):
        table_of_legal_action = []
        for i in range(6):
            for j in range(6):
                if self.board.board[i][j] == self.whose_move:
                    table_of_legal_action += self.board.Get_legal_moves(i, j)
        
        if not table_of_legal_action:
            print('x1')
            self.empty_moves = 1
        return table_of_legal_action

    def taking_off_board_iterator(self):
        table_of_legal_action = []
        if self.whose_move == 1:
            x = 2
        else:
            x = 1

        for i in range(6):
            for j in range(6):
                if self.board.board[i][j] == x:
                    table_of_legal_action.append([i, j])

        if not table_of_legal_action:
            print('x2')
        return table_of_legal_action

    def get_legal_actions(self): 

        if self.game_phase == 0:
            table_of_legal_action = self.putting_board_iterator()
            if not table_of_legal_action:
                print('x0')
            return table_of_legal_action
        elif self.game_phase == 1:
            table_of_legal_action = self.moving_board_iterator()
            if not table_of_legal_action:
                print('x1')
            return table_of_legal_action
        elif self.game_phase == 2:
            table_of_legal_action = self.taking_off_board_iterator()
            if not table_of_legal_action:
                print('x2')
            return table_of_legal_action

        

    @property
    def game_result(self):
        # check if game is over
        status = self.board.end()
        if(self.whose_move == 1):
            if status == 1:
                return 1.
            elif status == 2:
                return -1.
            else:
                return None
        elif(self.whose_move == 2):
            if status == 1:
                return 1.
            elif status == 2:
                return -1.
            else:
                return None
        elif self.empty_moves == 1:
            return 0.
        else:
            return None

    def is_game_over(self):
        return self.game_result is not None

    def move(self, move):
        new_board = copy.deepcopy(self.board)
        next = -1
        if self.game_phase == 0:
            if not new_board.Put_pawn(move[0], move[1], self.whose_move):
                next = new_board.change_turn(self.whose_move)
            else:
                next = self.whose_move
        elif self.game_phase == 1:
            if not new_board.Move_pawn(move[0], move[1], move[2], move[3], self.whose_move):
                next = new_board.change_turn(self.whose_move)
            else:
                next = self.whose_move
        elif self.game_phase == 2:
            new_board.Take_off_pawn(move[0], move[1], self.whose_move)
            next = new_board.change_turn(self.whose_move)

        return State(new_board, next, new_board.phase, move)
    
