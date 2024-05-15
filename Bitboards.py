# All the bitboards we are going to create will live here.

#
""" This will probably be removed """
#


import FEN


def bitboard_generator (piece_to_search: str, board: str) -> int:
    if len(piece_to_search) != 1 or piece_to_search.lower() not in "kqnbrp":
        return -1
    bitboard: int = 0
    index_count: int = 0
    for square in board:
        if square.isnumeric():
            index_count += int(square)
        elif square == piece_to_search:
            bitboard |= (1 << index_count)
            index_count += 1
        elif square.isalpha():
            index_count += 1
        elif square == "/":
            continue
        else:
            print("Issue with the provided FEN from Bitboards.bitboard_generator()")
    return bitboard  # Works correctly after a painful dealing with binary representations

# experiment
print(bin(bitboard_generator("P", FEN.fen_refine("rnb1kbnr/ppp2ppp/8/3pp1N1/2qPP3/8/PPP2PPP/R1BQKBNR w KQkq - 0 1")[2])))
