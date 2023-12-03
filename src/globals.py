import pygame

BLOCK_SIZE = 20  # размер одного блока
WALL_BLOCK = 3  # размер стены в блоках
WIDTH, HEIGHT = 500, 500  # ширина и высота экрана
SNAKE_ICON = "assets/snake.png"  # иконка приложения
SCREEN_COLOUR = (34, 139, 34)  # цвет окна
BACKGROUND_COLOUR = (0, 0, 0)  # задний фон
INITIAL_GAME_SPEED = 8  # fps
INITIAL_APPLES = 1  # изначальное количество яблок
INITIAL_SNAKE_LENGTH = 3  # изначальная длина змеи
SIZE_X = WIDTH // BLOCK_SIZE - WALL_BLOCK * 2  # размер поля со стенами по x
SIZE_Y = HEIGHT // BLOCK_SIZE - WALL_BLOCK * 2  # размер поля со стенами по y
SNAKE_COLOUR = '#3ca370'  # цвет змеи
SNAKE_RADIUS = BLOCK_SIZE // 4  # радиус сегментов змеи
WALL_COLOUR = (0, 100, 0)  # цвет стен
TEXT_COLOUR = (255, 255, 255)  # цвет текста

# POWERUPS
POWERUP_SPAWN_TIME_MIN = 10  # минимальное время спавна бонуса
POWERUP_SPAWN_TIME_MAX = 30  # максимальное время спавна бонуса
POWERUP_DURATION_MIN = 10  # минимальное время существования бонуса
POWERUP_DURATION_MAX = 30  # максимальное время существование бонуса
POWERUP_IMAGES = [pygame.image.load("assets/plus.png"), pygame.image.load("assets/x2.png"),
                  pygame.image.load("assets/rewind.png"),
                  pygame.image.load("assets/mine.png"),
                  pygame.image.load("assets/wall.png")
                  ]
POWERUP_NAMES = ['EXTRA APPLE', 'MULTIPLIER', 'SLOWDOWN', 'MINE', 'WALL', 'KNIFE']  # имена бонусов
APPLE_IMAGE = pygame.image.load("assets/apple.png")  # картинка яблока
