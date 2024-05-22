import MailboxBoard
import Custom_Exceptions


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
                Custom_Exceptions.Print_Problem("Mailbox Error", "There are unknown chars in the mailbox!")


## TEST ##
lgl_moves = PiecePositionEncodings(
    MailboxBoard.MailboxBoard.get_board_from_fen("5rk1/2p1ppbp/B4np1/2pP4/P3P3/5Q1P/5PP1/1N4K1 b - - 0 22")[0])
lgl_moves.generate_encodings()
print(*lgl_moves.Bb_brd)
## TEST ##

# Works properly


"""Move generations from now on"""

"""Important note:
These are to run once when the position is first loaded and read from fen. After that we can just simply modify existing
list of moves we have. Which is concern for another day at the moment.
Situations we can except when we check a square are encoded in the following way:
empty = 0, there is a blocking piece = 1, there is an enemy piece to capture = 2, there is a check = 3
"""

check: bool = False


def take_step(brd: list, loc: int, step: int,
              color: int) -> tuple:  # For diagonal and straight moves to iterate to the end of the board
    # Color: W=0,B=1
    # Possible situations to except when we check a square:
    # empty = 0, there is a blocking piece = 1, there is an enemy piece to capture = 2, there is a check = 3
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


def pawn_moves(board: list, wp_brd: list, bp_brd: list) -> tuple:
    wp_moves = []
    bp_moves = []
    if wp_brd:
        for pawn in wp_brd:
            if pawn + 8 > 54:  # Promotion move
                wp_moves.append((pawn % 8, 'promotion'))  ##TODO implement this
            if pawn < 8:  # Pawn not moved
                if board[pawn + 16] != 0:
                    wp_moves.append((pawn, 16))
            if board[pawn + 8] != 0:
                wp_moves.append((pawn, 8))
    if bp_brd:
        for pawn in bp_brd:
            if pawn - 8 < 8:  # Promotion move
                bp_moves.append((pawn % 8, 'promotion'))
            if pawn > 54:  # Pawn not moved
                if board[pawn - 16] != 0:
                    bp_moves.append((pawn, -16))
            if board[pawn - 8] != 0:
                bp_moves.append((pawn, -8))
    return wp_moves, bp_moves


# TODO look at this some time later
"""Two functions above just use a while loop till the end of the board. There probably is a way more efficient way to do 
this"""
"""
## Revision of the two functions below
For the 
Depth will be one for the king and to the end of the board for other pieces.
Both functions have the same logic.
Piece is just the index of the piece.
Eliminating illegal moves for the king is another days concern.
"""


def diagonal_moves(board: list, piece: int, color: int) -> list:
    # There are 4 directions we need to iterate through
    moves: list = []
    # up right
    up_right = piece
    while take_step(board, up_right, 9, color)[0]:
        up_right += 9
        moves.append(up_right)
    # up_left
    up_left = piece
    while take_step(board, up_left, 7, color)[0]:
        up_left += 7
        moves.append(up_left)
    # down_right
    down_right = piece
    while take_step(board, down_right, -7, color)[0]:
        down_right -= 7
        moves.append(down_right)
    # down_left
    down_left = piece
    while take_step(board, down_left, -9, color)[0]:
        down_left -= 9
        moves.append(down_left)

    return moves


def straight_moves(board: list, piece: int, color: int) -> list:
    moves: list = []
    # Up
    u: int = piece
    while take_step(board, u, 8, color)[0]:
        u += 8
        moves.append(u)
    # right
    right: int = piece
    while take_step(board, right, 1, color)[0]:
        right += 1
        moves.append(right)
    # down
    down: int = piece
    while take_step(board, down, -8, color)[0]:
        down -= 8
        moves.append(down)
    # left
    left: int = piece
    while take_step(board, left, -1, color)[0]:
        left -= 1
        moves.append(left)

    return moves
