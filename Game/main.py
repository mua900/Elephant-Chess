import Game
import Input

""" Call the window initialization function when its done """


def main():
    game: Game = None
    color: int
    board: str = input("Please give a chess position in standard FEN notation. If you want to skip to play from the default starting position, just type 'c' and press enter on your terminal.")
    if board == "c":
        game = Game.set_standard_start_pos()
    else:
        game = Game.Game(board)

    inp: str = input("Please give the move you want to make in standard notation.")

