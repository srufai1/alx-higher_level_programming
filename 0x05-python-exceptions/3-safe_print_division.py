#!/usr/bin/python3
def safe_print_division(num1, num2):
    """Returns the division of a by b."""
    try:
        divide = num1 / num2
    except (TypeError, ZeroDivisionError):
        divide = None
    finally:
        print("Inside result: {}".format(divide))
    return (divide)
