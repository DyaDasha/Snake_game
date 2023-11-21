import pygame


# инициализация одного из 2х основных массивов игры, смотрим, какие клавиши нажаты


def get_events():
    events = []
    raw = []
    for event in pygame.event.get():
        raw.append(event)
        if event.type == pygame.QUIT:
            events.append("quit")
        elif event.type == pygame.KEYDOWN:  # нажатие кнопки
            if event.key == pygame.K_UP:  # читаем, какая клавиша нажата
                events.append("up")
            elif event.key == pygame.K_DOWN:
                events.append("down")
            elif event.key == pygame.K_LEFT:
                events.append("left")
            elif event.key == pygame.K_RIGHT:
                events.append("right")
            if event.key == pygame.K_SPACE:
                events.append("space")
            if event.key == pygame.K_RETURN:
                events.append("enter")
            if event.key == pygame.K_ESCAPE:
                events.append("escape")
    return events, raw
