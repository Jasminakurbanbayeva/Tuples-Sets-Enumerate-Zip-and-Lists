def check_common_elements(set1: set, set2: set) -> bool:
    """
    Check if two sets have any common elements.
    Args:
        set1 (set): First set of numbers
        set2 (set): Second set of numbers
    Returns:
        bool: True if sets have common elements, False otherwise
    """
    for i in set1:
        if i in set2:
            return True
    return False
print(check_common_elements(set1 = {1, 2, 3}, set2 = {4, 5, 3}))
