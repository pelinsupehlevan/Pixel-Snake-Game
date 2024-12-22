import unittest
from controller.Controller import Controller

class TestController(unittest.TestCase):
    def setUp(self):
        """Headless modda Controller'ı başlat."""
        self.controller = Controller(headless=True)
        self.controller.start_game()

    def test_main_menu_buttons(self):
        """Ana menü düğmelerinin doğruluğunu kontrol et."""
        self.controller.start_game_from_menu("Easy")
        self.assertEqual(self.controller.SPEED, 150)

        self.controller.start_game_from_menu("Medium")
        self.assertEqual(self.controller.SPEED, 100)

        self.controller.start_game_from_menu("Hard")
        self.assertEqual(self.controller.SPEED, 50)

    def test_difficulty_speeds(self):
        """Zorluk seviyesine göre hız değişimini kontrol et."""
        self.controller.start_game_from_menu("Easy")
        self.assertEqual(self.controller.SPEED, 150)

        self.controller.start_game_from_menu("Medium")
        self.assertEqual(self.controller.SPEED, 100)

        self.controller.start_game_from_menu("Hard")
        self.assertEqual(self.controller.SPEED, 50)

    def test_game_components_loaded(self):
        """Oyun bileşenlerinin doğru yüklendiğini doğrula."""
        self.controller.start_game()
        self.assertIsNotNone(self.controller.snake)
        self.assertIsNotNone(self.controller.food)
        self.assertEqual(self.controller.score, 0)

    def test_snake_movement(self):
        """Yılanın yön kontrolünü test et."""
        self.controller.direction = "right"
        self.controller.next_turn()
        self.assertEqual(self.controller.snake.coordinates[0], (self.controller.SPACE_SIZE, 0))

        self.controller.change_direction("down")
        self.controller.next_turn()
        self.assertEqual(self.controller.snake.coordinates[0], (self.controller.SPACE_SIZE, self.controller.SPACE_SIZE))

    def test_snake_eats_food(self):
        """Yılanın büyümesini ve elma oluşumunu test et."""
        # Yılanın başlangıç pozisyonunu al
        head_x, head_y = self.controller.snake.coordinates[0]

        # Elmayı yılanın bir altındaki kareye yerleştir
        self.controller.food.coordinates = (head_x, head_y + self.controller.SPACE_SIZE)

        # Yılanın başlangıç uzunluğunu al
        initial_length = len(self.controller.snake.coordinates)

        # Hareket ettir ve elma yendiğini kontrol et
        self.controller.next_turn()

        # Uzunluk 1 artmalı
        self.assertEqual(len(self.controller.snake.coordinates), initial_length + 1,
                         "Yılan büyümesi başarısız: Uzunluk artmadı.")

        # Yeni elma koordinatlarının eskisinden farklı olduğunu kontrol et
        self.assertNotEqual(self.controller.food.coordinates, self.controller.snake.coordinates[0],
                            "Yeni elma yılanın kafasıyla çakışıyor.")

    def test_collision_ends_game(self):
        """Çarpışma sonrası oyun sonunu test et."""
        self.controller.snake.coordinates = [(0, 0), (20, 0), (40, 0)]
        self.controller.direction = "left"
        self.controller.next_turn()
        self.assertTrue(self.controller.check_collisions())

    def test_score_increment(self):
        """Skorun doğru arttığını test et."""
        # Yılanın başlangıç pozisyonunu al
        head_x, head_y = self.controller.snake.coordinates[0]

        # Elmayı yılanın bir altındaki kareye yerleştir
        self.controller.food.coordinates = (head_x, head_y + self.controller.SPACE_SIZE)

        # Başlangıç skorunu al
        initial_score = self.controller.score

        # Hareket ettir ve skoru kontrol et
        self.controller.next_turn()

        # Skorun bir arttığını doğrula
        self.assertEqual(self.controller.score, initial_score + 1,
                         "Skor artışı başarısız: Skor beklenenden farklı.")

    def test_pause_game(self):
        """Oyunun duraklatıldığını test et."""
        self.controller.toggle_pause()
        self.assertTrue(self.controller.paused)
        self.controller.toggle_pause()
        self.assertFalse(self.controller.paused)

    def test_resume_and_restart_game(self):
        """Oyunun devam ve yeniden başlatma işlemlerini test et."""
        self.controller.toggle_pause()  # Oyunu duraklat
        self.controller.resume_game()  # Devam et
        self.assertFalse(self.controller.paused, "Oyun duraklatmadan sonra devam etmedi.")

        self.controller.restart_game()  # Yeniden başlat
        self.assertEqual(self.controller.score, 0, "Skor sıfırlanmadı.")
        self.assertEqual(len(self.controller.snake.coordinates), 3,
                         "Yılan başlangıç uzunluğuna dönmedi.")  # Başlangıç uzunluğu

    def test_high_score_session_persistence(self):
        """High score'un doğru güncellenmesini test et."""
        # Başlangıç high_score ve score değerlerini kontrol et
        self.assertEqual(self.controller.high_score, 0, "Başlangıçta high score 0 olmalı.")
        self.assertEqual(self.controller.score, 0, "Başlangıçta score 0 olmalı.")

        # İlk oyunda skor 10, high score güncellenmeli
        self.controller.score = 10
        self.controller.high_score = max(self.controller.high_score, self.controller.score)
        self.assertEqual(self.controller.high_score, 10, "High score ilk oyunda güncellenmedi.")

        # Yeni bir oyun başlatıldığında score sıfırlanmalı, ancak high score korunmalı
        self.controller.reset_game_variables()
        self.assertEqual(self.controller.score, 0, "Yeni oyunda score sıfırlanmadı.")
        self.assertEqual(self.controller.high_score, 10, "Yeni oyunda high score korunmadı.")

        # İkinci oyunda skor 5, high score değişmemeli
        self.controller.score = 5
        self.controller.high_score = max(self.controller.high_score, self.controller.score)
        self.assertEqual(self.controller.high_score, 10, "High score düşük skorda yanlış güncellendi.")

        # Üçüncü oyunda skor 15, high score güncellenmeli
        self.controller.score = 15
        self.controller.high_score = max(self.controller.high_score, self.controller.score)
        self.assertEqual(self.controller.high_score, 15, "High score yüksek skorda doğru güncellenmedi.")


if __name__ == "__main__":
    unittest.main()
