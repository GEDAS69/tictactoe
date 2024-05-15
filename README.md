# Coursework report: Tic Tac Toe Game in Python

## 1. Introduction

### Application description

The Tic-Tac-Toe game is a classic two-player game where players take turns marking spaces in a 3x3 grid. The objective of the game is to get 3 symbols ('X' or 'O') in a row, column, or diagonal.

### How to run the program

To run the program, ensure you have Python installed on your system. Then download the files from the GitHub repository. Using the interpreter of your choice, open the Python file ('tic_tac_toe.py'). Enjoy!

### How to use the program

Once the program is open, an interface will apear. There players can take turns clicking on empty spaces on the 3x3 grid to place their symbol ('X' or 'O'). The game will indicate the result of the game when it ends (eg. 'Draw', 'Player X wins' or 'Player O wins').

## 2. Body/Analysis

### Polymorphism:

In my code, polymorphism is used indirectly due to the use of inheritance from the 'tk.Button' class in the 'ResetButton' class. The 'ResetButton' class inherits from 'tk.Button', and it defines it's own behavior for the 'reset_board()' method, which is invoked when the button is clicked.

### Encapsulation:

Encapsulation is observed in the classes where data (attributes) and functionality (methods) are bundled together. For instance, the 'Scoreboard' class encapsulates score-related data and methods.

```import tkinter as tk

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
```

### Inheritance:

Inheritance is used where certain classes inherit properties and methods from parent classes. For example, the 'ResetButton' class inherits from the 'tk.Button' class, leveraging its functionality while extending it with additional features.

### Encapsulation:

Encapsulation helps in hiding the internal state and implementation details of the Scoreboard class, providing a controlled interface for interacting with it. This approach protects the internal state from unintended or harmful modifications from outside the class.

### Design Patterns:

### Singleton:

Although not explicitly implemented, the TicTacToe class acts in a way similar to a singleton in that there is only one instance of the game being managed at a time. This ensures a single source of truth for the game state.

### Command pattern:

The command pattern is exemplified in the ResetButton class, where the button is configured with a command (self.reset_scores). This pattern decouples the sender (button press) from the action that needs to be performed (resetting the scores and board).

## 3. Results and summary

The Tic Tac Toe program successfully integrates object-oriented principles such as encapsulation and inheritance to create a robust and maintainable application with a user-friendly GUI using Tkinter.

Implementing the reset button functionality to reset scores required careful coordination between the ResetButton, Scoreboard, and TicTacToe classes to ensure proper encapsulation and interaction.

One of the challenges faced was managing the dependencies and ensuring the correct instantiation of objects, especially when passing references between classes, which was resolved by accurately defining and initializing the required parameters.

### Key findings and outcomes

During the coursework I successfully developed a fully functional Tic Tac Toe game using Python's Tkinter library, showcasing effective use of object-oriented programming principles. The program features a clean GUI, along with a scoreboard and reset functionality, enhancing the user experience by maintaining and displaying game scores and allowing easy game resets.

The main result of this work is a robust and maintanable Tic Tac Toe applicaction that can be easily extended and modified.





