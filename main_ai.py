from Board import Board
from mcts.nodes import *
from mcts.search import MonteCarloTreeSearch
from State import State
from Gui import Gui

def init():
    init_board = State(Board(), 1, 0)
    root = MonteCarloTreeSearchNode(state=init_board, parent=None)
    mcts = MonteCarloTreeSearch(root)
    best_node = mcts.best_action(100)
    c_state = best_node.state
    c_board = c_state.board
    return c_state, c_board



c_state, c_board = init()
c_board.Printing_board(c_board.turn)
gameWindow = Gui(c_board)
# graphics(c_board)
next_move = 2
next_phase = 0
while True:
    # move1 = get_action(c_state)
    # c_state = c_state.move(move1)
    # c_board = c_state.board
    # c_board.printBoard()
    #print('next = ', next_move)
    #print(c_board.boardValues)
    #print(c_board.turn)
    print(c_board.phase)
    board_state = State(c_board, next_move, next_phase)
    root = MonteCarloTreeSearchNode(state=board_state, parent=None)
    mcts = MonteCarloTreeSearch(root)
    best_node = mcts.best_action(100)
    c_state = best_node.state
    c_board = c_state.board
    c_board.Printing_board(next_move)
    gameWindow.setBoard(c_board)
    # graphics(c_board)
    if(c_board.If_three_pawns(c_state.current_move[0],c_state.current_move[1])):
        next_phase = 2
    else:
        next_phase = c_board.phase
    if(c_board.phase!=2):
        next_move = c_board.change_turn(next_move)
    else:
        print('ok')

    if c_state.is_game_over():
        break

print("Koniec")