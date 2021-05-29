from Board import Board
from mcts.nodes import *
from mcts.search import MonteCarloTreeSearch
from State import State
from Gui import Gui

def init():
    init_board = State(Board(), 1, 0)
    root = MonteCarloTreeSearchNode(state=init_board, parent=None)
    mcts = MonteCarloTreeSearch(root)
    best_node = mcts.best_action(50)
    c_state = best_node.state
    c_board = c_state.board
    return c_state, c_board

Player = 2;

c_state, c_board = init()
#c_board = State(Board(), 1, 0)
c_board.Printing_board(c_board.turn)
gameWindow = Gui(c_board)
# graphics(c_board)
next_move = 2
next_phase = 0
while True:
    if Player == 1:
        print(c_board.phase)
        board_state = State(c_board, 1, next_phase)
        root = MonteCarloTreeSearchNode(state=board_state, parent=None)
        mcts = MonteCarloTreeSearch(root)
        best_node = mcts.best_action(100)
        c_state = best_node.state
        c_board = c_state.board
        c_board.Printing_board(Player)
        gameWindow.setBoard(c_board)
        # graphics(c_board)

        #print("trojka1 " + str(c_board.If_three_pawns(c_state.current_move[0], c_state.current_move[1])))
        if(next_phase == 1):
            if(c_board.If_three_pawns(c_state.current_move[2],c_state.current_move[3])):
                print("ok")
                next_phase = 2
                Player = 1
            else:
                next_phase = c_board.phase
                Player = 2
        else:
            if (c_board.If_three_pawns(c_state.current_move[0], c_state.current_move[1])):
                print("ok")
                next_phase = 2
                Player = 1
            else:
                next_phase = c_board.phase
                Player = 2

        if c_state.is_game_over():
            break


    elif Player == 2:
        print(c_board.phase)
        board_state = State(c_board, 2, next_phase)
        root = MonteCarloTreeSearchNode(state=board_state, parent=None)
        mcts = MonteCarloTreeSearch(root)
        best_node = mcts.best_action(100)
        c_state = best_node.state
        c_board = c_state.board
        c_board.Printing_board(Player)
        gameWindow.setBoard(c_board)
        # graphics(c_board)
        #print("trojka2 " + str(c_board.If_three_pawns(c_state.current_move[0], c_state.current_move[1])))
        if(next_phase == 1):
            if (c_board.If_three_pawns(c_state.current_move[2], c_state.current_move[3])):
                print("ok")
                next_phase = 2
                Player = 2
            else:
                next_phase = c_board.phase
                Player = 1
        else:
            if (c_board.If_three_pawns(c_state.current_move[0], c_state.current_move[1])):
                print("ok")
                next_phase = 2
                Player = 2
            else:
                next_phase = c_board.phase
                Player = 1


        if c_state.is_game_over():
            break


print("Koniec")