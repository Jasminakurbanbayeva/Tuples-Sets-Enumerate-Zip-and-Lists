def remove_first(lst: list) -> list:
    """
    Remove the first element from a list.
    Args:
        lst (list): The input list
    Returns:
        list: List with the first element removed
    """
    lst.pop(0)
    return lst
print(remove_first(["a", "b", "c"]))
