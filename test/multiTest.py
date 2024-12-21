import unittest
from unittest.mock import MagicMock, patch
from controller.Controller import Controller
from model.Snake import Snake
from model.Food import Food

# tkinter ve View sınıflarını mockluyoruz
@patch("tkinter.Tk", new=MagicMock)
@patch("view.View.View", new=MagicMock)
class TestMainMenu(unittest.TestCase):
    @patch("controller.Controller.Menu")
    def setUp(self, MockMenu):
        MockMenu.return_value = MagicMock()
        self.controller = Controller()

    def test_main_menu_buttons(self):
        """Verify that the main menu shows all the required buttons."""
        self.controller.menu.get_buttons.return_value = ["Easy", "Medium", "Hard"]
        buttons = self.controller.menu.get_buttons()
        self.assertIn("Easy", buttons)
        self.assertIn("Medium", buttons)
        self.assertIn("Hard", buttons)

@patch("tkinter.Tk", new=MagicMock)
@patch("view.View.View", new=MagicMock)
class TestGameLogic(unittest.TestCase):
    @patch("controller.Controller.Menu")
    def setUp(self, MockMenu):
        MockMenu.return_value = MagicMock()
        self.controller = Controller()
        self.controller.snake = Snake()
        self.controller.food = Food()

    def test_snake_movement(self):
        """Test snake's movement logic."""
        self.controller.change_direction("Up")
        self.assertEqual(self.controller.direction, "Up")

    def test_snake_eats_food(self):
        """Test that snake eats food and grows."""
        initial_length = len(self.controller.snake.coordinates)
        self.controller.snake.coordinates[0] = self.controller.food.coordinates
        self.controller.next_turn()
        self.assertEqual(len(self.controller.snake.coordinates), initial_length + 1)

    def test_game_over(self):
        """Test game over logic when snake hits wall."""
        self.controller.snake.coordinates[0] = (-1, -1)  # Simulate wall collision
        self.controller.next_turn()
        self.controller.view.show_game_over.assert_called_once()

if __name__ == "__main__":
    unittest.main()
