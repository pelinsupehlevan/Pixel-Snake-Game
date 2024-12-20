import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPACE_SIZE = 50





class Food:
    def __init__(self):
        self.coordinates = [
            random.randint(0, int(GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE,
            random.randint(0, int(GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE
        ]