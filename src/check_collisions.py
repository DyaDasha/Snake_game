from globals import SIZE_X, SIZE_Y


# проверка на столкновение


def check_collisions(game_state):
    x, y = game_state["snake"][0]
    if x not in range(SIZE_X) or y not in range(SIZE_Y):
        game_state["game_running"] = False
    if (len(game_state["snake"])) > len(set(game_state["snake"])):
        game_state["game_running"] = False
    return not game_state["game_running"]
