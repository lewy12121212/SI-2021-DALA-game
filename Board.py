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
    def Get_players_placed_pawns(self,id):
        return self.players[id-1].placed_pawns

    #Podaje ilość pionków gracza znajdujących się na planszy
    def Get_players_pawns_on_board(self,id):
        return self.players[id-1].pawns_on_board    


    #po postawieniu pionka sprawdzić czy powstała trójka
    def If_three_pawns(self,x,y):

        #Ify zapobiegają wyjściu poza zakres tablicy
        if(x<=3):
             if((self.board[x][y]==self.board[x+1][y]==self.board[x+2][y])and self.board[x][y]!=0):
                self.Take_off_pawn()
                return 
        if(x>=2):
             if((self.board[x][y]==self.board[x-1][y]==self.board[x-2][y])and self.board[x][y]!=0):  
                self.Take_off_pawn()
                return 
        if(y<=3):      
            if((self.board[x][y]==self.board[x][y+1]==self.board[x][y+2])and self.board[x][y]!=0):  
                self.Take_off_pawn()
                return     
        if(y>=2):    
             if((self.board[x][y]==self.board[x][y-1]==self.board[x][y-2])and self.board[x][y]!=0):  
                self.Take_off_pawn()  
                return                         
                          
                    
    #Zdejmuje podany pionek przeciwnika
    def Take_off_pawn(self): 
        self.Printing_board()
        print("Removing opponent pawn") 
        x = int(input("Enter the row number: "))
        y = int(input("Enter the column number: "))       
        if((self.turn==1 and self.board[x][y]==2)or(self.turn==2 and self.board[x][y]==1)):
            self.board[x][y]=0
            self.players[self.turn-1].pawns_on_board-=1
        elif((self.turn==1 and self.board[x][y]==1)or(self.turn==2 and self.board[x][y]==2)): 
            print("You can't remove your own pawn")
            self.Take_off_pawn()
        else:
            print("There is no pawn to remove")
            self.Take_off_pawn()
          
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
            self.If_three_pawns(x,y)
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
            self.If_three_pawns(x,y)
            #Zmienia kolejkę gracza
            if(self.turn==1):
                self.turn = 2
            else: 
                self.turn = 1
        else:    
            print("You can't put your pawn here")

        #self.If_three_pawns(x,y)

    #Sprawdza czy gracz może przesunąć dany pionek
    def If_move_pawn(self,x,y):
        if((self.turn==1 and self.board[x][y]==2)or(self.turn==2 and self.board[x][y]==1)):
            print("You can't move your oponent's pawn")
        elif((self.turn==1 and self.board[x][y]==1)or(self.turn==2 and self.board[x][y]==2)): 
            self.Move_pawn(x,y)
        else:
            print("There is no pawn to move")

    #Sprawdza czy dwa pola sąsiadują ze sobą
    def Neighbours(self,x,ax):
        if(x>0):
            if(x==ax+1):
                return True
        if(x<5):
            if(x==ax-1):
                return True
        return False        
    
    #Sprawdza czy można przesunąć pionek na wybrane pole i go przesuwa
    def Move_pawn(self,x,y):
        mx = int(input("Move: Enter the row number: "))
        my = int(input("Move: Enter the column number: "))
        #Sprawdzenie czy wybrane pole nie jest puste
        if(self.board[mx][my]!=0):
            print("You can't move pawn here")
        else:
            while(True):
                self.Neighbours(x,mx)
                #Sprawdza czy pola sąsiadują ze sobą i nie są po skosie
                if((self.Neighbours(x,int(mx)) and y==int(my)) or (self.Neighbours(y,int(my)) and x==int(mx))):
                    #Czyszczenie poprzedniego pola
                    self.board[x][y]=0
                    #Wstawianie pionka na nowe pole
                    if(self.turn==1):
                        self.board[int(mx)][int(my)]=1
                    else:
                        self.board[int(mx)][int(my)]=2
                    #Sprawdzanie czy nie wystąpił rząd 3
                    self.If_three_pawns(int(mx),int(my))
                    #Zmiana tury
                    if(self.turn==1):
                        self.turn = 2
                    else: 
                        self.turn = 1
                    return
                else:
                    print("You can't move pawn here")
                    mx = int(input("Move: Enter the row number: "))
                    my = int(input("Move: Enter the column number: "))
