# FEN
# This code is to initialize and read FEN string
# The first and main part of the FEN string will be referred as fen_board

""" We want to swap out the order of rows in the fen string to be able to work with it since we will
 construct rest of the logic assuming we go from A1 to H8  (A1, A2 .... B1, B2 .... H7, H8) """

import Custom_Exceptions

# Assigning numbers is a temporary solution
WHITE = 0
BLACK = 1


def fen_refine(fen: str):
    if " " not in fen:
        raise Custom_Exceptions.Print_Problem("FEN Error", "FEN string must contain a space to separate the board and side to move.")

    f = fen.split(" ")
    fen_board = f[0]
    if f[1].lower() == "w":
        color_to_move = WHITE
    elif f[1].lower() == "b":
        color_to_move = BLACK
    else:
        raise Custom_Exceptions.Print_Problem("FEN Error", "Invalid side to move. It must be 'w' or 'b'.")
    # TODO We don't do anything about the last part of the FEN yet

    if "/" not in fen_board:
        raise Custom_Exceptions.Print_Problem("FEN Error", "FEN board part must contain '/' to separate rows.")

    rows: list = fen_board.split("/")
    if len(rows) != 8:
        raise Custom_Exceptions.Print_Problem("FEN Error", "FEN board must have exactly 8 rows.")

    rows.reverse()
    ref_fen = "/".join(rows)

    return color_to_move, ref_fen, rows


a = fen_refine("rnb1kbnr/ppp2ppp/8/3pp1N1/2qPP3/8/PPP2PPP/R1BQKBNR w KQkq - 0 1")
print(a[2])


def read_fen(fen_board: str):
    rows: list = fen_board.split("/")

    if len(rows) != 8:
        print("Invalid fen_board in the read_fen()")
