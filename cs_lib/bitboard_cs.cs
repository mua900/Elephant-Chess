using System;
using System.ComponentModel;
using System.Data;
using System.Text.RegularExpressions;

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
    public static int[] bitboard_generator(char piece_to_search, string fen){
        int[] bitboard = new int[64];
        int brd_index = 0;
        for (int i = 0; i < fen.Length; i++){
            switch (fen[i]){
                case IsDigit(fen[i]):
                    brd_index += Convert.ToInt32(fen[i]) - 1;
                    continue;
                case 'K':
                    bitboard[1] = 0;
                    continue;
                default:
                    break;
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