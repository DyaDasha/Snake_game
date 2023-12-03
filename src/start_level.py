import pygame_menu
from initialize_new_game import initialize_new_game

# запуск игры


def start_level(game_state, menu):
    initialize_new_game(game_state)
    game_state["menu_active"] = False
    game_state["game_running"] = True
    if menu.is_enabled():
        menu.disable()
    return pygame_menu.events.EXIT
