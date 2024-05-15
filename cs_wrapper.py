# Wrapper for our .cs libraries

import ctypes

cs_Library = ctypes.CDLL(".\\cs_lib\\bin\\Debug\\net8.0\\cs_lib.dll")

def bitboard():
    bitboard_generate = cs_Library.bitboard_generator()
