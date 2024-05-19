
import MailboxBoard
import Custom_Exceptions


class LegalMoves:

    def __init__(self, board: str):
        self.board = board
        # Declare variables
        self.Wp_brd: list = []
        self.Wn_brd: list = []
        self.Wb_brd: list = []
        self.Wr_brd: list = []
        self.Wq_brd: list = []
        self.Bp_brd: list = []
        self.Bn_brd: list = []
        self.Bb_brd: list = []
        self.Br_brd: list = []
        self.Bq_brd: list = []
        self.Wk_pos: int = 0
        self.Bk_pos: int = 0

    def generate_encodings(self, fen: str) -> list: ## We will only run this once at the initialization
        board: list = MailboxBoard.MailboxBoard.get_board_from_fen(fen)[0]
        for i in range(64):
            if board[i] == 0:
                continue
            if board[i] == "K":
                self.Wk_pos = i
            if board[i] == "k":
                self.Bk_pos = i
            if board[i] == "P":
                self.Wp_brd.append(i)
            if board[i] == "p":
                self.Bp_brd.append(i)
            if board[i] == "R":
                self.Wr_brd.append(i)
            if board[i] == "r":
                self.Br_brd.append(i)
            if board[i] == "B":
                self.Wb_brd.append(i)
            if board[i] == "b":
                self.Br_brd.append(i)
            if board[i] == "N":
                self.Wn_brd.append(i)
            if board[i] == "n":
                self.Bn_brd.append(i)
            if board[i] == "Q":
                self.Wq_brd.append(i)
            if board[i] == "q":
                self.Bn_brd.append(i)
            else:
                Custom_Exceptions.Print_Problem("Mailbox Error", "There are unknown chars in the mailbox!")
