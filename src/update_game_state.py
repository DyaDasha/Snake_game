from check_apple import check_apple
from check_collisions import check_collisions
from check_key_presses import check_key_presses
from check_powerups import check_powerups
from die import die
from handle_powerups import handle_powerups
from move_snake import move_snake
from reduce_multiplier import reduce_multiplier


def update_game_state(events, game_state, menu, screen):  # обновление состояния игры
    check_key_presses(events, game_state, menu)  # нажаты ли клавиши
    if game_state["game_running"] and not game_state["game_paused"]:
        reduce_multiplier(game_state)
        move_snake(game_state)
        handle_powerups(game_state)
        if check_collisions(game_state):
            die(game_state, screen, menu)

        else:
            check_apple(game_state)
            if check_powerups(game_state):
                die(game_state, screen, menu)