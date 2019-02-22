from math import pi

def circle_area(r):
    if type(r) not in [int, float]:
        raise TypeError("The radius must be be a non-negative real number")
    # if type(r) == str:
    #     raise TypeError("The radius cannot be a string")
    # if type(r) == bool:
    #     raise TypeError("The radius cannot be a boolean")
    # if type(r) == complex:
    #     raise TypeError("The radius cannot be a complex number")
    if r < 0:
        raise ValueError("The radius cannot be negative.")
    return pi*(r**2)
