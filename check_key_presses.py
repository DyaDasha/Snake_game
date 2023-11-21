import pygame_menu
from start_level import start_level

# проверка, какие клавиши нажаты


def check_key_presses(events, game_state, menu):
    if pygame_menu.events.EXIT in events:
        start_level(game_state, menu)
    if "quit" in events:
        game_state["program_running"] = False  # main exits the loop and closes the game
    elif not game_state["game_running"]:  # check which buttons have been pressed
        if "escape" in events:
            game_state["program_running"] = False
        # elif "enter" in events:
        #     initialize_new_game(game_state)
        #     game_state["game_running"] = True
    elif game_state["game_paused"]:
        if "escape" in events:
            game_state["game_running"] = True
        elif "space" in events:
            game_state["game_paused"] = False
    else:
        if "escape" in events or "space" in events:
            game_state["game_paused"] = True
        if "up" in events:
            game_state["direction"] = (0, -1)
        if "down" in events:
            game_state["direction"] = (0, 1)
        if "left" in events:
            game_state["direction"] = (-1, 0)
        if "right" in events:
            game_state["direction"] = (1, 0)