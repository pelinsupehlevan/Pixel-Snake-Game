import random
from view.View import View, GAME_WIDTH, GAME_HEIGHT, SPACE_SIZE

class Food:
    def __init__(self):
        self.coordinates = [
            random.randint(0, int(GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE,
            random.randint(0, int(GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE
        ]