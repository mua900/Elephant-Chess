import math


class Piece:
    value: int
    letter: str
    color: int  # White = 0, black = 1


class Pawn(Piece):
    Piece.value = 1
    letter = 'p'


class Rook(Piece):
    Piece.value = 5
    letter = 'r'


class Queen(Piece):
    Piece.value = 9
    letter = 'q'


class King(Piece):
    Piece.value = math.inf
    letter = 'k'


class Bishop(Piece):
    Piece.value = 3
    letter = 'b'


class Knight(Piece):
    Piece.value = 3
    letter = 'n'
