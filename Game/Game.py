import sys
import MailboxBoard
import Evaluation
import Moves
import Utils


"""Send whatever command there is to send to the application UI lib here"""
def game_over(winning_side):  ## TODO
    print(f"The Winning Side Is {winning_side}"
          f"Do you want to play again or quit? [y/n]")
    y_or_n = input()
    if y_or_n.lower() == "y":
        start_pos = input("Give a new starting position if you want or if will start with the default, give 'd'.")
        if start_pos == 'd':
            set_standard_start_pos()
        Game(start_pos)
    else:
        sys.exit()


# This will be the entry point of the whole program.
class Game:
    def __init__(self, starting_pos: str):
        print(
            "Welcome. Please make a move. Moves are supposed to be in standard notation."
        )  ## TODO work on welcoming message

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
