def replace_with_index(items: list) -> list:
    """
    Replace items in a list with their index using enumerate.
    Args:
        items (list): List of items to be replaced with indices
    Returns:
        list: List with items replaced by their indices
    """
    result=[]
    for i,x in enumerate(items):
        result.append(i)
    return result
print(replace_with_index(["a", "b", "c"]))
