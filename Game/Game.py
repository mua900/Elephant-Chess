import MailboxBoard
import Evaluation
import Moves
import Utils


# This will be the entry point of the whole program.
# Rules, main logic etc. goes here
class Game:
    def __init__(self, starting_pos: str):
        if starting_pos is None:
            set_standard_start_pos()
        self.start_pos, self.start_color = MailboxBoard.get_board_from_fen(starting_pos)
        self.start_eval: int = Evaluation.eval_function(self.start_pos)
        self.move_history: list = []

        # Create the piece boards
        self.piece_boards = Utils.piece_board_generator(self.start_pos)
        """
        This up there is a dictionary that contains piece types on keys and lists of their positions on the board as integers
        representing squares on the board
        """
        self.w_piece_brds: dict = {piece: piece_brd for piece, piece_brd in self.piece_boards.items() if piece.color == 0}
        self.b_piece_brds: dict = {piece: piece_brd for piece, piece_brd in self.piece_boards.items() if piece.color == 1}

        # Initialize moves lists
        self.white_moves: list = []
        self.black_moves: list = []

        self.white_moves, self.black_moves = Moves.get_moves_global(self.start_pos, self.start_color)


def set_standard_start_pos():
    Game("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
