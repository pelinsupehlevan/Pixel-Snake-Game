from model.Snake import Snake
from model.Food import Food
from view.View import View, GAME_WIDTH, GAME_HEIGHT, SPACE_SIZE
from PIL import Image, ImageTk
import tkinter as tk


class Menu:
    def __init__(self, root, start_game_callback):
        self.root = root
        self.start_game_callback = start_game_callback
        self.menu_frame = None
        self.difficulty_frame = None
        self.high_score = 0
        self.high_score_label = None

        self.setup_window()
        self.setup_main_menu()

    def setup_window(self):
        self.root.geometry(f"{GAME_WIDTH}x{GAME_HEIGHT}")
        self.root.resizable(False, False)

    def setup_main_menu(self):
        self.clear_frames()

        self.menu_frame = tk.Frame(self.root)
        self.menu_frame.pack(fill="both", expand=True)

        # Background image for the main menu
        original_image = Image.open("assets/MENU_BG.png")
        resized_image = original_image.resize((GAME_WIDTH, GAME_HEIGHT), Image.LANCZOS)
        bg_image = ImageTk.PhotoImage(resized_image)
        bg_label = tk.Label(self.menu_frame, image=bg_image)
        bg_label.image = bg_image
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Centered content frame
        content_frame = tk.Frame(self.menu_frame, bg="#101010")
        content_frame.place(relx=0.5, rely=0.65, anchor="center")  # Adjusted Y-axis position

        # High Score Label
        self.high_score_label = tk.Label(
            content_frame,
            text=f"High Score: {self.high_score}",
            font=("Consolas", 20, "bold"),
            fg="white",
            bg="#101010",
        )
        self.high_score_label.pack(pady=10)

        # Start Game Button
        start_button = tk.Button(
            content_frame,
            text="START GAME",
            font=("Consolas", 20, "bold"),
            bg="#ff39d7",
            fg="white",
            activebackground="#ff39a9",
            activeforeground="white",
            command=self.setup_difficulty_menu,
        )
        start_button.pack(pady=10)

        # Exit Button
        exit_button = tk.Button(
            content_frame,
            text="EXIT",
            font=("Consolas", 20, "bold"),
            bg="#fdff60",
            fg="black",
            activebackground="#ffe760",
            activeforeground="black",
            command=self.root.quit,
        )
        exit_button.pack(pady=10)

    def setup_difficulty_menu(self):
        self.clear_frames()

        self.difficulty_frame = tk.Frame(self.root)
        self.difficulty_frame.pack(fill="both", expand=True)

        # Background image for difficulty menu
        original_image = Image.open("assets/DIFF_BG.png")
        resized_image = original_image.resize((GAME_WIDTH, GAME_HEIGHT), Image.LANCZOS)
        bg_image = ImageTk.PhotoImage(resized_image)
        bg_label = tk.Label(self.difficulty_frame, image=bg_image)
        bg_label.image = bg_image
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Difficulty Title
        title = tk.Label(
            self.difficulty_frame,
            text="SELECT DIFFICULTY",
            font=("Consolas", 30, "bold"),
            fg="white",
            bg="#101010",
        )
        title.pack(pady=20)

        # Easy Button
        tk.Button(
            self.difficulty_frame,
            text="EASY",
            font=("Consolas", 20, "bold"),
            bg="#ff51dc",
            fg="white",
            activebackground="#fdff60",
            activeforeground="black",
            bd=3,
            relief="ridge",
            width=10,
            height=2,
            command=lambda: self.start_game_callback("Easy"),
        ).pack(pady=10)

        # Medium Button
        tk.Button(
            self.difficulty_frame,
            text="MEDIUM",
            font=("Consolas", 20, "bold"),
            bg="#ff39a9",
            fg="white",
            activebackground="#fdff60",
            activeforeground="black",
            bd=3,
            relief="ridge",
            width=10,
            height=2,
            command=lambda: self.start_game_callback("Medium"),
        ).pack(pady=10)

        # Hard Button
        tk.Button(
            self.difficulty_frame,
            text="HARD",
            font=("Consolas", 20, "bold"),
            bg="#ff397a",
            fg="white",
            activebackground="#fdff60",
            activeforeground="black",
            bd=3,
            relief="ridge",
            width=10,
            height=2,
            command=lambda: self.start_game_callback("Hard"),
        ).pack(pady=10)

    def update_high_score(self, score):
        if score > self.high_score:
            self.high_score = score
            if self.high_score_label:
                self.high_score_label.config(text=f"High Score: {self.high_score}")

    def clear_frames(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    Menu(root, lambda difficulty: print(f"Selected difficulty: {difficulty}"))
    root.mainloop()
