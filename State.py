class State:
    def __init__(self, board):
        self.gamePhase = {
            0: "putting",
            1: "moving",
        }
        self.board = board


    #dodatkowe metody statusu gry
    def get_game_phase(self):
        pass

    ##################################
    #zwracanie listy dostępnych ruchów
    #0: {[2,2],[3,2]}
    #1: {[2,2],[3,2]}
    def putting_board_iterator(self):
        table_of_legal_action = []
        for i in range(6):
            for j in range(6):
                if self.board[i][j] == 0:
                    table_of_legal_action.append([i,j])
            
        return table_of_legal_action

    def moving_board_iterator(self):
        table_of_legal_action = []
        for i in range(6):
            for j in range(6):
                if self.board[i][j] == self.board.turn:
                    x = self.board.Get_Legal_Moves(i, j)
                    table_of_legal_action.append(x)
            
        return table_of_legal_action

    def get_legal_actions(self): 

        if self.gamePhase == "putting":
            table_of_legal_action = self.putting_board_iterator()
            return table_of_legal_action
        elif self.gamePhase == "moving":
            table_of_legal_action = self.moving_board_iterator()
            return table_of_legal_action

        

    def is_game_over(self):
        pass

    def game_result(self):
        pass

    def move(self):
        pass

    def if_move_legal(self):
        pass

