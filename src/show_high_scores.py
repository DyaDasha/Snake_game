import pygame

from globals import WIDTH, TEXT_COLOUR, HEIGHT, BACKGROUND_COLOUR


# таблица рейтинга


def show_high_scores(game_state):
    font = pygame.font.Font(None, 36)
    text = "High Scores"
    text_surface = font.render(text, True, TEXT_COLOUR)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 4))

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return

        screen.fill(BACKGROUND_COLOUR)
        screen.blit(text_surface, text_rect)

        y_pos = HEIGHT // 3
        for name, score in game_state["high_scores"]:
            score_text = f"{name}: {score}"
            score_surface = font.render(score_text, True, TEXT_COLOUR)
            score_rect = score_surface.get_rect(center=(WIDTH // 2, y_pos))
            screen.blit(score_surface, score_rect)
            y_pos += 50

        pygame.display.flip()