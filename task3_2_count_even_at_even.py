def count_even_at_even(numbers: list) -> int:
    """
    Count how many even numbers are at even indexes.
    Args:
        numbers (list): List of integers
    Returns:
        int: Count of even numbers at even indexes
    """
    count=0
    for i,x in enumerate(numbers):
        if i % 2==0 and x % 2==0:
            count += 1
    return count
print(count_even_at_even([2, 4, 6, 3, 8]))
