import Custom_Exceptions
import Pieces

"""
Legacy:

# FEN
# This code is to initialize and read FEN string
# The first and main part of the FEN string will be referred as fen_board

# We want to swap out the order of rows in the fen string to be able to work with it since we will
# construct rest of the logic assuming we go from A1 to H8  (A1, A2 .... B1, B2 .... H7, H8)

# Assigning numbers is a temporary solution
    WHITE = 0
    BLACK = 1
    def fen_refine(fen: str):
        if " " not in fen:
            raise Custom_Exceptions.PrintProblem("FEN Error", "FEN string must contain a space to separate the board and side to move.")
        f = fen.split(" ")
        fen_board = f[0]
        if f[1].lower() == "w":
            color_to_move = WHITE
        elif f[1].lower() == "b":
            color_to_move = BLACK
        else:
            raise Custom_Exceptions.PrintProblem("FEN Error", "Invalid side to move. It must be 'w' or 'b'.")
        # TODO We don't do anything about the last part of the FEN yet
        if "/" not in fen_board:
            raise Custom_Exceptions.PrintProblem("FEN Error", "FEN board part must contain '/' to separate rows.")
        rows: list = fen_board.split("/")
        if len(rows) != 8:
            raise Custom_Exceptions.PrintProblem("FEN Error", "FEN board must have exactly 8 rows.")
        rows.reverse()
        ref_fen = "/".join(rows)
        return color_to_move, ref_fen, rows
    a = fen_refine("rnb1kbnr/ppp2ppp/8/3pp1N1/2qPP3/8/PPP2PPP/R1BQKBNR w KQkq - 0 1")
    print(a[2])  
    def read_fen(fen_board: str):
        rows: list = fen_board.split("/")
    
        if len(rows) != 8:
            print("Invalid fen_board in the read_fen()")
"""

column_num: dict = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7
}


def board_coord_index_converter(coord: str):
    if not len(coord) == 2:
        raise Custom_Exceptions.PrintProblem("Problematic coord entry to func", f"The coordinate is {len(coord)} chars")
    column_index: int = column_num[coord[0].upper()]
    return int((coord[0] * 8) + column_index - 8)


def index_to_board_coord_converter(index: int):
    if abs(index - 31) > 32:
        raise Custom_Exceptions.PrintProblem("Index out of the board", "Index value we are trying to convert is not in the "
                                                                       "boards bounds.")
    column_index: int = (index % 8) - 1
    row_index = index // 8 + 1
    reverse_column_num = {v: k for k, v in column_num.items()}
    return reverse_column_num[column_index] + str(row_index)


def match_piece(piece: str, piece_loc) -> Pieces:
    piece_map = {
        'K': Pieces.King(0, piece_loc),
        'Q': Pieces.Queen(0, piece_loc),
        'R': Pieces.Rook(0, piece_loc),
        'N': Pieces.Knight(0, piece_loc),
        'B': Pieces.Bishop(0, piece_loc),
        'P': Pieces.Pawn(0, piece_loc),
        'k': Pieces.King(1, piece_loc),
        'q': Pieces.Queen(1, piece_loc),
        'r': Pieces.Rook(1, piece_loc),
        'n': Pieces.Knight(1, piece_loc),
        'b': Pieces.Bishop(1, piece_loc),
        'p': Pieces.Pawn(1, piece_loc)
    }
    if piece not in piece_map:
        raise Custom_Exceptions.PrintProblem("Unknown Char in the Board", f"There is a piece that does not match to any of "
                                                                          f"the pieces ({piece})")
    return piece_map[piece]


# Returns a list of indexes (a list of ints) that represent positions for the pieces that exist on the board.
def piece_board_generator(pieces_brd: list) -> dict:
    piece_boards: dict = {}

    # The piece here is a class instance bundled in a tuple together with an int 0 or 1 for color.
    for piece in pieces_brd:
        if piece == 0:
            continue
        if piece not in piece_boards:
            piece_boards[piece] = []
        piece_boards[piece].append(piece.position)

    return piece_boards
