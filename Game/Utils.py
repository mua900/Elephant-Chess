import Custom_Exceptions
import Pieces

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
