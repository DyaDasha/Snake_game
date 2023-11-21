# включаем или выключаем бонусы


def set_powerups(_, value, game_state):
    game_state["powerups_enabled"] = value
