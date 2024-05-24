# All off the chess Pieces as classes. Will be implemented with OOP.

class Piece:
    value: int
    letter: str


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
    Piece.value = 10000
    letter = 'k'


class Bishop(Piece):
    Piece.value = 3
    letter = 'b'


class Knight(Piece):
    Piece.value = 3
    letter = 'n'
