from globals import INITIAL_GAME_SPEED

# добавление бонуса


def handle_powerups(game_state):
    if game_state['game_speed'] < INITIAL_GAME_SPEED:
        game_state["game_speed"] = round(game_state["game_speed"] * 1.01)
    for powerup in game_state['powerups']:
        x, y, t, p = powerup
        if p < 0:
            continue
        p = p - .02
        game_state['powerups'].remove(powerup)
        if p > 0:
            game_state['powerups'].append((x, y, t, p))
