import Pieces
import Utils


def print_non_empty_sqr(mid: int, piece: str, even: bool):
    if even:
        print(" " * (mid - 1) + piece + " " * mid)
    else:
        print(" " * mid + piece + " " * mid)


def draw_board(board: list, sqr_side: int):
    brd: list = Utils.convert_between_top_left_based_indexing_and_bottom_left_based(board, 1)
    mid_of_sqr: int = sqr_side // 2
    even: bool = mid_of_sqr % 2 == 0
    for row in range(9):
        if row % 8 == 0:
            print("-" * (sqr_side * 8))
        else:
            for col in range(8):
                sqr = brd[8 * row + col]
                if sqr is None:
                    print("|" + " " * (sqr_side - 1), end="")
                else:
                    match sqr.__class__:
                        case Pieces.Pawn:
                            if sqr.color == 0:
                                print_non_empty_sqr(mid_of_sqr, "P", even)
                            else:
                                print_non_empty_sqr(mid_of_sqr, "p", even)
                        case Pieces.King:
                            if sqr.color == 0:
                                print_non_empty_sqr(mid_of_sqr, "K", even)
                            else:
                                print_non_empty_sqr(mid_of_sqr, "k", even)
                        case Pieces.Queen:
                            if sqr.color == 0:
                                print_non_empty_sqr(mid_of_sqr, "Q", even)
                            else:
                                print_non_empty_sqr(mid_of_sqr, "q", even)
                        case Pieces.Rook:
                            if sqr.color == 0:
                                print_non_empty_sqr(mid_of_sqr, "R", even)
                            else:
                                print_non_empty_sqr(mid_of_sqr, "r", even)
                        case Pieces.Bishop:
                            if sqr.color == 0:
                                print_non_empty_sqr(mid_of_sqr, "B", even)
                            else:
                                print_non_empty_sqr(mid_of_sqr, "b", even)
                        case Pieces.Knight:
                            if sqr.color == 0:
                                print_non_empty_sqr(mid_of_sqr, "N", even)
                            else:
                                print_non_empty_sqr(mid_of_sqr, "n", even)
                print("|", end="")
            print()  # Newline at the end of the row
