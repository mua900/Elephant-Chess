# Math Utils

def approximately(a: float, b: float, tolerance: float) -> bool:
    return abs(a - b) <= tolerance


# Its name and type are descriptive enough about what this should return. This will be passed to the approximately
# above so adding a 4th parameter that will be passed in for that.

# noinspection GrazieInspection // editors thing I don't know
def ratio_close_to_desired(a: float, b: float, desired_ratio: float, tol: float) -> bool:
    # The a here is the bigger number, b is the lesser.
    # Since naming parameters as bigger and lesser would be confusing, we take two numbers given to us and set them
    # as we want.
    if a < b:
        a, b = b, a

    if desired_ratio < 1:
        desired_ratio = 1 / desired_ratio

    # If two ratios, say a/b and c/d, are close to each other then a/b * d/c or b/a * c/d should be close to 1
    # So we ensure a/b is less than and desired_ratio is bigger than one to compare the result of multiplication with
    # one.

    return approximately(b/a * desired_ratio, 1, tol)
