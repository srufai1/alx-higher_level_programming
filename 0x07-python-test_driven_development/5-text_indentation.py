#!/usr/bin/python3

"""
    Print text with 2 new lines after each of the characters '.', '?' and ':'.
"""
def text_indentation(text):
    """
    Print text with 2 new lines after each of the characters '.', '?' and ':'.

    
    Args:
    text (str): The input text.

    Raises:
    TypeError: If 'text' is not a string.

    Returns:
    None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Initialize a flag to avoid extra new lines after these characters
    flag = False

    for char in text:
        if char in ".?:":
            print(char)
            print()
            flag = True
        else:
            if flag and char == " ":
                continue
            else:
                print(char, end="")
                flag = False
    print()