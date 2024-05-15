import tkinter as tk

class ResetButton(tk.Button):
    def __init__(self, master, scoreboard, game_instance=None):
        super().__init__(master, text="Reset", font=('Corbel', 14), command=self.reset_scores)
        self.scoreboard = scoreboard
        self.game_instance = game_instance

    def reset_scores(self):
        self.scoreboard.x_score = 0
        self.scoreboard.o_score = 0
        self.scoreboard.update_score_labels()
        self.scoreboard.save_scores()
        if self.game_instance is not None:
            self.game_instance.reset_board() 
