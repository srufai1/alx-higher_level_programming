#!/usr/bin/python3
"""
    Insert here module comment
"""

def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
    a (int): The first integer to be added.
    b (int, optional): The second integer to be added. Default is 98.

    Returns:
    int: THe sum of a and b.

    Raises:
    TypeError: If a or b is not an integer or a float that cannot be cast to an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return (a + b)