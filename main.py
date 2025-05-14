import tkinter as tk

class ChessBoard:

    def __init__(self):
        self.board = [["R", "k", "B", "Q", "K", "B", "k", "R"],
                ["P", "P", "P", "P", "P", "P", "P", "P"],
                [" ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " "],
                ["P", "P", "P", "P", "P", "P", "P", "P"],
                ["R", "k", "B", "Q", "K", "B", "k", "R"]
                ]
        self.file_to_col = {'A': 0, 'B': 1, 'C': 2, 'D': 3,
                            'E': 4, 'F': 5, 'G': 6, 'H': 7
                            }
    
    def __call__(self, notation=None):
        if notation == None:
            result = ""
            for row in self.board:
                result += " ".join(row) + "\n"
            
            return result.rstrip("\n")
        else:
            col = self.file_to_col[notation[0].upper()]
            row = 8 - int(notation[1])
            return (self.board[row][col])
        
    def set(self, notation, piece):
        col = self.file_to_col[notation[0].upper()]
        row = 8 - int(notation[1])
        self.board[row][col] = piece



board = ChessBoard()
print(board())