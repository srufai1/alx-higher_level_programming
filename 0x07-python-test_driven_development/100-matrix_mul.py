#!/usr/bin/python3

def matrix_mul(m_a, m_b):
    """
    Multiply two matrices.

    Args:
        m_a (list): The first matrix (list of lists of integers or floats).
        m_b (list): The second matrix (list of lists of intgers or floats).

    Returns:
        list: The result of the matrix multiplication.

    Raises:
        TypeError: If m_a or m_b is not a list, not a list of lists,
        contains non-integer or non-float elements, or not a rectangle.
        ValueError: If m_a or m_b is empty or if they can't be multiplied.

    Example:
        >>> matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]])
        [[7, 10], [15, 22]]
    """
    if not isinstance(m_a, list) or not all(isinstance(row, list) for  row in m_a) \
            or not all(isinstance(num, (int, float)) for row in m_a for num in row):
                raise TypeError("m_a should contain only integers or floats")
    if not isinstance(m_b, list) or not all(isinstance(row, list) for row in m_b) \
            or not all(isinstance(num, (int, float)) for row in m_b for num in row):
                raise TypeError("m_b should contain only integers or floats")

    if not m_a or not m_b:
        raise ValueError("m_a can't be empty" if not m_a else "m_b can't be empty")

    num_cols_a = len(m_a[0])
    num_cols_b = len(m_b[0])

    if not all(len(row) == num_cols_a for row in m_a) or not all(len(row) == num_cols_b for row in m_b):
        raise TypeError("each row of m_a must be of the same size" if num_cols_a != num_cols_b else "each row of m_b must be of the same size")

    if num_cols_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]
    return (result)