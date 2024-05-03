import unittest
from tkinter import Tk, messagebox
from game_io import save_game_state, load_game_state
from scoreboard import Scoreboard
from reset_button import ResetButton
from tic_tac_toe import TicTacToe

class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.game = TicTacToe(self.root)
        self.scoreboard = Scoreboard(self.root)
        self.reset_button = ResetButton(self.root, self.scoreboard, self.game)

    def test_create_board(self):
        self.assertEqual(len(self.game.buttons), 3)
        for row in self.game.buttons:
            self.assertEqual(len(row), 3)

    def test_configure_grid(self):
        for i in range(4):
            self.root.grid_rowconfigure(i, weight=1)
            self.root.grid_columnconfigure(i, weight=1)

    def test_on_click(self):
        # Test that the on_click method correctly updates the game board and switches the current player
        self.game.on_click(0, 0)
        self.assertEqual(self.game.board[0][0], 'X')
        self.assertEqual(self.game.current_player, 'O')

        # Test that the message box is displayed correctly
        self.game.on_click(0, 0)
        self.game.on_click(0, 1)
        self.game.on_click(0, 2)
        messagebox.showinfo("Winner!", "Player X wins!")
        self.assertEqual(self.scoreboard.update_score('X'), 1)

        # Test that the board is reset correctly
        self.game.reset_board()
        for row in self.game.board:
            for cell in row:
                self.assertEqual(cell, ' ')

    def test_switch_player(self):
        # Test that the switch_player method correctly switches the current player
        self.game.current_player = 'X'
        self.game.switch_player()
        self.assertEqual(self.game.current_player, 'O')

    def test_check_winner(self):
        # Test that the check_winner method correctly identifies a winner
        self.game.board[0][0] = 'X'
        self.game.board[0][1] = 'X'
        self.game.board[0][2] = 'X'
        self.assertTrue(self.game.check_winner())

        # Test that the check_winner method correctly identifies no winner
        self.game.reset_board()
        self.game.board[0][0] = 'X'
        self.game.board[0][1] = 'O'
        self.game.board[0][2] = 'X'
        self.assertFalse(self.game.check_winner())

    def test_check_draw(self):
        # Test that the check_draw method correctly identifies a draw
        for i in range(3):
            for j in range(3):
                if (i+j) % 2 == 0:
                    self.game.board[i][j] = 'X'
                else:
                    self.game.board[i][j] = 'O'
        self.assertTrue(self.game.check_draw())

        # Test that the check_draw method correctly identifies no draw
        self.game.reset_board()
        self.game.board[0][0] = 'X'
        self.game.board[0][1] = 'O'
        self.game.board[0][2] = ' '
        self.assertFalse(self.game.check_draw())

    def test_reset_board(self):
        # Test that the reset_board method correctly resets the board
        self.game.board[0][0] = 'X'
        self.game.reset_board()
        for row in self.game.board:
            for cell in row:
                self.assertEqual(cell, ' ')

    def test_load_game_state(self):
        # Test that the load_game_state method correctly loads the game state
        save_game_state('tictactoe_save.json', 'X', self.game.board)
        loaded_current_player, loaded_board = load_game_state('tictactoe_save.json')
        self.assertEqual(loaded_current_player, 'X')
        for i in range(3):
            for j in range(3):
                self.assertEqual(loaded_board[i][j], self.game.board[i][j])

    def tearDown(self):
        self.root.destroy()

if __name__ == "__main__":
    unittest.main()
