using System;
using System.ComponentModel;

/*
Explaining all var names above will be exhausting. All will be named according to this table where the most of the things are represented with a single later. Var names will be consturusted from these.

W = white
B = black

p = pawn
n = knight
k = king
q = queen
b = bishop
r = rook

bt = bitboard
*/

// 0 is white, black is supposed to be one but can be anything else

namespace cs_lib{
public class Bitboard
{
    // Bitboards will live and delt with here.
    public static int bitboard_generator(char piece_to_search, string board){

        // Necessary checks for valid inputs into function
        if (!"KkQqRrBbNnPp".Contains(piece_to_search)){
            Console.WriteLine("There is a problem with the piece we are searching on the board! - cs_Library>Bitboard>bitboard_generator");
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

public class Move_Generator(){
    // TODO -> look up here.

    public void Pawn_Moves(int W_bt, int B_bt, int Wp_bt, int Bp_bt, int color){
        int dir;
        int color_bt;
        int color_p_bt;
        if (color == 0){
            dir = 1;
            color_bt = W_bt;
            color_p_bt = Wp_bt;
        }
        else{
            dir = -1;
            color_bt = B_bt;
            color_p_bt = B_bt;
        }
    }
}
}