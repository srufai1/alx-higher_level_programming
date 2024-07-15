#!/usr/bin/python3

def print_square(size):
    """
    Print a square with the character '#' based on the given size.

    Args:
    size (int): The size (side length) of the square.

    Raises:
    TypeError: If 'size' is not an integer or it it's a float less than 0.
    ValueError: If 'size' is less than 0.

    Returns:
    None
    """
    if not isinstance(size, int):
        if isinstance(size, float) and size < 0:
            raise TypeError("size must be an integer")
        else:
            raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)