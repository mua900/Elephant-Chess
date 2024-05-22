import Custom_Exceptions

"""
Explaining all var names above will be exhausting. All will be named according to this table where the most of the things are
represented with a single later. Var names will be constructed from these.

W = white
B = black

p = pawn
n = knight
k = king
q = queen
b = bishop
r = rook

brd = board
pos = position (index on the board as it is a 1D array)
"""


class MailboxBoard:
    files = ["A", "B", "C", "D", "E", "F", "G", "H"]
    ranks = [1, 2, 3, 4, 5, 6, 7, 8]

    def __init__(self):
        pass

    @staticmethod
    def get_board_from_fen(fen: str) -> (list, int):
        how_many_pieces = 0

        board = [0] * 64
        if not "/" or " " not in fen:
            raise Custom_Exceptions.Print_Problem("FEN is not valid", "FEN is either lacking spaces or slashes.")
        f = fen.split(" ")
        fen_board, color_to_move = f[0], f[1]

        rows = fen_board.split("/")
        if len(rows) != 8:
            raise Custom_Exceptions.Print_Problem("FEN is not valid", "FEN does not seem to contain 8 rows!")

        rows.reverse()  # FEN.py is kinda redundant now
        sqr_index: int = 0
        for i in range(8):
            for j in range(len(rows[i])):
                if rows[i][j].isdigit():
                    sqr_index += int(rows[i][j]) - 1
                elif rows[i][j].isalpha():
                    board[sqr_index] = rows[i][j]
                    how_many_pieces += 1
                else:
                    raise Custom_Exceptions.Print_Problem("FEN is not valid", "There are invalid character types in the FEN")
                sqr_index += 1

        return board, how_many_pieces
