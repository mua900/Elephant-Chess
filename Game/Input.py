import Pieces
import Utils
import Custom_Exceptions

"""
# This is to support standard notation.
def handle_input(board: list, inp: str, color_to_move: int):
    Parse the input to determine the type of chess move.
    If the input is just a coordinate, it is a pawn move.
    If it includes a piece identifier, search for the moves of that piece.
    The input could also specify the start coordinate before the target square.
    # Initialize target square variable
    start_sqr: int
    target_sqr: int
    piece_to_move: Pieces
    inp_len: int = len(inp)
    candidate_pieces: List[Pieces] = []

    if color_to_move == 0:
        direc = -1
    else:
        direc = 1
    if 'x' in inp:
        parts = inp.split('x')
        start_sqr = Utils.board_coord_index_converter(parts[0])
        target_sqr = Utils.board_coord_index_converter(parts[1])
    else:
        # Match the input length to determine the type of move
        match inp_len:
            case 2:  # Only the target square is specified (pawn move)
                target_sqr = Utils.board_coord_index_converter(inp)
                sqr_before = board[target_sqr + 8 * direc]
                if color_to_move == 0 and inp[1] == 4:
                    if sqr_before is None:
                        two_sqr_before = board[target_sqr + 16 * direc]
                        if two_sqr_before == Pieces.Pawn(color_to_move, target_sqr + 16 * direc):
                            piece_to_move = two_sqr_before
                if sqr_before == Pieces.Pawn(color_to_move, target_sqr + 8 * direc):
                    piece_to_move = sqr_before
            case 3:  # Piece type and target square are specified
                piece_letter = inp[0]
                col = inp[1]
                row = inp[2]
                target_sqr = Utils.board_coord_index_converter(col + row)
                piece = Utils.match_piece_without_piece_loc(inp[0])
                if piece_letter.upper() == "Q":
                    candidate_pieces.extend(Utils.search_for_piece_on_the_board(board, piece, col, row, str(target_sqr) + "d"))
                elif piece_letter.upper() == "R":
                    candidate_pieces.extend(Utils.search_for_piece_on_the_board(board, piece, col, row))
                elif piece_letter.upper() == "B":
                    candidate_pieces.extend(Utils.search_for_piece_on_the_board(board, piece, str(target_sqr) + "d"))
                elif piece_letter.upper() == "N":
                    possible_sqrs: List[int] = [target_sqr - 17, target_sqr - 15, target_sqr - 6, target_sqr - 10, target_sqr + 6, target_sqr + 10, target_sqr + 15, target_sqr + 17]
                    for sqr in possible_sqrs:
                        if 0 <= sqr < 64:
                            if board[sqr] == Pieces.Pawn(color_to_move, sqr):
                                candidate_pieces.extend(board[sqr])
            case 4:  # Start square and target square are specified
                piece_to_move = inp[0]
                start_row_or_column = inp[1]
                start_sqr = Utils.search_for_piece_on_the_board(start_row_or_column)
                target_sqr = Utils.board_coord_index_converter(inp[2] + inp[3])
            case 5:
                piece_to_move = inp[0]
                start_sqr = Utils.board_coord_index_converter(inp[1] + inp[2])
                target_sqr = Utils.board_coord_index_converter(inp[3] + inp[4])
            case _:
                raise Custom_Exceptions.PrintProblem("Invalid Move Input", "Move Input is not the length it is supposed to.")
    
    # Return or process target_sqr as needed
    return start_sqr, target_sqr, piece_to_move ## TODO
"""

"""Probably going to scrap the one above so maybe change the name of the one below to handle_input"""


"""Recommended you call with a piece board."""
def parse_and_search_move(board: list, inp: str, legal_moves: dict, *piece_map: list) -> Pieces:
    """
    Parses the input string to identify the piece to move and the target square, then searches for the piece
    on the board or within the piece_map that can legally make the specified move.

    Parameters:
    board (list): The game board with pieces.
    inp (str): The input string specifying the move.
    legal_moves (dict): A dictionary with pieces as keys and their legal moves as values.
    piece_map (list): Optional lists of pieces to check.

    Returns:
    Pieces: The piece that can make the move if exactly one such piece is found.

    Raises:
    Custom_Exceptions.PrintProblem: If there is not exactly one piece that can make the move.
    """
    piece_to_move: Pieces = None
    col: str = " "
    row: str = " "

    # Parse the input string
    for char in inp:
        if char.isalpha():
            if char.isupper():
                piece_to_move = Utils.match_piece_without_piece_loc(char)
            else:
                if col == " ":
                    col = char
        elif char.isdigit():
            if row == " ":
                row = char

    # Convert the target square to an index
    target_sqr: int = Utils.board_coord_index_converter(col + row)

    # Search for the piece that can make the move
    identical_pieces_to_have_the_same_move: list = []

    if piece_map:
        # Search within piece_map if provided
        for piece in piece_map:
            if piece == piece_to_move and target_sqr in legal_moves.get(piece_to_move, []):
                identical_pieces_to_have_the_same_move.append(piece)
    else:
        # Search within the board if piece_map is not provided
        for piece in board:
            if piece == piece_to_move and target_sqr in legal_moves.get(piece_to_move, []):
                identical_pieces_to_have_the_same_move.append(piece)

    # If exactly one piece can make the move, return it
    if len(identical_pieces_to_have_the_same_move) == 1:
        return identical_pieces_to_have_the_same_move[0]
    else:
        raise Custom_Exceptions.PrintProblem(
            "Move Ambiguity",
            "There should be exactly one piece that can make the specified move, but found {}.".format(len(identical_pieces_to_have_the_same_move))
        )
