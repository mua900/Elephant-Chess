import Custom_Exceptions
import Utils


def get_board_from_fen(fen: str) -> (list, int):  # A list instead of a 1D array, a list of tuples, an int either 0 or 1
    board: list = [0] * 64
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
    for i in range(8):
        for j in range(len(rows[i])):
            if rows[i][j].isdigit():
                sqr_index += int(rows[i][j]) - 1
            elif rows[i][j].isalpha():
                board[sqr_index] = (Utils.match_piece(rows[i][j], sqr_index))
            else:
                raise Custom_Exceptions.PrintProblem("FEN is not valid", "There are invalid character types in the FEN")
            sqr_index += 1

    return board, color_to_move


print(get_board_from_fen("8/ppk3pp/8/3K4/8/8/PP3PPP/8 b - - 0 26"))
