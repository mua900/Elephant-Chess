import math

import Custom_Exceptions
import Moves


class Piece:

    def __eq__(self, other):
        return isinstance(self, other) and self.color == other.color and self.position == other.position

    value: int
    letter: str

    def __init__(self, color: int, *args):  # Arg[0] for location
        self.color: int = color  # White = 0, black = 1
        self.position = args[0]

    def get_moves(self, board: list):
        raise NotImplementedError("Custom // This method should be overridden in the subclasses.")


class Pawn(Piece):
    value = 1
    letter = 'p'

    def get_moves(self, board: list):
        if self.position is None:
            Custom_Exceptions.PrintProblem("Location info missing", "The location of the piece we are searching moves for is missing.")
        Moves.pawn_moves(board, self.position, self.color)


class Rook(Piece):
    value = 5
    letter = 'r'

    def get_moves(self, board: list):
        if self.position is None:
            Custom_Exceptions.PrintProblem("Location info missing", "The location of the piece we are searching moves for is missing.")
        Moves.horizontal_and_vertical_moves(board, self.position, self.color, 8)


class Queen(Piece):
    value = 9
    letter = 'q'

    def get_moves(self, board: list):
        if self.position is None:
            Custom_Exceptions.PrintProblem("Location info missing", "The location of the piece we are searching moves for is missing.")
        Moves.horizontal_and_vertical_moves(board, self.position, self.color, 8)
        Moves.diagonal_moves(board, self.position, self.color, 8)


class King(Piece):
    value = math.inf
    letter = 'k'

    def get_moves(self, board: list, danger_sqrs: list = None):
        if self.position is None:
            Custom_Exceptions.PrintProblem("Location info missing", "The location of the piece we are searching moves for is missing.")
        if danger_sqrs is None:
            danger_sqrs = []
        Moves.king_moves(board, danger_sqrs, self.color)


class Bishop(Piece):
    value = 3
    letter = 'b'

    def get_moves(self, board: list):
        if self.position is None:
            Custom_Exceptions.PrintProblem("Location info missing", "The location of the piece we are searching moves for is missing.")
        Moves.diagonal_moves(board, self.position, self.color, 8)


class Knight(Piece):
    value = 3
    letter = 'n'

    def get_moves(self, board: list):
        if self.position is None:
            Custom_Exceptions.PrintProblem("Location info missing", "The location of the piece we are searching moves for is missing.")
        Moves.knight_moves(board, self.position, self.color)
