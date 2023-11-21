import time

import pygame
import sys

from build_main_menu import build_main_menu
from get_events import get_events
from globals import WIDTH, HEIGHT
from initialize_game_state import initialize_game_state
from initialize_snake import initialize_snake
from set_level import set_level
from shutdown import shutdown
from update_game_state import update_game_state
from update_screen import update_screen


def main():
    screen, clock = initialize_snake((WIDTH, HEIGHT))
    game_state = initialize_game_state()
    menu = build_main_menu(game_state)
    set_level('', '1-empty.csv', game_state)
    while game_state["program_running"]:
        events, raw = get_events()
        if game_state['game_running']:
            clock.tick(game_state["game_speed"])
        if menu.is_enabled():
            menu.update(raw)
            if menu.is_enabled():
                menu.draw(screen)
            pygame.display.update()
        else:
            update_game_state(events, game_state, menu, screen)
            update_screen(screen, game_state)
    shutdown()











main()
