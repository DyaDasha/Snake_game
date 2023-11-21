# движение змеи

def move_snake(game_state):
    x = game_state["snake"][0][0] + game_state["direction"][0]  # x coordinate after moving
    y = game_state["snake"][0][1] + game_state["direction"][1]  # y coordinate after moving
    game_state["snake"].insert(0, (x, y))