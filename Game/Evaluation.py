import Custom_Exceptions
import Utils


def eval_function(pieces: list) -> int:  # Just count the pieces with their values for now
    piece_value_sum: int = 0

    for p in pieces:
        piece = Utils.match_piece(p)
        if piece.color == 0:
            piece_value_sum += piece.value
        elif piece.color == 1:
            piece_value_sum += piece.value
        else:
            Custom_Exceptions.PrintProblem("Non Defined Piece Color", "The piece we are trying to evaluate has a non "
                                                                      "defined value.")

    return piece_value_sum
