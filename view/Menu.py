from tkinter import *


class Menu:
    def __init__(self, controller):
        self.controller = controller
        self.window = Tk()
        self.window.title("Snake Game - Menu")
        self.window.resizable(False, False)

        # Center the menu window
        window_width = 400
        window_height = 300
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2) - (window_height / 2))
        self.window.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Title Label
        title_label = Label(self.window, text="Snake Game", font=('consolas', 30, 'bold'), fg="green")
        title_label.pack(pady=20)

        # Difficulty Buttons
        Button(self.window, text="Kolay", font=('consolas', 20), width=10, command=lambda: self.start_game(150)).pack(pady=10)
        Button(self.window, text="Orta", font=('consolas', 20), width=10, command=lambda: self.start_game(100)).pack(pady=10)
        Button(self.window, text="Zor", font=('consolas', 20), width=10, command=lambda: self.start_game(40)).pack(pady=10)

        # Exit Button
        Button(self.window, text="Çıkış", font=('consolas', 15), width=10, command=self.window.quit).pack(pady=20)

        # Start Tkinter mainloop
        self.window.mainloop()

    def start_game(self, speed):
        self.controller.set_speed(speed)  # Set the game speed based on difficulty
        self.window.destroy()  # Close the menu window
        self.controller.start_game()  # Start the game
