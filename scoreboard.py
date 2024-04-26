import tkinter as tk
import game_io
from reset_button import ResetButton

class Scoreboard(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.x_score = 0
        self.o_score = 0
        self.x_label = tk.Label(self, text="X: 0", font=('Corbel', 14))
        self.o_label = tk.Label(self, text="O: 0", font=('Corbel', 14))
        self.reset_button = ResetButton(self.master, self)  # Pass self as the parent widget and also the scoreboard
        
        self.x_label.grid(row=0, column=0, padx=5, pady=5)
        self.o_label.grid(row=0, column=1, padx=5, pady=5)
        self.reset_button.grid(row=0, column=2, padx=5, pady=5)
        
        self.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.load_scores()

    def load_scores(self):
        x_score, o_score = game_io.load_scores('scores.json')
        if x_score is not None:
            self.x_score = x_score
            self.o_score = o_score
            self.update_score_labels()

    def update_score(self, winner):
        if winner == 'X':
            self.x_score += 1
        elif winner == 'O':
            self.o_score += 1
        self.update_score_labels()
        self.save_scores()

    def update_score_labels(self):
        self.x_label.config(text=f"X: {self.x_score}")
        self.o_label.config(text=f"O: {self.o_score}")

    def save_scores(self):
        game_io.save_scores('scores.json', self.x_score, self.o_score)