import Game

""" Call the window initialization function when its done """


def main():
    board: str = input("Please give a chess position in standard FEN notation. If you want to skip to play from the default starting position, just type 'c' and press enter on your terminal.")
    if board == "c":
        Game.set_standard_start_pos()
    else:
        Game.Game(board)
