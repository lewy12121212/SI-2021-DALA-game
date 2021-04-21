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

    def Split_turn(self):
        #Zmienia kolejkę gracza
        if(self.turn == 1):
            self.turn = 2
        else: 
            self.turn = 1

    #po postawieniu pionka sprawdzić czy powstała trójka
    def If_three_pawns(self,x,y):

        #Ify zapobiegają wyjściu poza zakres tablicy
        if(x<=3):
             if((self.board[x][y]==self.board[x+1][y]==self.board[x+2][y]) and self.board[x][y]!=0):
                #self.Take_off_pawn()
                return True # informacja zwerotna o istnieniu trójki 
        if(x>=2):
             if((self.board[x][y]==self.board[x-1][y]==self.board[x-2][y]) and self.board[x][y]!=0):  
                #self.Take_off_pawn()
                return True # informacja zwerotna o istnieniu trójki 
        if(y<=3):      
            if((self.board[x][y]==self.board[x][y+1]==self.board[x][y+2]) and self.board[x][y]!=0):  
                #self.Take_off_pawn()
                return True # informacja zwerotna o istnieniu trójki   
        if(y>=2):    
             if((self.board[x][y]==self.board[x][y-1]==self.board[x][y-2]) and self.board[x][y]!=0):  
                #self.Take_off_pawn()  
                return True # informacja zwerotna o istnieniu trójki 
        else:
            return False # informacja zwerotna o istnieniu trójki                       
                          
                    
    #Zdejmuje podany pionek przeciwnika 
    def Take_off_pawn(self, field): 
        self.Printing_board()
        print("Removing opponent pawn") 
        x = field[1]
        y = field[0]     
        if((self.turn==1 and self.board[x][y]==2)or(self.turn==2 and self.board[x][y]==1)):
            self.board[x][y]=0
            self.players[self.turn-1].pawns_on_board-=1
            return True
        elif((self.turn==1 and self.board[x][y]==1)or(self.turn==2 and self.board[x][y]==2)): 
            print("You can't remove your own pawn")
            return False
            #self.Take_off_pawn(field)
        else:
            print("There is no pawn to remove")
            return False
            #self.Take_off_pawn(field)
          
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
            #self.If_three_pawns(x,y)
            #Zmienia kolejkę gracza
            self.Split_turn()

            return True #zwrócenie informacji o tym czy pionek został postawiony czy nie 
        #Sprawdza czy gracz chce zajęć któreś z czterech środkowych pól oraz czy typowane pole jest puste
        elif (((x==2 and (y==2 or y==3)) or (x==3 and (y==2 or y==3)))and self.board[x][y]==0 ):
            self.board[x][y]=player
            self.players[self.turn-1].placed_pawns+=1
            self.players[self.turn-1].pawns_on_board+=1
            #self.If_three_pawns(x,y)
            #Zmienia kolejkę gracza
            self.Split_turn()

            return True #zwrócenie informacji o tym czy pionek został postawiony czy nie 
        else:    
            print("You can't put your pawn here")
            return False #zwrócenie informacji o tym czy pionek został postawiony czy nie 

        #self.If_three_pawns(x,y)

    #Sprawdza czy gracz może przesunąć dany pionek
    def If_move_pawn(self,x,y):
        if((self.turn==1 and self.board[x][y]==2)or(self.turn==2 and self.board[x][y]==1)):
            print("You can't move your oponent's pawn")
            return False
        elif((self.turn==1 and self.board[x][y]==1)or(self.turn==2 and self.board[x][y]==2)): 
            #self.Move_pawn(x,y)
            return True
        else:
            print("There is no pawn to move")
            return False

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
    def Move_pawn(self, x, y, mx, my):
        #mx = int(input("Move: Enter the row number: "))
        #my = int(input("Move: Enter the column number: "))
        #Sprawdzenie czy wybrane pole nie jest puste
        print(x, " ", y, " - ", mx, " ", my)

        if(self.board[mx][my]!=0):
            print("1. You can't move pawn here")
            return False
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
                    #self.If_three_pawns(int(mx),int(my))
                    #Zmiana tury
                    self.Split_turn()
                    return True
                else:
                    print("2. You can't move pawn here")
                    return False
                    #mx = int(input("Move: Enter the row number: "))
                    #my = int(input("Move: Enter the column number: "))
