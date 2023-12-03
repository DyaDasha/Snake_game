import logging
import time

from globals import INITIAL_SNAKE_LENGTH, INITIAL_APPLES, INITIAL_GAME_SPEED
from load_level import load_level
from place_apples import place_apples
from place_snake import place_snake

# новая игра


def initialize_new_game(game_state):
    logging.warning(game_state)
    game_state["mult"] = 1
    game_state["menu_active"] = False
    game_state["snake"] = []
    game_state['selected_level'] = '1-empty'
    game_state["powerups"] = []
    load_level(game_state)
    place_snake(INITIAL_SNAKE_LENGTH, game_state)
    game_state["apples"] = []
    place_apples(INITIAL_APPLES, game_state)
    game_state["direction"] = (1, 0)  # изначально змея едет вправо
    game_state["game_paused"] = False
    game_state["score"] = 0
    game_state["game_speed"] = INITIAL_GAME_SPEED
    game_state["last_powerup_time"] = time.time()
    game_state["current_powerup"] = None
    game_state["current_powerup_end_time"] = None
    return game_state