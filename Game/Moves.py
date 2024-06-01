from typing import List, Tuple
import Custom_Exceptions
import Pieces

"""
Explaining all var names above will be exhausting. All will be named according to this table where the most of the things are
represented with a single later. Var names will be constructed from these.

W = white
B = black

p = location
n = knight
k = king
q = queen
b = bishop
r = rook

brd = board
pos = position (index on the board as it is a 1D array)
"""

"""
Situations we can except when we check a square are encoded in the following way:
empty = 0, there is a blocking location = 1, there is an enemy location to capture = 2, there is a check = 3
"""


## Placeholder
def game_over():  ## TODO
    pass


#  A global function to call when generating moves.
def get_moves_global(board: list, move_turn: int) -> tuple:  # move_turn is the half move count since the start of the game

    w_moves: list = []
    b_moves: list = []
    restricted_sqrs_wk: list = []
    restricted_sqrs_bk: list = []

    if not len(board) == 64:
        raise Custom_Exceptions.PrintProblem("Invalid Board", "The board is not 64 squares long")

    for piece in board:
        if piece == 0:
            continue
        if not piece.__class__ == Pieces.King:
            move_method_output = piece.get_moves(self=piece, board=board)
            if piece.__class__ == Pieces.Pawn:
                if move_method_output[2]:  # Check
                    break
                if piece.color == 0:
                    restricted_sqrs_bk.extend(move_method_output[1])
                    w_moves.extend(move_method_output[0])
                else:
                    restricted_sqrs_wk.extend(move_method_output[1])
                    b_moves.extend(move_method_output[0])
            else:
                if move_method_output[1]:  # Check
                    break
                if piece.color == 0:
                    restricted_sqrs_bk.extend(move_method_output[0])
                    w_moves.extend(move_method_output[0])
                else:
                    restricted_sqrs_wk.extend(move_method_output[0])
                    b_moves.extend(move_method_output[0])
        else:
            if piece.color == 0:
                w_k: Pieces.King = piece
            else:
                b_k: Pieces.King = piece
    if w_k == None or b_k == None:
        raise Custom_Exceptions.PrintProblem("No King?????????", "Couldn't find the king on the move generation function.")
    w_k_moves = w_k.get_moves(board, restricted_sqrs_wk)
    b_k_moves = b_k.get_moves(board, restricted_sqrs_bk)

    if move_turn % 2 == 0:
        if len(w_k_moves) == 0:
            game_over()
    else:
        if len(b_k_moves) == 0:
            game_over()
    return w_moves, b_moves


def king_moves(board: list, loc: int, restricted_sqrs: list, color: int):
    moves: list = []
    possible_move_sqrs: list = [loc - 9, loc - 8, loc - 7, loc - 1, loc + 1, loc + 7, loc + 8, loc + 9]
    for sqr in possible_move_sqrs:
        if -1 < sqr < 64 and sqr not in restricted_sqrs:
            if board[sqr] is None:
                moves.append(sqr)
            elif not board[sqr].color == color:
                moves.append(color)
    return moves


def take_step(brd: list, loc: int, step: int,
              color: int) -> tuple:  # For diagonal and straight moves to iterate to the end of the board
    # Color: W=0,B=1
    # Possible situations to except when we check a square:
    # empty = 0, there is a blocking location = 1, there is an enemy location to capture = 2, there is a check = 3
    sqr_index: int = loc + step
    square = brd[sqr_index]
    if square is None:
        return True, 0
    if color == 0:
        if square == Pieces.King(1, sqr_index):
            return False, 3
        return True, 2
    elif color == 1:
        if square == Pieces.King(0, sqr_index):
            return False, 3
        return True, 2
    else:
        return False, 1


def pawn_moves(board: List, location: int, color: int) -> Tuple[List[int], List[int], bool]:
    moves: List[int] = []
    attacking_squares: List[int] = []
    checking_the_enemy_king: bool = False

    if color not in (0, 1):
        raise ValueError("Invalid color. Color must be 0 (white) or 1 (black).")

    if color == 0:  # White pawn
        forward_one = location + 8
        forward_two = location + 16
        promotion_row = range(56, 64)
        attacking_squares = [location + 7, location + 9]
    else:  # Black pawn
        forward_one = location - 8
        forward_two = location - 16
        promotion_row = range(0, 8)
        attacking_squares = [location - 9, location - 7]

    for sqr in attacking_squares:
        if 0 <= sqr < 64 and board[sqr] == Pieces.King(1 - color, sqr):
            checking_the_enemy_king = True

    if forward_one in promotion_row:
        moves.append((location % 8, 'promotion'))  ## TODO implement
    else:
        if 0 <= forward_one < 64 and board[forward_one] is None:
            moves.append(forward_one)
        if (color == 0 and location < 16) or (color == 1 and location >= 48):
            if 0 <= forward_two < 64 and board[forward_two] is None:
                moves.append(forward_two)

    return moves, attacking_squares, checking_the_enemy_king  # If you ever change this line, the method that calls this from Game.py globally reaches its outputs thorough index.


"""
Two functions below just use a while loop till the end of the board. There probably is a way more efficient way to do 
this"""
"""
Both functions have the same logic.
Piece is just the index of the location.
"""


def generate_moves_for_direction(board: list, location: int, color: int, directions: list, depth: int) -> tuple:
    moves: list = []
    checking_the_enemy_king: bool = False
    has_a_pin_on_the_enemy_king: bool = False
    pieces_seen_through: list = []

    for direction in directions:
        sqr = location
        for i in range(depth):
            valid, state = take_step(board, sqr, direction, color)

            if not valid:  # Probably a good idea to continue for pins and stuff.
                maybe_pinned = sqr
                for j in range(depth - i):
                    sqr += direction
                    valid_2, state_2 = take_step(board, sqr, direction, color)
                    if not valid_2:
                        break
                    if state_2 == 3:
                        has_a_pin_on_the_enemy_king = True
                        ## maybe_pinned  ## TODO implement move restriction and pin
                    if state_2 == 2:
                        pieces_seen_through.append(sqr)
                break

            sqr += direction
            moves.append(sqr)
            if state == 3:
                checking_the_enemy_king = True
                break
            if state == 2:
                break

    return moves, checking_the_enemy_king, has_a_pin_on_the_enemy_king, pieces_seen_through  # If you ever change this, the method that calls this globally reaches its outputs thorough index.


"""We currently don't do anything with the has_a_pin_on_the_enemy_king and pieces_seen_through so its garbage at the moment
but keep because maybe we will decide to add some ai and it will be useful."""


def diagonal_moves(board: list, location: int, color: int, depth: int) -> tuple:
    directions = [9, 7, -7, -9]
    return generate_moves_for_direction(board, location, color, directions, depth)


def horizontal_and_vertical_moves(board: list, location: int, color: int, depth: int) -> tuple:
    directions = [8, 1, -1, -8]
    return generate_moves_for_direction(board, location, color, directions, depth)


def knight_moves(board: list, location: int, color: int) -> tuple:
    directions = [-17, -15, -6, -10, 6, 10, 15, 17]
    return generate_moves_for_direction(board, location, color, directions, 1)
