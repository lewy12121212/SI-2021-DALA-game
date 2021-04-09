import Player
class Board:
    board=[]
    turn = 1
    player1 = Player
    player2 = Player
    players=[]
    #Konstruktor tworzący planszę 6x6 wypełnioną zerami
    def __init__(self):
        self.board = [[0 for j in range(6)] for i in range(6)]
        self.turn = 1
        self.player1 = Player.Player(1)
        self.player2 = Player.Player(2)
        self.players = [self.player1,self.player2]

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
            return True
    #Podaje ilość pionków postawionych przez gracza na planszy
    def get_players_placed_pawns(self,id):
        return self.players[id-1].placed_pawns

       

    #1 - gracz 1
    #2 - gracz 2

    #Wstawia pionek na podane pole (x i y = od 0 do 5), jako dany gracz (1/2)
    def Put_pawn(self,x,y,player):
        #Sprawdza czy zostały najpierw zajęte cztery środkowe pola oraz czy typowane pole jest puste
        if(self.Four_field()==True and self.board[x][y]==0):
            self.board[x][y]=player
            self.players[self.turn-1].placed_pawns+=1
            self.players[self.turn-1].pawns_on_board+=1
            #Zmienia kolejkę gracza
            if(self.turn==1):
                self.turn = 2
            else: 
                self.turn = 1
        #Sprawdza czy gracz chce zajęć któreś z czterech środkowych pól oraz czy typowane pole jest puste
        elif (((x==2 and (y==2 or y==3)) or (x==3 and (y==2 or y==3)))and self.board[x][y]==0):
            self.board[x][y]=player
            self.players[self.turn-1].placed_pawns+=1
            self.players[self.turn-1].pawns_on_board+=1
            #Zmienia kolejkę gracza
            if(self.turn==1):
                self.turn = 2
            else: 
                self.turn = 1
        else:    
            print("You can't put your pawn here")



