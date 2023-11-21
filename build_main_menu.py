import sys

import pygame_menu

from set_level import set_level
from set_powerups import set_powerups
from set_snake_color import set_snake_color
from show_high_scores import show_high_scores
from show_powerups import show_powerups
from start_level import start_level

# функция по созданию меню


def build_main_menu(game_state):
    menu = pygame_menu.Menu(width=400, height=400, title='Select Options',
                            theme=pygame_menu.themes.THEME_DARK)

    # кнопка запуска змейки
    menu.add.button('Play', lambda: start_level(game_state, menu))

    # выбор уровня
    menu.add.selector('Level: ', [('Blank', '1-empty.csv'), ('Walls', '2-walls.csv'), ('Mines', '3-mines.csv'),
                                  ('Enemy Lines', '4-enemy-lines.csv'), ('Risk', '6-risk.csv')], onchange=set_level,
                      game_state=game_state)

    # Выбрать цвет змейки
    menu.add.selector('Snake color: ',
                      [('Lichen', '#3ca370'), ('Ochre', '#73275c'), ('Sky', '#00FF00'), ('Sass', '#ff6b97')],
                      onchange=lambda x, y: set_snake_color(x, game_state))

    # включить или выключить бонусы
    menu.add.selector('Powerups: ', [('Enabled', True), ('Disabled', False)], onchange=set_powerups,
                      game_state=game_state)

    menu.add.button('Powerup Gallery', show_powerups, game_state)

    # посмотреть таблицу рекордов
    menu.add.button('High Scores', show_high_scores, game_state)

    # выйти из игры
    menu.add.button('Quit', lambda: sys.exit())

    menu.enable()

    return menu
