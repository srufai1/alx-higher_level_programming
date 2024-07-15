#!/usr/bin/python3


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a number and round to 3 decimal places.

    Args:
    matrix (list of lists): The matrix to be divided.
    div (int or float): The number by which to divide the elements.

    Returns:
    list of lists: A new matrix with elements divided by 'div' and rounded to 2 decimal places.

    Raises:
    TypeError: If 'matrix' is not a list of lists containing integers or floats,
                or if 'div' is not a number (integer or float).
    TypeError: If each row of the matrix does not have the same size.
    ZeroDivisionError: If 'div' is equal to 0.
    """

    # Check if 'matrix' is a list of lists containing integers or floats
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix)\
            or not all(isinstance(num, (int, float)) for row in matrix for num in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if each row of the matrix has the same size
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Check if 'div' is a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if 'div' is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide the elements of the matrix by 'div' and around to 2 decimal places
    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    return (new_matrix)