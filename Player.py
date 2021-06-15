class Player:

    #Konstruktor domyślny
    def __init__(self):
        self.pawns_on_board = 0
        self.placed_pawns = 0
        self.all_pawns = 12

    #Konstruktor wraz z podaniem id gracza
    def __init__(self, id):
        self.pawns_on_board = 0
        self.placed_pawns = 0
        self.player_id = id
        self.all_pawns = 12

    #Zwraca id gracza
    def Id(self):
        return self.player_id


    def SubtractPawn(self):
        self.all_pawns -= 1