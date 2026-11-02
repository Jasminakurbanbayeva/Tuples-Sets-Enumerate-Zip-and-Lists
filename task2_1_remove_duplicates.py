def remove_duplicates(numbers: list) -> set:
    """
    Remove duplicates from a list using a set.
    Args:
        numbers (list): A list of numbers with possible duplicates
    Returns:
        set: A set containing unique numbers from the input list
    """
    return set(numbers)
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))
