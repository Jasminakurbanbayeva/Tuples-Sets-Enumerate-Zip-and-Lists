def combine_lists(list1: list, list2: list) -> list:
    """
    Combine two lists into a list of tuples using zip.
    Args:
        list1 (list): First list of items
        list2 (list): Second list of items
    Returns:
        list: List of tuples containing paired items from both lists
    """
    result=[]
    for i in zip(list1,list2):
        result.append(i)
    return result
print(combine_lists([1, 2], ["a", "b"]))
