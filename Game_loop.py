#Sprawdza czy gracze umieścili już wszystkie swoje pionki
def Putting(new_board, y, x):
    #new_board.Printing_board()
    try:
        #Podawanie miejsca postawienia pionka
        #x = input("Enter the row number: ")
        #y = input("Enter the column number: ")
        #Sprawdzanie kolejności gracza
        if(new_board.turn==1):
            id = new_board.players[0].Id()
        else:
            id = new_board.players[1].Id()
        #Umieszczanie pionka na planszy
        new_board.Put_pawn(int(x),int(y),id)
    
    except:
        pass
#Sprawdzanie czy gra nie została zakończona 
def Sliding(new_board, y, x):
    print("\nMoving your pawn")   
    #new_board.Printing_board()
    try:
        #Wybieranie pionka do przesunięcia
        #x = input("Enter the pawn row number: ")
        #y = input("Enter the pawn column number: ")
        #Sprawdzanie kolejności gracza
        if(new_board.turn==1):
            id = new_board.players[0].Id()
        else:
            id = new_board.players[1].Id()
        #Przesuwanie pionka
        new_board.If_move_pawn(int(x),int(y))
    except:
        pass
