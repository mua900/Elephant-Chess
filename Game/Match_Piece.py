import Custom_Exceptions
import Pieces

piece_map = {
    'K': (Pieces.King, 0),
    'Q': (Pieces.Queen, 0),
    'R': (Pieces.Rook, 0),
    'N': (Pieces.Knight, 0),
    'B': (Pieces.Bishop, 0),
    'P': (Pieces.Pawn, 0),
    'k': (Pieces.King, 1),
    'q': (Pieces.Queen, 1),
    'r': (Pieces.Rook, 1),
    'n': (Pieces.Knight, 1),
    'b': (Pieces.Bishop, 1),
    'p': (Pieces.Pawn, 1),
}


def match_piece(piece: str) -> Pieces:
    if piece not in piece_map:
        raise Custom_Exceptions.PrintProblem("Unknown Char in the Board", f"There is a piece that does not match to any of "
                                                                          f"the pieces ({piece})")
    piece_class, color = piece_map[piece]
    new_piece = piece_class()
    new_piece.color = color
    return new_piece
