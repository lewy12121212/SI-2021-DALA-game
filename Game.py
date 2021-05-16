import Board
import Player
import State
import os

class Game:
    def __init__(self):
        self.board = Board.Board()
        self.gameState = State.State(self.board)

    def run(self):
        self.putting()
        self.moving()

    def end(self):
        if self.board.Get_players_placed_pawns(1)!=5 or self.board.Get_players_placed_pawns(2)!=5:
            return True
        elif self.board.Get_players_pawns_on_board(1)>2 or self.board.Get_players_pawns_on_board(2)>2:
            return True
        else:
            return False

    def take_off_pawn():
        pass

    def putting(self):
        
        if not self.end():
            try:
                self.board.Printing_board()
                #Podawanie miejsca postawienia pionka
                x = input("Enter the row number: ")
                y = input("Enter the column number: ")
                #Sprawdzanie kolejności gracza
                if(self.board.turn==1):
                    id = self.board.players[0].Id()
                else:
                    id = self.board.players[1].Id()

                #Umieszczanie pionka na planszy
                self.board.Put_pawn(int(x),int(y),id)

                #zmiana tury
                self.board.change_turn()

            except:
                pass

    def moving(self):
        #Sprawdzanie czy gra nie została zakończona         
        while(self.board.Get_players_pawns_on_board(1)>2 or self.board.Get_players_pawns_on_board(2)>2):
            print("\nMoving your pawn")   
            self.board.Printing_board()
            try:
                #Wybieranie pionka do przesunięcia
                x = input("Enter the pawn row number: ")
                y = input("Enter the pawn column number: ")
                #Sprawdzanie kolejności gracza
                if(self.board.turn==1):
                    id = self.board.players[0].Id()
                else:
                    id = self.board.players[1].Id()

                #Przesuwanie pionka
                self.board.If_move_pawn(int(x),int(y))
            except:
                pass