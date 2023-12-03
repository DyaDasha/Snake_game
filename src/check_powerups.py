from place_apples import place_apples


def check_powerups(game_state):
    for powerup in game_state["powerups"]:
        if (powerup[0], powerup[1]) == game_state["snake"][0]:  # координаты головы змеи
            power = powerup[2]
            game_state["powerups"].remove(powerup)
            if power == 0:  # добавление яблока
                place_apples(1, game_state)
            elif power == 1:  # приумножение счета
                game_state["mult"] = round(game_state["mult"] * 2, 2)
            elif power == 2:  # замедление
                game_state["game_speed"] = round(game_state["game_speed"] * .75)  # уменьшает до 75%
            elif power in (3, 4):  # мина или стена
                return True  # смерть
