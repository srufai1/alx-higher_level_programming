#!/usr/bin/python3
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy's matmul function.
    
    Args:
    m_a: The first matrix.
    m_b: The second matrix.
    
    Returns:
    The result of the matrix multiplication.
    
    Raises:
    TypeError: If m_a or m_b is not a list or contains elements that are not lists.
    ValueError: If m_a or m_b is empty, or if the matrices cannot be multiplied.
    """
    # Check if m_a and m_b are lists of lists
    if not isinstance(m_a, list) or not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not isinstance(m_b, list) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    
    # Check if m_a and m_b are empty
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    
    # Check if all elements in m_a and m_b are integers or floats
    if not all(isinstance(element, (int, float)) for row in m_a for element in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(element, (int, float)) for row in m_b for element in row):
        raise TypeError("m_b should contain only integers or floats")
    
    # Check if the number of columns in m_a is equal to the number of rows in m_b
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result = np.matmul(m_a, m_b)

    return result.tolist()
