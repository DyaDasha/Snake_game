from random import randint

from globals import SIZE_X, SIZE_Y, POWERUP_IMAGES

# добавляем бонусы


def place_powerups(powerups, game_state):
    if game_state['powerups_enabled']:
        for i in range(powerups):
            x = randint(0, SIZE_X - 1)
            y = randint(0, SIZE_Y - 1)
            while (x, y, 0) in game_state["powerups"] or (x, y) in game_state["snake"]:
                x = randint(0, SIZE_X - 1)
                y = randint(0, SIZE_Y - 1)
            game_state["powerups"].append((x, y, randint(0, len(POWERUP_IMAGES) - 2), 1))
