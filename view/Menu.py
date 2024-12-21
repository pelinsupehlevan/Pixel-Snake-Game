from tkinter import *


class Menu:
    def __init__(self, controller):
        self.controller = controller
        self.window = Tk()
        self.window.title("Snake Game - Menu")
        self.window.resizable(False, False)

        window_width = 800
        window_height = 600
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2) - (window_height / 2))
        self.window.geometry(f"{window_width}x{window_height}+{x}+{y}")

        title_label = Label(self.window, text="Snake Game", font=('consolas', 30, 'bold'), fg="green")
        title_label.pack(pady=20)

        Button(
            self.window,
            text="Easy", 
            font=('consolas', 20), 
            width=10,
            bg="#ff51dc",
            fg="white",
            activebackground="#fdff60",
            activeforeground="black",
            bd=3,
            relief="ridge", 
            command=lambda: self.start_game(150)).pack(pady=10)
        
        Button(
            self.window, 
            text="Medium", 
            font=('consolas', 20), 
            width=10,
            bg="#ff39a9",
            fg="white",
            activebackground="#fdff60",
            activeforeground="black",
            bd=3,
            relief="ridge",            
            command=lambda: self.start_game(100)).pack(pady=10)
        
        Button(
            self.window, 
            text="Hard", 
            font=('consolas', 20), 
            width=10,
            bg="#ff397a",
            fg="white",
            activebackground="#fdff60",
            activeforeground="black",
            bd=3,
            relief="ridge", 
            command=lambda: 
            self.start_game(50)).pack(pady=10)
        
        Button(
            self.window, 
            text="Exit", 
            font=('consolas', 15), 
            width=10,
            bg="#ff51dc",
            fg="white",
            activebackground="#fdff60",
            activeforeground="black",
            bd=3,
            relief="ridge",  
            command=self.window.quit).pack(pady=20)

        self.window.mainloop()

    def start_game(self, speed):
        self.controller.set_speed(speed)  
        self.window.destroy() 
        self.controller.start_game()  
