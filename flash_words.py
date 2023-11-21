import time

import pygame


# строка, которая вызывается после смерти


def flash_words(screen, message):
    words = message.split()
    font = pygame.font.SysFont(None, 48)

    for word in words:
        screen.fill('#000000')  # отчищаем экран
        text = font.render(word, True, "#ffffff")
        text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        screen.blit(text, text_rect)
        pygame.display.flip()  # обновляем экран
        time.sleep(0.25)  # промежуток времени между словами
