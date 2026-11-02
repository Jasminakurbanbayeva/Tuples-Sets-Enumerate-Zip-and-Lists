def count_threes(numbers: tuple) -> int:
    """
    Count how many times 3 appears in the tuple.
    Args:
        numbers (tuple): A tuple of integers
    Returns:
        int: The count of number 3 in the tuple
    """
    a=numbers.count(3)
    return a
print(count_threes((1, 3, 3, 7, 3)))
