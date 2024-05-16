import Custom_Exceptions
import Match_Piece


def get_board_from_fen(fen: str) -> (list, list):
    pieces = []

    board = [0] * 64
    if not ("/" in fen and " " in fen):
        raise Custom_Exceptions.PrintProblem(
            "FEN is not valid",
            "FEN is either lacking spaces or slashes."
        )

    f = fen.split(" ")
    if len(f) < 2:
        raise Custom_Exceptions.PrintProblem(
            "FEN is not valid",
            "FEN string is missing required components."
        )
    fen_board, color_to_move = f[0], f[1]

    rows = fen_board.split("/")
    if len(rows) != 8:
        raise Custom_Exceptions.PrintProblem(
            "FEN is not valid",
            "FEN does not seem to contain 8 rows!"
        )

    rows.reverse()
    sqr_index: int = 0
    for row in range(8):
        for char in range(len(rows[row])):
            if rows[row][char].isdigit():
                sqr_index += int(rows[row][char]) - 1
            elif rows[row][char].isalpha():
                pieces.append((sqr_index, Match_Piece.match_piece(rows[row][char])))
                board[sqr_index] = rows[row][char]
            else:
                raise Custom_Exceptions.PrintProblem("FEN is not valid", "There are invalid character types in the FEN")
            sqr_index += 1

    return board, pieces
