from Board import Board
from mcts.nodes import *
from mcts.search import MonteCarloTreeSearch
from State import State
from Gui import Gui
import Gui_user

def init():
    init_board = State(Board(), 1, 0)
    root = MonteCarloTreeSearchNode(state=init_board, parent=None)
    mcts = MonteCarloTreeSearch(root)
    best_node = mcts.best_action(50)
    c_state = best_node.state
    c_board = c_state.board
    return c_state, c_board

class Game:
    def __init__(self, type_of_game, count_of_simulation, window) -> None:
        self.Player = 2;
        self.c_state, self.c_board = init()
        #c_board = State(Board(), 1, 0)
        self.c_board.Printing_board(self.c_board.turn)
        self.gameWindow = Gui(self.c_board, window)
        # graphics(c_board)
        self.next_move = 2
        self.next_phase = 0

        self.count_of_simulation = count_of_simulation
        self.type_of_game = type_of_game

    def start(self):
        print("ilość symulacji: ", self.count_of_simulation)

        if(self.type_of_game == 0):
            self.ai_vs_ai()
        elif(self.type_of_game == 1):
            self.user_vs_ai()
        else:
            print("type of game problem!")

    def ai_player_move(self):
        print(self.c_board.phase)
        board_state = State(self.c_board, self.Player, self.next_phase)
        root = MonteCarloTreeSearchNode(state=board_state, parent=None)
        mcts = MonteCarloTreeSearch(root)
        best_node = mcts.best_action(self.count_of_simulation)
        self.c_state = best_node.state
        self.c_board = self.c_state.board
        self.c_board.Printing_board(self.Player)
        #self.gameWindow.setBoard(self.c_board, self.next_phase, self.Player)

    def user_player_move(self):
        self.c_board, user_last_x, user_last_y = self.gui_user.user_move(self.c_board, 2, self.next_phase)
        #self.gameWindow.setBoard(self.c_board)
        return user_last_x, user_last_y

    def user_vs_ai(self):
        self.gui_user = Gui_user.Gui_user(self.c_board, 2)

        while True:
            #print("while phase: ", self.next_phase)
            #print("end: ", self.c_board.end())

            if self.Player == 1:
                self.ai_player_move()
                # graphics(c_board)

                #print("trojka1 " + str(c_board.If_three_pawns(c_state.current_move[0], c_state.current_move[1])))
                if(self.next_phase == 1):
                    if(self.c_board.If_three_pawns(self.c_state.current_move[2],self.c_state.current_move[3])):
                        print("ok")
                        self.next_phase = 2
                        self.Player = 1
                    else:
                        self.next_phase = self.c_board.phase
                        self.Player = 2
                else:
                    if (self.c_board.If_three_pawns(self.c_state.current_move[0], self.c_state.current_move[1])):
                        print("ok")
                        self.next_phase = 2
                        self.Player = 1
                    else:
                        self.next_phase = self.c_board.phase
                        self.Player = 2

                if self.c_state.is_game_over():
                    break

            elif self.Player == 2:
                user_last_x, user_last_y = self.user_player_move()
                #print("user x/y:",user_last_x,": ", user_last_y)
                # graphics(c_board)
                #print("trojka2 " + str(c_board.If_three_pawns(c_state.current_move[0], c_state.current_move[1])))
                if(self.next_phase == 1):
                    if (self.c_board.If_three_pawns(user_last_y, user_last_x)):
                        print("ok")
                        self.next_phase = 2
                        self.Player = 2
                    else:
                        self.c_board.set_state_for_user_move()
                        self.next_phase = self.c_board.phase
                        self.Player = 1
                else:
                    if (self.c_board.If_three_pawns(user_last_y, user_last_x)):
                        print("ok")
                        self.next_phase = 2
                        self.Player = 2
                    else:
                        self.c_board.set_state_for_user_move()
                        self.next_phase = self.c_board.phase
                        self.Player = 1

                if self.c_board.end() == 1 or self.c_board.end() == 2:
                    break
            self.gameWindow.setBoard(self.c_board, self.next_phase, self.Player)

        print("Koniec")
        return self.Player

    def ai_vs_ai(self):

        while True:
            print("while phase: ", self.next_phase)

            if self.Player == 1:
                self.ai_player_move()
                # graphics(c_board)

                #print("trojka1 " + str(c_board.If_three_pawns(c_state.current_move[0], c_state.current_move[1])))
                if(self.next_phase == 1):
                    if(self.c_board.If_three_pawns(self.c_state.current_move[2],self.c_state.current_move[3])):
                        print("ok")
                        self.next_phase = 2
                        self.Player = 1
                    else:
                        self.next_phase = self.c_board.phase
                        self.Player = 2
                else:
                    if (self.c_board.If_three_pawns(self.c_state.current_move[0], self.c_state.current_move[1])):
                        print("ok")
                        self.next_phase = 2
                        self.Player = 1
                    else:
                        self.next_phase = self.c_board.phase
                        self.Player = 2

                if self.c_state.is_game_over():
                    break

            elif self.Player == 2:
                self.ai_player_move()
                # graphics(c_board)
                #print("trojka2 " + str(c_board.If_three_pawns(c_state.current_move[0], c_state.current_move[1])))
                if(self.next_phase == 1):
                    if (self.c_board.If_three_pawns(self.c_state.current_move[2], self.c_state.current_move[3])):
                        print("ok")
                        self.next_phase = 2
                        self.Player = 2
                    else:
                        self.next_phase = self.c_board.phase
                        self.Player = 1
                else:
                    if (self.c_board.If_three_pawns(self.c_state.current_move[0], self.c_state.current_move[1])):
                        print("ok")
                        self.next_phase = 2
                        self.Player = 2
                    else:
                        self.next_phase = self.c_board.phase
                        self.Player = 1

                if self.c_state.is_game_over():
                    break
            self.gameWindow.setBoard(self.c_board, self.next_phase, self.Player)

        print("Koniec")
        return self.Player


if __name__ == "__main__":
    game = Game(10)
    game.start()
