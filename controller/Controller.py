from model.Snake import Snake
from model.Food import Food
from view.View import View, GAME_WIDTH, GAME_HEIGHT, SPACE_SIZE
from view.Menu import Menu
import tkinter as tk



class Controller:
    def __init__(self):
        self.GAME_WIDTH = GAME_WIDTH
        self.GAME_HEIGHT = GAME_HEIGHT
        self.SPACE_SIZE = SPACE_SIZE
        self.SPEED = 100  
        self.score = 0
        self.high_score = 0 
        self.direction = 'down'
        self.paused = False

        self.root = tk.Tk()
        self.menu = Menu(self.root, self.start_game_from_menu)
        self.root.mainloop()

    def set_speed(self, speed):
        self.SPEED = speed

    def start_game_from_menu(self, difficulty):
        if difficulty == "Easy":
            self.set_speed(150)
        elif difficulty == "Medium":
            self.set_speed(100)
        elif difficulty == "Hard":
            self.set_speed(50)

        self.root.destroy()
        self.start_game()

    def start_game(self):
        self.reset_game_variables() 
        self.snake = Snake() 
        self.food = Food()
        self.view = View(self)  

        self.view.update_score(self.score, self.high_score)

        self.view.draw_snake(self.snake)
        self.view.draw_food(self.food)

        self.next_turn()

        self.view.window.mainloop()

    def next_turn(self):
        if self.paused: 
            return
        
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
            if self.score > self.high_score:
                self.high_score = self.score

            self.view.update_score(self.score, self.high_score)
            self.food = Food()
            self.view.draw_food(self.food)
        else:
            del self.snake.coordinates[-1]

        if self.check_collisions():        
            self.view.clear_canvas()
            self.view.show_game_over(self.return_to_menu, self.restart_game)
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

    def reset_game_variables(self):
        self.score = 0
        self.direction = 'down'

    def toggle_pause(self):
        if not self.paused:
            self.paused = True
            self.view.show_pause_menu(self.resume_game, self.restart_game, self.return_to_menu)
        else:
            self.resume_game()
    
    def resume_game(self):
        self.paused = False  
        self.view.hide_pause_menu() 
        self.next_turn() 
    
    def restart_game(self):
        self.view.window.destroy() 
        self.paused = False  
        self.start_game()  

    def return_to_menu(self):
        self.view.window.destroy()  
        self.paused = False 
        self.root = tk.Tk()
        self.menu = Menu(self.root, self.start_game_from_menu)
        self.root.mainloop()


if __name__ == "__main__":
    Controller()
