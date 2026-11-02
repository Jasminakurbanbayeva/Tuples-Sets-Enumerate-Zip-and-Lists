def count_apples(items: list) -> int:
    """
    Count how many times "apple" appears in a list.
    Args:
        items (list): List of strings
    Returns:
        int: Number of times "apple" appears in the list
    """
    count=0
    for i in items:
        if i =="apple":
            count += 1
    return count
print(count_apples(["apple", "banana", "apple","apple"]))
