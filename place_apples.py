from random import randint

from globals import SIZE_X, SIZE_Y

# добавляем яблочки

def place_apples(apples, game_state):
    for i in range(apples):
        x = randint(0, SIZE_X - 1)
        y = randint(0, SIZE_Y - 1)
        while (x, y) in game_state["apples"] or (x, y) in game_state["snake"] or (x, y) in game_state["powerups"]:
            x = randint(0, SIZE_X - 1)
            y = randint(0, SIZE_Y - 1)
        game_state["apples"].append((x, y))