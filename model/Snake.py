BODY_PARTS = 3

class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        for i in range(BODY_PARTS):
            self.coordinates.append([0, 0])