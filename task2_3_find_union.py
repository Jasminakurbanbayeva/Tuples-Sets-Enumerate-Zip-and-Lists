def find_union(set1: set, set2: set) -> set:
    """
    Find the union of two sets.
    Args:
        set1 (set): First set of numbers
        set2 (set): Second set of numbers
    Returns:
        set: Union of both sets
    """
    return set(list(set1) + list(set2))
print(find_union({1, 2}, {2, 3}))
