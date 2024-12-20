from model.Snake import Snake
from model.Food import Food, GAME_WIDTH, GAME_HEIGHT, SPACE_SIZE
from view.View import View



class Controller:
    def __init__(self):
        self.GAME_WIDTH = GAME_WIDTH
        self.GAME_HEIGHT = GAME_HEIGHT
        self.SPACE_SIZE = SPACE_SIZE
        self.SPEED = 70
        self.score = 0
        self.direction = 'down'

        self.snake = Snake()
        self.food = Food()
        self.view = View(self)

        self.view.draw_snake(self.snake)
        self.view.draw_food(self.food)

        self.next_turn()

        self.view.window.mainloop()

    def next_turn(self):
        x, y = self.snake.coordinates[0]

        if self.direction == "up":
            y -= self.SPACE_SIZE
        elif self.direction == "down":
            y += self.SPACE_SIZE
        elif self.direction == "left":
            x -= self.SPACE_SIZE
        elif self.direction == "right":
            x += self.SPACE_SIZE

        self.snake.coordinates.insert(0, (x, y))

        if x == self.food.coordinates[0] and y == self.food.coordinates[1]:
            self.score += 1
            self.view.update_score(self.score)
            self.food = Food()
            self.view.draw_food(self.food)
        else:
            del self.snake.coordinates[-1]

        if self.check_collisions():
            self.view.clear_canvas()
            self.view.show_game_over()
        else:
            self.view.clear_canvas()
            self.view.draw_snake(self.snake)
            self.view.draw_food(self.food)
            self.view.window.after(self.SPEED, self.next_turn)

    def change_direction(self, new_direction):
        if new_direction == 'left' and self.direction != 'right':
            self.direction = new_direction
        elif new_direction == 'right' and self.direction != 'left':
            self.direction = new_direction
        elif new_direction == 'up' and self.direction != 'down':
            self.direction = new_direction
        elif new_direction == 'down' and self.direction != 'up':
            self.direction = new_direction

    def check_collisions(self):
        x, y = self.snake.coordinates[0]

        if x < 0 or x >= self.GAME_WIDTH or y < 0 or y >= self.GAME_HEIGHT:
            return True

        for body_part in self.snake.coordinates[1:]:
            if x == body_part[0] and y == body_part[1]:
                return True

        return False


