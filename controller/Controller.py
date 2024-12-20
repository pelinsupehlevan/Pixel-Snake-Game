from model.Snake import Snake
from model.Food import Food, GAME_WIDTH, GAME_HEIGHT, SPACE_SIZE
from view.View import View
from view.Menu import Menu


class Controller:
    def __init__(self):
        self.GAME_WIDTH = GAME_WIDTH
        self.GAME_HEIGHT = GAME_HEIGHT
        self.SPACE_SIZE = SPACE_SIZE
        self.SPEED = 100  # Varsayılan hız
        self.score = 0
        self.high_score = 0  # Oturumdaki yüksek skor
        self.direction = 'down'

        # Menü ekranını başlat
        self.menu = Menu(self)

    def set_speed(self, speed):
        """Zorluk seviyesine göre hızı ayarla."""
        self.SPEED = speed

    def start_game(self):
        """Oyunu başlat ve yeni yılan/yiyecek oluştur."""
        self.reset_game_variables()  # Değişkenleri sıfırla
        self.snake = Snake()  # Yeni yılan oluştur
        self.food = Food()  # Yeni yiyecek oluştur
        self.view = View(self)  # Oyun ekranını oluştur

        # Skoru sıfırla ve güncelle
        self.view.update_score(self.score, self.high_score)

        # Yılan ve yiyeceği çizin
        self.view.draw_snake(self.snake)
        self.view.draw_food(self.food)

        # Oyun döngüsünü başlat
        self.next_turn()

        # Pencereyi açık tut
        self.view.window.mainloop()

    def next_turn(self):
        """Oyun döngüsünü yönet."""
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
            self.view.show_game_over(self.return_to_menu)
        else:
            self.view.clear_canvas()
            self.view.draw_snake(self.snake)
            self.view.draw_food(self.food)
            self.view.window.after(self.SPEED, self.next_turn)

    def change_direction(self, new_direction):
        """Yön değişikliği kontrolü."""
        if new_direction == 'left' and self.direction != 'right':
            self.direction = new_direction
        elif new_direction == 'right' and self.direction != 'left':
            self.direction = new_direction
        elif new_direction == 'up' and self.direction != 'down':
            self.direction = new_direction
        elif new_direction == 'down' and self.direction != 'up':
            self.direction = new_direction

    def check_collisions(self):
        """Çarpışma kontrolü."""
        x, y = self.snake.coordinates[0]

        if x < 0 or x >= self.GAME_WIDTH or y < 0 or y >= self.GAME_HEIGHT:
            return True

        for body_part in self.snake.coordinates[1:]:
            if x == body_part[0] and y == body_part[1]:
                return True

        return False

    def reset_game_variables(self):
        """Oyun değişkenlerini sıfırla."""
        self.score = 0
        self.direction = 'down'

    def return_to_menu(self):
        """Menü ekranına dön."""
        self.view.window.destroy()  # Oyun penceresini kapat
        self.menu = Menu(self)  # Menü ekranını tekrar aç


if __name__ == "__main__":
    Controller()
