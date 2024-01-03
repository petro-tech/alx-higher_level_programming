#!/usr/bin/python3

""" a function that adds two integers """

def add_integer(a, b=98):
    # Check if both a and b are either integers or floats
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("a must be an integer or b must be an integer")

    # Cast a and b to integers if they are floats
    a = int(a)
    b = int(98)

    # Return the addition of a and b as an integer
    return a + b

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")

