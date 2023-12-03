import pygame

from draw_apples import draw_apples
from draw_powerups import draw_powerups
from draw_snake import draw_snake
from draw_walls import draw_walls
from globals import BACKGROUND_COLOUR
from print_new_name_message import print_new_game_message
from print_game_paused_message import print_game_paused_message
from print_score import print_score

# обновление экрана


def update_screen(screen, game_state):
    screen.fill(BACKGROUND_COLOUR)
    if not game_state["game_running"]:
        print_new_game_message(screen)
    elif game_state["game_paused"]:
        print_game_paused_message(screen)
    else:
        draw_apples(screen, game_state["apples"])
        draw_powerups(screen, game_state["powerups"])
        draw_snake(screen, game_state)
    draw_walls(screen)
    print_score(screen, game_state)
    pygame.display.flip()