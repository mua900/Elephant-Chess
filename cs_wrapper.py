# Wrapper for our .cs libraries

import os
import pythonnet
import clr

crnt_dir = os.getcwd()
btbrd_dll_pth = os.path.join(crnt_dir, "cs_lib", "bin", "cs_lib.dll")

pythonnet.load("mono")
clr.AddReference(btbrd_dll_pth)
