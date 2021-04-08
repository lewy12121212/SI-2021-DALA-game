class Board:
    board=[]

    #Konstruktor tworzący planszę 6x6 wypełnioną zerami
    def __init__(self):
        self.board = [[0 for j in range(6)] for i in range(6)]
        #print(board)

    #Wypisuje planszę
    def Printing_board(self):
        print("")
        for x in self.board:
            for y in x:
                print(y,end = " ")
            print()
        
    #1 - gracz 1
    #2 - gracz 2

    #Wstawia pionek na podane pole (x i y = od 0 do 5), jako dany gracz (1/2)
    def Put_pawn(self,x,y,player):
        self.board[x][y]=player


a = Board() 
a.Printing_board()
a.Put_pawn(1,1,1) 
a.Printing_board() 
a.Put_pawn(3,2,2)
a.Printing_board()
