from typing import List
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

reverse_column_num = {
    0: 'A',
    1: 'B',
    2: 'C',
    3: 'D',
    4: 'E',
    5: 'F',
    6: 'G',
    7: 'H'
}  # Normal dictionary has letters as keys and numbers as values, we maybe need search the opposite way.


def diag_search(board: list, piece: Pieces, start_sqr: int):
    found: list = []
    dirs: list = [-9, -7, 7, 9]
    col = start_sqr % 8  # 0 to 7
    row = start_sqr // 8  # 0 to 7
    bounds: list = [min(col - 1, row - 1), min(7 - row, col - 1), min(7 - row, row - 1), min(7 - row, 7 - col)]

    for direction, bound in zip(dirs, bounds):
        sqr = start_sqr
        for _ in range(bound):
            sqr += direction
            if board[sqr] == piece:
                found.append(sqr)

    return found


def search_horizontal(board: List, piece: Pieces, row: int) -> List[int]:
    if not (0 <= row < 8):
        raise Custom_Exceptions.PrintProblem(
            "Out of range input for the row",
            "Input we are dealing with for the row is not in range [0,8)"
        )

    found: List[int] = []
    start_index = row * 8
    end_index = start_index + 8

    for i in range(start_index, end_index):
        if board[i] and isinstance(board[i], type(piece)) and board[i].color == piece.color:
            found.append(i)

    return found


def search_vertical(board: List, piece: Pieces, column: str) -> List[int]:
    column_index = column_num.get(column.upper())

    if column_index is None:
        raise ValueError(f"Invalid column: {column}")

    found: List[int] = []
    start_index = column_index
    end_index = start_index + 57  # Inclusive range for the last index in the column

    for i in range(start_index, end_index, 8):
        if board[i] and isinstance(board[i], type(piece)) and board[i].color == piece.color:
            found.append(i)

    return found


"""
To use:
If you want to search for vertical or horizontal pass a single character long argument indicating columns with a single 
letter and rows with a single digit.
For diagonal search, stick a "d" at the end of the start square from which to search diagonally.
"""


## TODO make a better version with piece boards
def search_for_piece_on_the_board(board: list, piece: Pieces,
                                  *args) -> list:  # Aditional arg is supposed to be either the row or the column or diagonal
    pieces_searched_for: list = []
    if args[0]:
        for arg in args:
            pieces_searched_for.extend(search_defined(board, piece, arg))
    else:  # This is an entire board wide search.
        for sqr in board:
            if isinstance(sqr, piece) and sqr.color == piece.color:
                pieces_searched_for.append(sqr)
    return pieces_searched_for


def search_defined(board: list, piece: Pieces, arg) -> List[int]:
    found: List[int] = []
    arg_len = len(arg)
    if arg_len == 1:
        if arg.isdigit():
            found.extend(search_horizontal(board, piece, arg))
        elif arg.isalpha():
            found.extend(search_vertical(board, piece, arg))
        else:
            raise Custom_Exceptions.PrintProblem(
                "Invalid column or row",
                "There is a non-alpha, non-digit column or row name we are searching."
            )
    else:
        if arg[-1] == 'd':
            arg.pop(arg[-1])
            found.extend(diag_search(board, piece, arg))
        else:
            raise Custom_Exceptions.PrintProblem("arg length incorrect",
                                                 "The argument passed to filter what to search is invalid")
    return found


def board_coord_index_converter(coord: str):
    if not len(coord) == 2:
        raise Custom_Exceptions.PrintProblem("Problematic coord entry to func", f"The coordinate is {len(coord)} chars")
    column_index: int = column_num[coord[0].upper()]
    return int((coord[0] * 8) + column_index - 8)


def index_to_board_coord_converter(index: int) -> str:
    if abs(index - 31) > 32:
        raise Custom_Exceptions.PrintProblem("Index out of the board", "Index value we are trying to convert is not in the "
                                                                       "boards bounds.")
    column_index: int = (index % 8) - 1
    row_index = index // 8 + 1
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


def match_piece_without_piece_loc(piece: str) -> Pieces:
    piece_map = {
        'K': Pieces.King(0),
        'Q': Pieces.Queen(0),
        'R': Pieces.Rook(0),
        'N': Pieces.Knight(0),
        'B': Pieces.Bishop(0),
        'P': Pieces.Pawn(0),
        'k': Pieces.King(1),
        'q': Pieces.Queen(1),
        'r': Pieces.Rook(1),
        'n': Pieces.Knight(1),
        'b': Pieces.Bishop(1),
        'p': Pieces.Pawn(1)
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
