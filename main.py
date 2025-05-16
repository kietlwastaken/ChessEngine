import tkinter as tk

class ChessBoard:



    def __init__(self):
        self.board = [
            [Rook("black"), Knight("black"), Bishop("black"), Queen("black"), King("black"), Bishop("black"), Knight("black"), Rook("black")],
            [Pawn("black")] * 8,
            [None] * 8, [None] * 8, [None] * 8, [None] * 8,
            [Pawn("white")] * 8,
            [Rook("white"), Knight("white"), Bishop("white"), Queen("white"), King("white"), Bishop("white"), Knight("white"), Rook("white")]
        ]

        self.file_to_col = {'A': 0, 'B': 1, 'C': 2, 'D': 3,
                            'E': 4, 'F': 5, 'G': 6, 'H': 7
                            }


    def __call__(self, notation=None):
        if notation is None:
            result = "    A B C D E F G H\n"
            result += "  +-----------------+\n"
            for i, row in enumerate(self.board):
                rank = 8 - i
                row_str = " ".join(str(cell) if isinstance(cell, Piece) else '.' for cell in row)
                result += f"{rank} | {row_str} |\n"
            result += "  +-----------------+"
            return result
        else:
            col = self.file_to_col[notation[0].upper()]
            row = 8 - int(notation[1])
            return self.board[row][col]


    def pos(self, notation):
        col = self.file_to_col[notation[0].upper()]
        row = 8 - int(notation[1])
        return (row, col)


    def set(self, notation, piece):
        col = self.file_to_col[notation[0].upper()]
        row = 8 - int(notation[1])
        self.board[row][col] = piece


class Piece:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour

    def __str__(self):
        return self.name.upper() if self.colour == 'white' else self.name.lower()

    def valid_moves(self):
        pass


class Pawn(Piece):
    def __init__(self, colour):
        super().__init__('P', colour)

    def valid_moves(self, position, board):
        row, col = position
        moves = []

        direction = -1 if self.colour == 'white' else 1

        # normal foward 1 move
        if 0 <= row + direction < 8 and board[row + direction][col] == None:
            moves.append((row + direction, col))

        # first move double
        if (self.colour == 'white' and row == 6) or (self.colour == 'black' and row == 1):
            if 0 <= row + direction * 2 < 8 and board[row + direction][col] == None and board[row + direction * 2][col] == None:
                moves.append((row + direction * 2, col))

        # taking diagonal
        if 0 <= row + direction < 8:
            if 0 <= col - 1 < 8 and board[row + direction][col - 1] != None:
                moves.append((row + direction, col - 1))
            if 0 <= col + 1 < 8 and board[row + direction][col +1] != None:
                moves.append((row + direction, col + 1))

        return moves

class Knight(Piece):
    def __init__(self, colour):
        super().__init__('N', colour)

    def valid_moves(self, position, board):
        row, col = position
        moves = []

        # Possible L-shaped moves
        knight_moves = [(-2, -1), (-2, 1), (2, -1), (2, 1), 
                        (-1, -2), (-1, 2), (1, -2), (1, 2)]

        for move in knight_moves:
            new_row = row + move[0]
            new_col = col + move[1]
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                if board[new_row][new_col] == None or board[new_row][new_col].colour != self.colour:
                    moves.append((new_row, new_col))


        return moves

class Bishop(Piece):
    def __init__(self, colour):
        super().__init__('B', colour)

    def valid_moves(self, position, board):
        row, col = position
        moves = []

        # Diagonal moves
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

        for direction in directions:
            for i in range(1, 8):
                new_row = row + direction[0] * i
                new_col = col + direction[1] * i
                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    if board[new_row][new_col] == None:
                        moves.append((new_row, new_col))
                    elif board[new_row][new_col].colour != self.colour:
                        moves.append((new_row, new_col))
                        break
                    else:
                        break
                else:
                    break

        return moves

class Rook(Piece):
    def __init__(self, colour):
        super().__init__('R', colour)

    def valid_moves(self, position, board):
        row, col = position
        moves = []

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for direction in directions:
            for i in range(1,8):
                new_row = row + direction[0] * i
                new_col = col + direction[1] * i
                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    if board[new_row][new_col] == None:
                        moves.append((new_row, new_col))
                    elif board[new_row][new_col].colour != self.colour:
                        moves.append((new_row, new_col))
                        break
                    else:
                        break

        return moves

class Queen(Piece):
    def __init__(self, colour):
        super().__init__('Q', colour)

    def valid_moves(self, position, board):
        row, col = position
        moves = []

        rook = Rook(self.colour)
        bishop = Bishop(self.colour)

        moves.extend(rook.valid_moves(position, board))
        moves.extend(bishop.valid_moves(position, board))

        return moves

class King(Piece):
    def __init__(self, colour):
        super().__init__('K', colour)

    def valid_moves(self, position, board):
        row, col = position
        moves = []

        # Possible king moves
        king_moves = [
                    (-1, -1), (-1, 0), (-1, 1), (0, -1), 
                    (0, 1), (1, -1), (1, 0), (1, 1)
                    ]

        for move in king_moves:
            new_row = row + move[0]
            new_col = col + move[1]
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                if board[new_row][new_col] == None or board[new_row][new_col].colour != self.colour:
                    moves.append((new_row, new_col))

        return moves


board = ChessBoard()



# loooooooooooooooop
while True:
    print(board())
    move = input("Move? ").strip().upper()

    if len(move.split()) != 2:
        print("Invalid input format. Please use 'e2 e4' format.")
        continue

    from_notation, to_notation = move.split()

    from_pos = board.pos(from_notation)
    to_pos = board.pos(to_notation)

    piece = board.board[from_pos[0]][from_pos[1]]

    if piece == None:
        print("No piece at start pos")
        continue
    if piece.colour != 'white':
        print("Hands off that's not yours")
        continue
    if to_pos not in piece.valid_moves(from_pos, board.board):
        print("Not allowed")
        continue


    # actually moving the piece
    board.board[to_pos[0]][to_pos[1]] = piece
    board.board[from_pos[0]][from_pos[1]] = None