def check_seven(numbers: tuple) -> bool:
    """
    Check if the number 7 exists in a tuple.
    Args:
        numbers (tuple): A tuple of integers
    Returns:
        bool: True if 7 is in the tuple, False otherwise
    """
    a=7
    if a in numbers:
        return True
    else:
        return False
print(check_seven((1, 2, 3, 4)))
