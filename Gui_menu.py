import pygame
import pygame_menu
import main_ai
import time


SURFACE = pygame.display.set_mode((600, 425))

def start_game(mode, simulation_count):

    print("sim print:", simulation_count, "mode: ", mode)
    game = main_ai.Game(mode, simulation_count, SURFACE)
    player = game.start()
    return player
    # Do the job here !

class GameMenu:
    def __init__(self) -> None:
        #set variables
        self.simulation_count = 100
        self.mode = 0
        self.show_main_menu = True
        self.winner = 0
        
        #call init funcitons
        self.init_main_menu()
        self.init_restart_menu()


    def init_main_menu(self):
        self.main_menu = pygame_menu.Menu(300, 400, 'Menu', theme=pygame_menu.themes.THEME_GREEN)
        self.main_menu.add.text_input('Symulacje :', default=100, onchange=self.set_count)
        self.main_menu.add.selector('Tryb :', [('AI vs AI', 0), ('User vs AI', 1)], onchange=self.set_game_mode)
        self.main_menu.add.button('Play', self.start_the_game)
        self.main_menu.add.button('Quit', pygame_menu.events.EXIT)

    def init_restart_menu(self):
        self.restart_menu = pygame_menu.Menu(300, 400, 'Wynik', theme=pygame_menu.themes.THEME_GREEN)
        self.restart_menu.add.label(str(self.winner), label_id="player_winner", onselect=None)
        self.restart_menu.add.button('Restart', self.start_the_game)
        self.restart_menu.add.button('Back to menu', self.set_menu)


    def start(self) -> None:
        while True:

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    exit()

            if self.show_main_menu and self.main_menu.is_enabled():
                SURFACE.fill((0, 0, 0))
                self.main_menu.update(events)
                self.main_menu.draw(SURFACE)
            else:
                #self.restart_menu.set_attribute("player_winner", str(self.winner))
                self.restart_menu.update(events)
                self.restart_menu.draw(SURFACE)


            pygame.display.update()
            time.sleep(0.1)

        #self.menu.mainloop(SURFACE)

    def set_game_mode(self, mode_tuple, mode):
        print("Print: ", mode_tuple, " count: ", mode)
        # Do the job here !
        self.mode = mode

    def set_count(self, count):
        self.simulation_count = count
        print(self.simulation_count, " + ", count)

    def set_menu(self):
        self.show_main_menu = True

    def start_the_game(self):
        self.winner = start_game(self.mode, int(self.simulation_count))
        self.show_main_menu = False

        self.restart_menu = None
        self.init_restart_menu()
        
        print("koniec gry menu :/")

if __name__ == "__main__":
    pygame.init()
    menu = GameMenu()
    menu.start()
