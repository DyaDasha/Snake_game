from globals import BLOCK_SIZE, WALL_BLOCK, APPLE_IMAGE

# добавление яблочек на поле


def draw_apples(screen, apples):
    for apple in apples:
        x = apple[0] * BLOCK_SIZE + WALL_BLOCK * BLOCK_SIZE
        y = apple[1] * BLOCK_SIZE + WALL_BLOCK * BLOCK_SIZE
        rect = ((x, y), (BLOCK_SIZE, BLOCK_SIZE))
        screen.blit(APPLE_IMAGE, rect)
