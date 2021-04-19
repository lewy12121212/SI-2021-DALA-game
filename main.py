import Board
import Player
import os
import Gui
import threading
import time
from Game_loop import *



print("Dala game started!")
new_board = Board.Board() 
gui = Gui.Gui(new_board)
#threading.Thread(target=Gui.Gui()).start()
#new_board.Printing_board()

#Putting(new_board)
#Sliding(new_board)