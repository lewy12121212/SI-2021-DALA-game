class Player:
    pawns_on_board=0
    placed_pawns=0
    player_id=0
    #Konstruktor domyślny
    def __init__(self):
        self.pawns_on_board = 0
        self.placed_pawns = 0

    #Konstruktor wraz z podaniem id gracza
    def __init__(self, id):
        self.pawns_on_board = 0
        self.placed_pawns = 0
        self.player_id = id

    #Zwraca id gracza
    def Id(self):
        return self.player_id