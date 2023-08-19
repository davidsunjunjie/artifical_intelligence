# I need the basic GUI that I can play the tic-tac-toe and my opposite can play too 
# I need the logic behind the tic-tac-toe

#Part One: 

import tkinter as tk
from tkinter import messagebox
root = tk.Tk()

root.title("Tic Tac Toe")



buttons = [[None for _ in range(3)] for _ in range(3)]

current_player = "X"


def on_button_click(i,j):
    global current_player
    if buttons[i][j]['text'] == "" and current_player == "X":
        buttons[i][j]['text'] = "X" # if there is not occupied and then there should be X 
        current_player = "O"  # and the current player changed into O because it takes turn 
    elif buttons[i][j]['text'] == "" and current_player == "O":
        buttons[i][j]['text'] = "O"
        current_player = "X"
    check_winner() # each turn need to check there is winner or not 

def check_winner():
    for i in range(3):
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != "":
            declare_winner(buttons[i][0]['text'])
        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != "":
            declare_winner(buttons[0][i]['text'])
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        declare_winner(buttons[0][0]['text'])
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        declare_winner(buttons[0][2]['text'])



def declare_winner(winner):
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(state=tk.DISABLED)
    messagebox.showinfo("Tic Tac Toe", f"Player {winner} wins!")


def reset_game():
    global current_player
    for i in range(3):
        for j in range(3):
            buttons[i][j]['text'] = ""
            buttons[i][j].config(state=tk.NORMAL)
    current_player = "X"


for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text="", width=10, height=3, command=lambda i=i, j=j: on_button_click(i, j))
        buttons[i][j].grid(row=i,column=j)

# Add the reset button
reset_button = tk.Button(root, text="Reset Game", command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3)

root.mainloop()
