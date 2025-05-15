import tkinter as tk

class ChessBoard:

    def __init__(self):
        self.board = [
                ["R", "N", "B", "Q", "K", "B", "N", "R"],
                ["P", "P", "P", "P", "P", "P", "P", "P"],
                [" ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " "],
                ["P", "P", "P", "P", "P", "P", "P", "P"],
                ["R", "N", "B", "Q", "K", "B", "N", "R"]
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


class piece:
    def __init__(self, name):
        self.name = name
        self.colour = None

    def valid_moves(self):
        pass

class Pawn(piece):
    def __init__(self, colour):
        super().__init__('P', colour)

    def valid_moves(self, position, board):
        row, col = position
        moves = []

        direction = 1 if self.colour == 'white' else -1

        # normal foward 1 move
        if 0 <= row + direction < 8 and board[row + direction][col] == ' ':
            moves.append((row + direction, col))

        # first move double
        if (self.colour == 'white' and row == 6) or (self.colour == 'black' and row == 1):
            if board[row + direction * 2][col] == ' ':
                moves.append((row + direction * 2, col))
        
        # taking diagonal
        if 0 <= row + direction < 8:
            if 0 <= col - 1 < 8 and grid[row + direction][col - 1] != ' ':
                moves.append((row + direction, col - 1))
            if 0 <= col + 1 < 8 and grid[row + direction][col +1] != ' ':
                moves.append((row + direction, col + 1))

        return moves

class Knight(piece):
    def __init__(self, colour):
        super().__init__('N', colour)

    def valid_moves(self, position, board):
        moves = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]

        for move in moves:
            if (not 0 <= move[1] < 8) and (not 0 <= move[0] < 8):
                moves.remove(move)

        return moves


board = ChessBoard()
knight = Knight('white')
print(board())
Knight.valid_moves('C1',board)