import tkinter as tk

def createBoard():
    global board
    board = [["R", "k", "B", "Q", "K", "B", "k", "R"],
             ["P", "P", "P", "P", "P", "P", "P", "P"],
             [" ", " ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " ", " "],
             ["P", "P", "P", "P", "P", "P", "P", "P"],
             ["R", "k", "B", "Q", "K", "B", "k", "R"]
             ]
    
def pos(notation):
    file_to_col = {'A': 0, 'B': 1, 'C': 2, 'D': 3,
                   'E': 4, 'F': 5, 'G': 6, 'H': 7}
    col = file_to_col[notation[0].upper()]
    row = 8 - int(notation[1])  # Row 1 is bottom → index 7
    return row, col


def printBoard():
    global board
    for row in board:
        print(row)

createBoard()
printBoard()
print(board[pos("B3")[0]][pos("B3")[1]])