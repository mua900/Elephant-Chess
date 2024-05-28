import MailboxBoard
import Evaluation
import Utils
import Custom_Exceptions


# This will be the entry point of the whole program.
# Rules, main logic etc. goes here
class Game:
    def __init__(self, starting_pos: str):
        self.start_pos, self.start_piece_loc, self.start_color = MailboxBoard.get_board_from_fen(starting_pos)
        self.start_eval: int = Evaluation.eval_function(self.start_piece_loc)
        self.move_history: list = []

        """ Call the window initialization function when its done """

        # Create the piece boards
        self.piece_boards = Utils.piece_board_generator(self.start_piece_loc)
        """
        This up there is a dictionary that contains piece types on keys and lists of their positions on the board as integers
        representing squares on the board
        """
        self.w_piece_brds: dict = {piece: piece_brd for piece, piece_brd in self.piece_boards.items() if piece.color == 0}
        self.b_piece_brds: dict = {piece: piece_brd for piece, piece_brd in self.piece_boards.items() if piece.color == 1}

        # Initialize moves lists
        self.white_moves: list = []
        self.black_moves: list = []

        # Generate initial moves for all pieces
        self._generate_initial_moves()

    def _generate_initial_moves(self):
        """
        Generates initial moves for all pieces based on the starting position.
        This method populates the white_moves and black_moves lists.
        """
        for piece in self.start_piece_loc:
            if piece.color == 0:
                self.white_moves.extend(piece.get_moves(self.start_pos))
            elif piece.color == 1:
                self.black_moves.extend(piece.get_moves(self.start_pos))
            else:
                raise Custom_Exceptions.PrintProblem("Invalid Color", "There is a piece with an invalid color value.")

    def update_moves(self):
        """
        Updates moves for all pieces after a move is made.
        This method can be called after each move to refresh the moves list.
        """
        self.white_moves = []
        self.black_moves = []
        for piece in self.start_piece_loc:
            if piece.color == 0:
                self.white_moves.extend(piece.get_moves(self.start_pos))
            elif piece.color == 1:
                self.black_moves.extend(piece.get_moves(self.start_pos))
