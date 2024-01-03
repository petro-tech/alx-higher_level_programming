#!/usr/bin/python3

""" Prints a square """

def print_square(size):
    # Check if size is an integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # Check if size is greater than or equal to 0
    if size < 0:
        raise ValueError("size must be >= 0")

    # Check if size is an integer (not a float)
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    # Print the square
    for _ in range(size):
        print("#" * size)
