# уменьшаем множитель


def reduce_multiplier(game_state):
    if game_state["mult"] > 1:
        game_state["mult"] = float(game_state["mult"] * 100 - 1) / float(100.0)
        if game_state["mult"] < 1:
            game_state["mult"] = 1
