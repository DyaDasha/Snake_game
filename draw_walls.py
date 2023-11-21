import pygame

from globals import WALL_COLOUR, WALL_BLOCK, BLOCK_SIZE, WIDTH, HEIGHT

# рисуем стены на поле


def draw_walls(screen):
    pygame.draw.rect(screen, WALL_COLOUR, ((0, 0), (WIDTH, WALL_BLOCK * BLOCK_SIZE)))
    pygame.draw.rect(screen, WALL_COLOUR, ((0, 0), (WALL_BLOCK * BLOCK_SIZE, HEIGHT)))
    pygame.draw.rect(screen, WALL_COLOUR, ((0, HEIGHT - WALL_BLOCK * BLOCK_SIZE), (WIDTH, HEIGHT)))
    pygame.draw.rect(screen, WALL_COLOUR, ((WIDTH - WALL_BLOCK * BLOCK_SIZE, 0), (WIDTH, HEIGHT)))