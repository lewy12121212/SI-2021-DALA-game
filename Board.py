import Player
class Board:
    board=[]
    turn = 1
    player1 = Player
    player2 = Player
    players=[]
    start = 0

    #Konstruktor tworzący planszę 6x6 wypełnioną zerami
    def __init__(self):
        self.board = [[0 for j in range(6)] for i in range(6)]
        self.turn = 1
        self.player1 = Player.Player(1)
        self.player2 = Player.Player(2)
        self.players = [self.player1,self.player2]
        self.start=0

    #Wypisuje planszę
    def Printing_board(self):
        print("")
        print("It's turn Player nr", self.turn)
        for x in self.board:
            for y in x:
                print(y,end = " ")
            print()
        
    #Sprawdza czy którekolwiek z czterech środkowych pól planszy jest puste, jeśli tak zwraca fałsz, w przeciwnym wypadku zwraca prawdę
    def Four_field(self):
        if(self.board[2][2]==0 or self.board[2][3]==0 or self.board[3][2]==0 or self.board[3][3]==0):
            return False
        else:
            self.start=1 
            return True
    #Podaje ilość pionków postawionych przez gracza na planszy
    def get_players_placed_pawns(self,id):
        return self.players[id-1].placed_pawns


    #po postawieniu pionka sprawdzić czy powstała trójka
    def if_three_pawns(self,x,y):

        #Ify zapobiegają wyjściu poza zakres tablicy
        if(x<=3):
             if((self.board[x][y]==self.board[x+1][y]==self.board[x+2][y])and self.board[x][y]!=0):
                self.take_off_pawn()
                return 
        if(x>=2):
             if((self.board[x][y]==self.board[x-1][y]==self.board[x-2][y])and self.board[x][y]!=0):  
                self.take_off_pawn()
                return 
        if(y<=3):      
            if((self.board[x][y]==self.board[x][y+1]==self.board[x][y+2])and self.board[x][y]!=0):  
                self.take_off_pawn()
                return     
        if(y>=2):    
             if((self.board[x][y]==self.board[x][y-1]==self.board[x][y-2])and self.board[x][y]!=0):  
                self.take_off_pawn()  
                return                         
                          
                    
    #Zdejmuje podany pionek przeciwnika
    def take_off_pawn(self): 
        self.Printing_board()
        print("Removing opponent pawn")   
        x = int(input("Enter the row number: "))
        y = int(input("Enter the column number: "))       
        if((self.turn==1 and self.board[x][y]==2)or(self.turn==2 and self.board[x][y]==1)):
            self.board[x][y]=0
        elif((self.turn==1 and self.board[x][y]==1)or(self.turn==2 and self.board[x][y]==2)): 
            print("You can't remove your own pawn")
            self.take_off_pawn()
        else:
            print("There is no pawn to remove")
            self.take_off_pawn()
          
    #1 - gracz 1
    #2 - gracz 2

    #Wstawia pionek na podane pole (x i y = od 0 do 5), jako dany gracz (1/2)
    def Put_pawn(self,x,y,player):
        #Sprawdza czy cztery środkowe pola zostały zapełnione po raz pierwszy0
        if(self.start==0):
            self.Four_field()
        #Sprawdza czy zostały najpierw zajęte cztery środkowe pola oraz czy typowane pole jest puste
        if(self.start==1 and self.board[x][y]==0):
            self.board[x][y]=player
            self.players[self.turn-1].placed_pawns+=1
            self.players[self.turn-1].pawns_on_board+=1
            self.if_three_pawns(x,y)
            #Zmienia kolejkę gracza
            if(self.turn==1):
                self.turn = 2
            else: 
                self.turn = 1
        #Sprawdza czy gracz chce zajęć któreś z czterech środkowych pól oraz czy typowane pole jest puste
        elif (((x==2 and (y==2 or y==3)) or (x==3 and (y==2 or y==3)))and self.board[x][y]==0 ):
            self.board[x][y]=player
            self.players[self.turn-1].placed_pawns+=1
            self.players[self.turn-1].pawns_on_board+=1
            self.if_three_pawns(x,y)
            #Zmienia kolejkę gracza
            if(self.turn==1):
                self.turn = 2
            else: 
                self.turn = 1
        else:    
            print("You can't put your pawn here")



