# загружаю уровень

def load_level(game_state):
    with open('levels/' + game_state['level_selected']) as file:
        level = [list(line.rstrip('\n')) for line in file]
    print(level)
    for y, row in enumerate(level):
        for x, tile in enumerate(row):
            if tile == 'W':
                game_state["powerups"].append((x, y, 4, -1))
                print('Adding wall')
            elif tile == 'A':
                game_state["powerups"].append((x, y, 0, -1))
            elif tile == 'M':
                game_state["powerups"].append((x, y, 3, -1))
                print('Adding mine')
            elif tile == 'D':
                game_state["powerups"].append((x, y, 1, -1))
                print('Adding doubler')
