import Player


class Board:
    board=[]
    turn = 1
    start = 0

    #Konstruktor tworzący planszę 6x6 wypełnioną zerami
    def __init__(self):
        self.board = [[0 for j in range(6)] for i in range(6)]
        self.turn = 1
        self.player1 = Player.Player(1)
        self.player2 = Player.Player(2)
        self.players = [self.player1, self.player2]
        self.start = 1
        self.phase = 0
        self.X = 0
        self.init_board = [[2,2],[2,3],[3,2],[3,3]]

    #sprawdzenie ilości poionków przy ruchu użytkownika
    def set_state_for_user_move(self):
        if self.Get_players_placed_pawns(1) == 12 and self.Get_players_placed_pawns(2) == 12:
            self.phase = 1


    #zwraca plansze
    def Get_board(self):
        return self.board

    #Wypisuje planszę
    def Printing_board(self,who):
        print("")
        print("It's turn Player nr", who)
        for x in self.board:
            for y in x:
                print(y, end = " ")
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
    def Get_players_pawns_on_board(self, id):
        #return self.players[id-1].pawns_on_board
        quantity = 0
        for j in self.board:
            for i in j:
                if i == id:
                    quantity += 1

        return quantity

        # Podaje ilość pionków gracza znajdujących się na planszy
    def Get_players_pawns(self, id):
        return self.players[id - 1].all_pawns

    #po postawieniu pionka sprawdzić czy powstała trójka
    def If_three_pawns(self,x,y):
        
        #result = False
        #Ify zapobiegają wyjściu poza zakres tablicy
        if(x<=3):
            if((self.board[x][y]==self.board[x+1][y]==self.board[x+2][y])and self.board[x][y]!=0):
                return True        
        if(x>=2):
            if((self.board[x][y]==self.board[x-1][y]==self.board[x-2][y])and self.board[x][y]!=0):  
                return True
        if(y<=3):
            if((self.board[x][y]==self.board[x][y+1]==self.board[x][y+2])and self.board[x][y]!=0):  
                return True  
        if(y>=2):
            if((self.board[x][y]==self.board[x][y-1]==self.board[x][y-2])and self.board[x][y]!=0):  
                return True
        if (x >= 1 and x <= 4):
            if ((self.board[x][y] == self.board[x + 1][y] == self.board[x - 1][y]) and self.board[x][y] != 0):
                return True  # informacja zwerotna o istnieniu trójki
        if (y >= 1 and y <= 4):
            if ((self.board[x][y] == self.board[x][y + 1] == self.board[x][y - 1]) and self.board[x][y] != 0):
                return True  # informacja zwerotna o istnieniu trójki

        return False
                    
    #Zdejmuje podany pionek przeciwnika
    def Take_off_pawn(self, x, y, who):
        #self.Printing_board()
        #print("Removing opponent pawn")
        oponent = -1
        #print("take off: ", who)
        if(who == 1):
            oponent = 1
        else:
            oponent = 0
        if(self.board[x][y] !=0 and self.board[x][y]!=who):
            self.board[x][y] = 0
            self.players[oponent].pawns_on_board -= 1
            self.players[oponent].all_pawns -= 1

        if self.Get_players_placed_pawns(oponent + 1) < 12:
            self.phase = 0
        else:
            self.phase = 1

        #self.Printing_board(who)
    #1 - gracz 1
    #2 - gracz 2

    #Wstawia pionek na podane pole (x i y = od 0 do 5), jako dany gracz (1/2)
    def Put_pawn(self, x, y, who):
        #Sprawdza czy cztery środkowe pola zostały zapełnione po raz pierwszy0
        #if(self.start==0):
        #   self.Four_field()
        #Sprawdza czy zostały najpierw zajęte cztery środkowe pola oraz czy typowane pole jest puste
        if(self.start==1 and self.board[x][y]==0 and self.Get_players_placed_pawns(who) < 12):
            self.board[x][y]=who
            self.players[who-1].placed_pawns+=1
            self.players[who-1].pawns_on_board+=1

        if self.If_three_pawns(x, y):
            self.phase = 2
            return True
        elif self.Get_players_placed_pawns(1) == 12 and self.Get_players_placed_pawns(2) == 12:
            self.phase = 1
            return False
        else:
            return False
        #self.Printing_board(who)

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

    #zwraca wszysctkich dostępnych sąsiadów (możliwe pola ruchu)  
    def Get_legal_moves(self, x, y):
        table_of_legal_moves = []

        if y > 0 and self.board[x][y-1] == 0:
            table_of_legal_moves.append([x, y, x, y-1])

        if y < 5 and self.board[x][y+1] == 0:
            table_of_legal_moves.append([x, y, x, y+1])

        if x > 0 and self.board[x-1][y] == 0:
            table_of_legal_moves.append([x, y, x-1, y])

        if x < 5 and self.board[x+1][y] == 0:
            table_of_legal_moves.append([x, y, x+1, y])
        
        return table_of_legal_moves
    

    def end(self):
        #print(self.Get_players_pawns(1), ":", self.Get_players_pawns(2))
        if self.Get_players_pawns(1)<3:
            return 2
        elif self.Get_players_pawns(2)<3:
            #self.X+=1
            #print(self.X)
            return 1
        else:
            return 0



    #Sprawdza czy można przesunąć pionek na wybrane pole i go przesuwa
    def Move_pawn(self, x, y, mx, my, who):
        #Sprawdzenie czy wybrane pole nie jest puste
        self.board[x][y]=0
        self.board[int(mx)][int(my)] = who
        if self.If_three_pawns(int(mx), int(my)):
            self.phase = 2
            return True
        else:
            return False
    
    
    def change_turn(self, who):
        if(who == 1):
            return 2
        else: 
            return 1

    def change_turn_not_ai(self):
        if(self.turn==1):
            self.turn = 2
        else:
            self.turn = 1

    def get_turn(self):
        return self.turn
            
    