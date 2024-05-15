# Math Utils

import math

def approximately(a: float, b: float, tolerance: float) -> bool:
    if math.fabs(a - b) <= tolerance:
        return True
    else:
        return False

# Its name and type are descriptive enough about what this should return. This will be passed to the approximately above so
# adding a 4th parameter that will be passed in for that.
##TODO##
## There probably is a more optimal way to do this.##
def ratio_close_to_desired(a: float, b: float, desired_ratio:float, tol: float) -> bool:
    if a > b:
        bigger, lesser = a, b
    else:
        bigger, lesser = b, a

    if approximately(lesser/bigger * (1 / desired_ratio), 1, tol):
        return True
    else:
        return False
