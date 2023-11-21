import pygame

from globals import BLOCK_SIZE, WALL_BLOCK, POWERUP_IMAGES
# добавление бонусов на поле


def draw_powerups(screen, powerups):
    for powerup in powerups:
        x = powerup[0] * BLOCK_SIZE + WALL_BLOCK * BLOCK_SIZE
        y = powerup[1] * BLOCK_SIZE + WALL_BLOCK * BLOCK_SIZE
        t = powerup[2]
        p = powerup[3]
        shrunk_size = BLOCK_SIZE * abs(p)
        offset = (BLOCK_SIZE - shrunk_size) / 2
        POWERUP_IMAGES[t].set_alpha(255 if p < 0 else 255 * p)
        resized_image = pygame.transform.scale(POWERUP_IMAGES[t], (shrunk_size, shrunk_size))
        rect = ((x + offset, y + offset), (shrunk_size, shrunk_size))
        screen.blit(resized_image, rect)
