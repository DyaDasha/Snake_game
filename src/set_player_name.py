import sys

import pygame

from globals import TEXT_COLOUR, HEIGHT, WIDTH, BACKGROUND_COLOUR

# получаем на ввод имя игрока


def get_player_name(screen):
    font = pygame.font.Font(None, 36)
    text = "Enter Your Name:"
    text_surface = font.render(text, True, TEXT_COLOUR)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 4))

    running = True
    input_text = ""

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if input_text == '':
                        return 'YOU'
                    return input_text
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

        screen.fill(BACKGROUND_COLOUR)
        screen.blit(text_surface, text_rect)

        input_surface = font.render(input_text, True, TEXT_COLOUR)
        input_rect = input_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(input_surface, input_rect)

        pygame.display.flip()
    return input_text