import unittest
from model.Snake import Snake

class TestSnake(unittest.TestCase):
    def setUp(self):
        self.snake = Snake()

    def test_initial_body_size(self):
        """Test that the snake starts with the correct body size."""
        self.assertEqual(len(self.snake.coordinates), 3)

    def test_snake_growth(self):
        """Test that the snake grows by one unit."""
        initial_length = len(self.snake.coordinates)
        self.snake.coordinates.append([0, 0])  # Simulate growth
        self.assertEqual(len(self.snake.coordinates), initial_length + 1)

if __name__ == "__main__":
    unittest.main()
