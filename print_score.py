import pygame

from globals import TEXT_COLOUR, WALL_BLOCK, BLOCK_SIZE
from pad import left_pad_with_zeros


def print_score(screen, game_state):
    font = pygame.font.SysFont("Courier New", 24, bold=True)  # font
    text = font.render(
        "Score: " + left_pad_with_zeros(str(game_state["score"]), 4) + "    Mult: " + str(
            round(game_state["mult"], 2)), True,
        TEXT_COLOUR)
    text_rect = text.get_rect()
    text_rect.topleft = (WALL_BLOCK * BLOCK_SIZE, 0)
    screen.blit(text, text_rect)