using System;
using System.ComponentModel;

namespace cs_lib;

public class Bitboard
{
    // Bitboards will live and delt with here.
    public static int bitboard_generator(char piece_to_search, string board){

        // Necesarry checks for valid inputs into function
        if (!"KkQqRrBbNnPp".Contains(piece_to_search)){
            Console.WriteLine("There is a problem with the piece we are searching on the board! - cs_Library>Bitboards>bitboard_generator");
        }

        int bitboard = 0;
        for (int i = 0; i < board.Length; i++){
            if (char.IsDigit(board[i])){
                i += (int)board[i] - 1;
            }

            if (board[i] == piece_to_search){
                bitboard |= 1 << i;
            }
        }
        return bitboard;
    }
}
