import Custom_Exceptions
import MailboxBoard

"""
Explaining all var names above will be exhausting. All will be named according to this table where the most of the things are
represented with a single later. Var names will be constructed from these.

W = white
B = black

p = location
n = knight
k = king
q = queen
b = bishop
r = rook

brd = board
pos = position (index on the board as it is a 1D array)
"""


class PiecePositionEncodings:

    def __init__(self, board: list):
        self.board = board
        # Declare variables
        self.wp_brd: list = []
        self.Wn_brd: list = []
        self.Wb_brd: list = []
        self.Wr_brd: list = []
        self.Wq_brd: list = []
        self.bp_brd: list = []
        self.Bn_brd: list = []
        self.Bb_brd: list = []
        self.Br_brd: list = []
        self.Bq_brd: list = []
        self.Wk_pos: int = 0
        self.Bk_pos: int = 0

    def generate_encodings(self):  # We will only run this once at the initialization
        for i in range(64):
            if self.board[i] == 0:
                continue
            if self.board[i] == "K":
                self.Wk_pos = i
            if self.board[i] == "k":
                self.Bk_pos = i
            if self.board[i] == "P":
                self.wp_brd.append(i)
            if self.board[i] == "p":
                self.bp_brd.append(i)
            if self.board[i] == "R":
                self.Wr_brd.append(i)
            if self.board[i] == "r":
                self.Br_brd.append(i)
            if self.board[i] == "B":
                self.Wb_brd.append(i)
            if self.board[i] == "b":
                self.Bb_brd.append(i)
            if self.board[i] == "N":
                self.Wn_brd.append(i)
            if self.board[i] == "n":
                self.Bn_brd.append(i)
            if self.board[i] == "Q":
                self.Wq_brd.append(i)
            if self.board[i] == "q":
                self.Bq_brd.append(i)
            else:
                Custom_Exceptions.PrintProblem("Mailbox Error", "There are unknown chars in the mailbox!")


"""I forgot about this existed so it is not used. Maybe remove if you see this"""


"""Move generations from now on"""

"""Important note:
These are to run once when the position is first loaded and read from fen. After that we can just simply modify existing
list of moves we have. Which is concern for another day at the moment.
Situations we can except when we check a square are encoded in the following way:
empty = 0, there is a blocking location = 1, there is an enemy location to capture = 2, there is a check = 3
"""


def take_step(brd: list, loc: int, step: int,
              color: int) -> tuple:  # For diagonal and straight moves to iterate to the end of the board
    # Color: W=0,B=1
    # Possible situations to except when we check a square:
    # empty = 0, there is a blocking location = 1, there is an enemy location to capture = 2, there is a check = 3
    square: str = brd[loc + step]
    if square == 0:
        return True, 0
    elif square.islower() and color == 0:
        if square == 'k':
            return False, 3
        return True, 2
    elif square.isupper() and color == 1:
        if square == 'K':
            return False, 3
        return True, 2
    else:
        return False, 1


def pawn_moves(board: list, location: int, color: int) -> tuple:
    moves: list = []
    checking_the_enemy_king: bool = False
    if color == 0:
        if location + 8 > 54:  # Promotion move
            moves.append((location % 8, 'promotion'))  ##TODO implement this
        if location < 8:  # Pawn not moved
            if board[location + 16] != 0:
                moves.append(location + 16)
        if board[location + 8] != 0:
            moves.append(location + 8)
    elif color == 1:
        if location - 8 < 8:  # Promotion move
            moves.append((location % 8, 'promotion'))
        if location > 54:  # Pawn not moved
            if board[location - 16] != 0:
                moves.append(location - 16)
        if board[location - 8] != 0:
            moves.append(location - 8)
    else:
        raise ValueError("Custom // There is a pawn that is not 0 or 1 for color.")
    return moves, checking_the_enemy_king


"""Two functions below just use a while loop till the end of the board. There probably is a way more efficient way to do 
this"""
"""
Both functions have the same logic.
Piece is just the index of the location.
"""


def generate_moves_for_direction(board: list, location: int, color: int, directions: list, depth: int) -> tuple:
    moves: list = []
    checking_the_enemy_king: bool = False

    for direction in directions:
        sqr = location
        for i in range(depth):
            valid, state = take_step(board, sqr, direction, color)
            if not valid:
                break
            sqr += direction
            moves.append(sqr)
            if state == 3:
                checking_the_enemy_king = True
                break
            if state == 2:
                break

    return moves, checking_the_enemy_king


def diagonal_moves(board: list, location: int, color: int, depth: int) -> tuple:
    directions = [9, 7, -7, -9]
    return generate_moves_for_direction(board, location, color, directions, depth)


def horizontal_and_vertical_moves(board: list, location: int, color: int, depth: int) -> tuple:
    directions = [8, 1, -1, -8]
    return generate_moves_for_direction(board, location, color, directions, depth)


def knight_moves(board: list, location: int, color: int) -> tuple:
    directions = [-17, -15, -6, -10, 6, 10, 15, 17]
    return generate_moves_for_direction(board, location, color, directions, 1)
