import unittest
import os
from controller.Controller import Controller
from model.Snake import Snake
from model.Food import Food

class TestController(unittest.TestCase):
    def setUp(self):
        # Çalışma dizinini projenin köküne ayarlıyoruz
        os.chdir(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

        self.controller = Controller()
        self.controller.snake = Snake()
        self.controller.food = Food()

    def test_initial_score(self):
        """Test that the initial score is 0."""
        self.assertEqual(self.controller.score, 0)

    def test_score_increase(self):
        """Test that score increases correctly when the snake eats food."""
        self.controller.score = 5
        self.controller.snake.coordinates[0] = self.controller.food.coordinates  # Simulate eating food
        self.controller.next_turn()
        self.assertEqual(self.controller.score, 6)

if __name__ == "__main__":
    unittest.main()
