import pygame
import pygame_menu
import main_ai


SURFACE = pygame.display.set_mode((600, 425))

def start_game(mode, simulation_count):

    while True:
        print("sim print:", simulation_count, "mode: ", mode)
        game = main_ai.Game(mode, simulation_count, SURFACE)
        player = game.start()
        print("koniec gry menu :/")
        RestartMenu(player)

    # Do the job here !

class RestartMenu:
    def __init__(self, player) -> None:
        self.menu = pygame_menu.Menu(300, 400, 'Wynik', theme=pygame_menu.themes.THEME_GREEN)
        self.simulation_count = 100
        self.mode = 0
        self.player = player
        self.start()

    def start(self) -> None:
        txt_for_label = "Wygrał użytkownik: "
        txt_for_label += self.player
        self.menu.add.label(txt_for_label, label_id='A', onselect=None)
        #self.menu.add.text_input('Symulacje :', default=100, onchange=self.set_count)
        #self.menu.add.selector('Tryb :', [('AI vs AI', 0), ('User vs AI', 1)], onchange=self.set_game_mode)
        self.menu.add.button('Restart', self.start_the_game)
        self.menu.add.button('Back to menu', pygame_menu.events.EXIT)
        self.menu.mainloop(SURFACE)

    def set_game_mode(self, mode_tuple, mode):
        print("Print: ", mode_tuple, " count: ", mode)
        # Do the job here !
        self.mode = mode

    def set_count(self, count):
        self.simulation_count = count
        print(self.simulation_count, " + ", count)

    def start_the_game(self):
        start_game(self.mode, int(self.simulation_count))



class GameMenu:
    def __init__(self) -> None:
        self.menu = pygame_menu.Menu(300, 400, 'Welcome', theme=pygame_menu.themes.THEME_GREEN)
        self.simulation_count = 100
        self.mode = 0

    def start(self) -> None:
        self.menu.add.text_input('Symulacje :', default=100, onchange=self.set_count)
        self.menu.add.selector('Tryb :', [('AI vs AI', 0), ('User vs AI', 1)], onchange=self.set_game_mode)
        self.menu.add.button('Play', self.start_the_game)
        self.menu.add.button('Quit', pygame_menu.events.EXIT)

        self.menu.mainloop(SURFACE)

    def set_game_mode(self, mode_tuple, mode):
        print("Print: ", mode_tuple, " count: ", mode)
        # Do the job here !
        self.mode = mode

    def set_count(self, count):
        self.simulation_count = count
        print(self.simulation_count, " + ", count)

    def start_the_game(self):
        start_game(self.mode, int(self.simulation_count))



if __name__ == "__main__":
    pygame.init()
    menu = GameMenu()
    menu.start()
