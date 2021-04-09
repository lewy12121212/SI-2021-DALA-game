import Board
import Player
import os


print("Dala game started!")
new_board = Board.Board() 
new_board.Printing_board()
#Sprawdza czy gracze umieścili już wszystkie swoje pionki
while (new_board.get_players_placed_pawns(1)!=12 or new_board.get_players_placed_pawns(2)!=12):
    #Podawanie miejsca postawienia pionka
    x = input("Podaj numer kolumny: ")
    y = input("Podaj numer wiersza: ")
    #Sprawdzanie kolejności gracza
    if(new_board.turn==1):
        id = new_board.players[0].id()
    else:
        id = new_board.players[1].id()

    #Umieszczanie pionka na planszy
    new_board.Put_pawn(int(x),int(y),id)
    new_board.Printing_board()

