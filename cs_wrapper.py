# Wrapper for our .cs libraries
# We will see if I can do this with pythonnet and mono

import os
import pythonnet
import clr

crnt_dir = os.getcwd()
btbrd_dll_pth = os.path.join(crnt_dir, "cs_mono", "bitboard.dll")

pythonnet.load("mono")
clr.AddReference(btbrd_dll_pth)
