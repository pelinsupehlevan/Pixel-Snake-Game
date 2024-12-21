import unittest
from model.Food import Food
from view.View import GAME_WIDTH, GAME_HEIGHT, SPACE_SIZE

class TestFood(unittest.TestCase):
    def setUp(self):
        self.food = Food()

    def test_food_position_within_bounds(self):
        """Test that food is generated within game boundaries."""
        x, y = self.food.coordinates
        self.assertTrue(0 <= x < GAME_WIDTH)
        self.assertTrue(0 <= y < GAME_HEIGHT)
        self.assertEqual(x % SPACE_SIZE, 0)
        self.assertEqual(y % SPACE_SIZE, 0)

if __name__ == "__main__":
    unittest.main()
