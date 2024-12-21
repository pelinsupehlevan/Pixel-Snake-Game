from tkinter import *


class View:
    def __init__(self, controller):
        self.controller = controller
        self.window = Tk()
        self.window.title("Snake Game")
        self.window.resizable(False, False)

        # Skor etiketi
        self.score_label = Label(self.window, text="Score: 0 | Highscore: 0", font=('consolas', 20))
        self.score_label.pack()

        self.canvas = Canvas(self.window, bg="black", height=self.controller.GAME_HEIGHT, width=self.controller.GAME_WIDTH)
        self.canvas.pack()

        self.window.update()
        self.window.bind('<Escape>', lambda event: self.controller.toggle_pause())

        window_width = self.window.winfo_width()
        window_height = self.window.winfo_height()
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2) - (window_height / 2))
        self.window.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.window.bind('<Left>', lambda event: self.controller.change_direction('left'))
        self.window.bind('<Right>', lambda event: self.controller.change_direction('right'))
        self.window.bind('<Up>', lambda event: self.controller.change_direction('up'))
        self.window.bind('<Down>', lambda event: self.controller.change_direction('down'))

    def update_score(self, score, high_score):
        """Skor ve yüksek skoru güncelle."""
        self.score_label.config(text=f"Score: {score} | Highscore: {high_score}")

    def clear_canvas(self):
        """Oyun alanını temizle."""
        self.canvas.delete(ALL)

    def draw_snake(self, snake):
        """Yılanı çiz."""
        for x, y in snake.coordinates:
            self.canvas.create_rectangle(x, y, x + self.controller.SPACE_SIZE, y + self.controller.SPACE_SIZE, fill="#00FF00", tag="snake")

    def draw_food(self, food):
        """Yiyeceği çiz."""
        x, y = food.coordinates
        self.canvas.create_oval(x, y, x + self.controller.SPACE_SIZE, y + self.controller.SPACE_SIZE, fill="#FF0000", tag="food")

        

    def show_game_over(self, on_menu_callback, restart_game_callback):
        """GAME OVER ekranını göster."""
        self.canvas.create_text(self.canvas.winfo_width() / 2, self.canvas.winfo_height() / 2 - 100,
                                font=('consolas', 50), text="GAME OVER", fill="red", tag="gameover")
        
        
        button_spacing = 88
        
        
        Button(self.window, text="Return to Menu", font=('consolas', 20),width=15,
               command=on_menu_callback).place(relx=0.5, rely=0.5, anchor="center", y=button_spacing)
        
        Button(self.window, text="Restart", font=('consolas', 20),width=15,
               command=restart_game_callback).place(relx=0.5, rely=0.5, anchor="center", y=0)
        
    def show_pause_menu(self, resume_callback, restart_callback, return_to_menu_callback):
        """Display the pause menu."""
        self.pause_overlay = Frame(self.window, bg="black")
        self.pause_overlay.place(relx=0.5, rely=0.5, anchor="center")

        Label(self.pause_overlay, text="PAUSED", font=("consolas", 50), fg="yellow", bg="black").pack(pady=20)

        Button(self.pause_overlay, text="Resume", font=("consolas", 20), command=resume_callback).pack(pady=10)
        Button(self.pause_overlay, text="Restart", font=("consolas", 20), command=restart_callback).pack(pady=10)
        Button(self.pause_overlay, text="Return to Menu", font=("consolas", 20), command=return_to_menu_callback).pack(pady=10)

    def hide_pause_menu(self):
        """Remove the pause menu."""
        self.pause_overlay.destroy()


    def hide_pause_menu(self):
        """Pause menüsünü gizle."""
        self.pause_overlay.destroy()

