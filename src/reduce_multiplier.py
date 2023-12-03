# уменьшаем множитель


def reduce_multiplier(game_state):
    game_state["mult"] = max(1, game_state["mult"] - 0.01)
