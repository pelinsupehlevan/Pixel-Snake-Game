from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPACE_SIZE = 50
FOOD_COLOR = "#FF0000"

class Food:

    def __init__(self):

        x = random.randint(0, int(GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, int(GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")