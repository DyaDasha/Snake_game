import pygame

from globals import SNAKE_ICON


def initialize_snake(screen_size):  # инициализация приложения
    pygame.init()
    screen = pygame.display.set_mode(screen_size)  # создание дисплея
    icon = pygame.image.load(SNAKE_ICON)
    pygame.display.set_icon(icon)  # создаю иконку
    pygame.display.set_caption("ArcadeSnake")  # название игры
    clock = pygame.time.Clock()  # обновляю fps
    return screen, clock
