from globals import INITIAL_GAME_SPEED, SNAKE_COLOUR

# создаем один из самых важных массивов игры


def initialize_game_state():  # состояние игры
    # 1) запущено приложение или нет 2) запущена игра или нет
    game_state = {
        "program_running": True,
        "game_running": False,
        "game_paused": False,
        "game_speed": INITIAL_GAME_SPEED,
        'selected_level': '1-empty',
        "high_scores": [],
        "mult": 1.0,
        "score": 0,
        "powerups": [],
        "powerups_enabled": True,
        "snake_color": SNAKE_COLOUR
    }
    return game_state
