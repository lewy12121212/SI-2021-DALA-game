import pygame
import pygame_menu
import main_ai

pygame.init()
surface = pygame.display.set_mode((600, 400))

def set_game_mode(mode_tuple, mode):
    print("Print: ", mode_tuple, " count: ", mode)
    # Do the job here !
    pass

def start_the_game():
    main_ai.ai_vs_ai(100)
    # Do the job here !
    pass

menu = pygame_menu.Menu(300, 400, 'Welcome', theme=pygame_menu.themes.THEME_GREEN)

menu.add.text_input('Symulacje :', default=100)
menu.add.selector('Tryb :', [('AI vs AI', 0), ('User vs AI', 1)], onchange=set_game_mode)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(surface)
