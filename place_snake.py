from globals import SIZE_X, SIZE_Y

# добавляем змею


def place_snake(length, game_state):
    x = SIZE_X // 2
    y = SIZE_Y // 2
    game_state["snake"].append((x, y))
    for i in range(1, length):
        game_state["snake"].append((x - i, y))