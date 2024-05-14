# FEN
# This code is to initialize and read FEN string

""" We want to swap out the order of rows in the fen string to be able to work with it since we will
 construct rest of the logic assuming we go from A1 to H8  (A1, A2 .... B1, B2 .... H7, H8) """


# Assigning numbers is a temporary solution
WHITE = 0
BLACK = 1


def fen_refine(fen: str):
    fen_is_valid = True
    ref_fen: str = ""
    color_to_move = None

    if " " in fen:
        f = fen.split(" ")
        fen_pieces = f[0]
        if f[1].lower() == "w":
            color_to_move = WHITE
        elif f[1].lower() == "b":
            color_to_move = BLACK
        else:
            fen_is_valid = False

        # We don't do anything about the last part of the FEN yet

    else:
        fen_is_valid = False

    if "/" in fen_pieces:
        rows: list = fen_pieces.split("/")
    else:
        fen_is_valid = False

    if len(rows) != 8:
        fen_is_valid = False

    if fen_is_valid:
        rows.reverse()
        ref_fen = "/".join(rows)

    return fen_is_valid, color_to_move, ref_fen



# DELETE
a = fen_refine("rnb1kbnr/ppp2ppp/8/3pp1N1/2qPP3/8/PPP2PPP/R1BQKBNR w KQkq - 0 1")
if not a[0]:
    print("Invalid FEN string")
else:
    print(a[2])
# DELETE
