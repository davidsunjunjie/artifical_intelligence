import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe vs AI")
        
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(root, text="", width=10, height=3, command=lambda i=i, j=j: self.on_button_click(i, j))
                self.buttons[i][j].grid(row=i,column=j)

        self.reset_button = tk.Button(root, text="Reset Game", command=self.reset_game)
        self.reset_button.grid(row=3, column=0, columnspan=3)

    def on_button_click(self, i, j):
        if self.buttons[i][j]['text'] == "" and self.current_player == "X":
            self.buttons[i][j]['text'] = "X"
            if not self.check_winner():
                self.ai_move()
                self.check_winner()

    def ai_move(self):
        empty_cells = [(i, j) for i in range(3) for j in range(3) if self.buttons[i][j]['text'] == ""]
        if empty_cells:
            i, j = random.choice(empty_cells)
            self.buttons[i][j]['text'] = "O"

    def check_winner(self):
        for i in range(3):
            if self.buttons[i][0]['text'] == self.buttons[i][1]['text'] == self.buttons[i][2]['text'] != "":
                self.declare_winner(self.buttons[i][0]['text'])
                return True
            if self.buttons[0][i]['text'] == self.buttons[1][i]['text'] == self.buttons[2][i]['text'] != "":
                self.declare_winner(self.buttons[0][i]['text'])
                return True
        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != "":
            self.declare_winner(self.buttons[0][0]['text'])
            return True
        if self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != "":
            self.declare_winner(self.buttons[0][2]['text'])
            return True
        return False

    def declare_winner(self, winner):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(state=tk.DISABLED)
        messagebox.showinfo("Tic Tac Toe", f"Player {winner} wins!")

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]['text'] = ""
                self.buttons[i][j].config(state=tk.NORMAL)
        self.current_player = "X"

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

