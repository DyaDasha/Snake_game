from flash_words import flash_words
from set_player_name import get_player_name
from show_high_scores import show_high_scores

# после столкновения (смерти) выводится фраза game over и запускается таблица рейтинга


def die(game_state, screen, menu):
    flash_words(screen, 'GAME OVER')
    player_name = get_player_name(screen)
    if player_name:
        game_state["high_scores"].append((player_name, round(game_state["score"], 2)))
        game_state["high_scores"].sort(key=lambda x: x[1], reverse=True)
        show_high_scores(game_state)
        menu.enable()