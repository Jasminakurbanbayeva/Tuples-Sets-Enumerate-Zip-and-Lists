def print_with_index(items: list) -> None:
    """
    Use enumerate to print each item in a list with its index.
    Args:
        items (list): List of items to print with their indices
    Returns:
        None: Prints each item with its index
    """
    for i in enumerate(items):
        print(i) 
print(print_with_index(["apple", "banana", "cherry"]))
