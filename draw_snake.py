import pygame

from globals import BLOCK_SIZE, WALL_BLOCK, SNAKE_RADIUS

# рисуем змею на поле


def draw_snake(screen, game_state):
    for segment in game_state['snake']:
        x = segment[0] * BLOCK_SIZE + WALL_BLOCK * BLOCK_SIZE
        y = segment[1] * BLOCK_SIZE + WALL_BLOCK * BLOCK_SIZE
        rect = ((x, y), (BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(screen, game_state["snake_color"], rect, border_radius=SNAKE_RADIUS)