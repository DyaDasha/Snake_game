from globals import INITIAL_GAME_SPEED

# добавление бонуса


def handle_powerups(game_state):
    if game_state['game_speed'] < INITIAL_GAME_SPEED:
        game_state["game_speed"] = round(game_state["game_speed"] * 1.01)
    updated_powerups = []
    for powerup in game_state['powerups']:
        x, y, t, p = powerup  # координаты бонуса, тип и размер
        if p >= 0:
            p -= 0.02
            if p > 0:
                updated_powerups.append((x, y, t, p))
    game_state['powerups'] = updated_powerups
