def get_odd_indexed_items(items: list) -> list:
    """
    Print only items at odd indexes.
    Args:
        items (list): List of items
    Returns:
        list: Items at odd indexes
    """
    return items[1::2]
print(get_odd_indexed_items(["x", "y", "z", "w"]))
