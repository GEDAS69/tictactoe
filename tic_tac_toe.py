import tkinter as tk
from tkinter import messagebox
import game_io
from scoreboard import Scoreboard
from reset_button import ResetButton

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.current_player = 'X'
        self.board = [[' ']*3 for _ in range(3)]
        self.buttons = [[None]*3 for _ in range(3)]
        self.scoreboard = Scoreboard(self.master)
        self.reset_button = ResetButton(self.master, self.scoreboard, self)
        self.create_board()
        self.configure_grid()
        self.load_game_state()

        self.scoreboard.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
        self.reset_button.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

    def create_board(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.master, text='', font=('Corbel', 20), width=5, height=2, 
                                   command=lambda row=i, col=j: self.on_click(row, col))
                button.grid(row=i+1, column=j, padx=10, pady=10)
                self.buttons[i][j] = button

    def configure_grid(self):
        for i in range(4):
            self.master.grid_rowconfigure(i, weight=1)
            self.master.grid_columnconfigure(i, weight=1)

    def on_click(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Winner!", f"Player {self.current_player} wins!")
                self.scoreboard.update_score(self.current_player)
                self.reset_board()
            elif self.check_draw():
                messagebox.showinfo("Draw!", "It's a draw!")
                self.reset_board()
            else:
                self.switch_player()
            self.save_game_state()

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True
        return False
    
    def check_draw(self):
        for row in self.board:
            for cell in row:
                if cell == ' ':
                    return False
        return True    

    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = ' '
                self.buttons[i][j].config(text = ' ')
        self.current_player = 'X'

    def save_game_state(self):
        game_io.save_game_state('tictactoe_save.json', self.current_player, self.board)

    def load_game_state(self):
        current_player, board = game_io.load_game_state('tictactoe_save.json')
        if current_player is not None and board is not None:
            self.current_player = current_player
            self.board = board
            for i in range(3):
                for j in range(3):
                    self.buttons[i][j].config(text=self.board[i][j])

def main():
    root = tk.Tk()
    root.geometry("300x380")
    game = TicTacToe(root)
    root.mainloop()
    
if __name__ == "__main__":
    main()
