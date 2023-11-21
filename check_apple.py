import random

from place_apples import place_apples
from place_powerups import place_powerups

# проверка на съедание яблока


def check_apple(game_state):
    apples_eaten = 0
    for apple in game_state["apples"]:
        if apple == game_state["snake"][0]:  # координаты головы змеи
            game_state["apples"].remove(apple)
            place_apples(1, game_state)
            game_state["score"] += round(game_state["mult"], 2)
            apples_eaten += 1
            game_state["game_speed"] = round(game_state["game_speed"] * 1.01)  # увеличение скорости на 1 %
            if random.randint(0, 3) == 0:
                place_powerups(1, game_state)
    if apples_eaten == 0:
        game_state["snake"].pop()