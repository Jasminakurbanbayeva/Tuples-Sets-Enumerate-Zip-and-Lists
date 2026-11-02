def create_dict_from_list(items: list) -> dict:
    """
    Create a dictionary from a list using enumerate.
    Args:
        items (list): List of items
    Returns:
        dict: Dictionary with indices as keys and items as values
    """
    result={}
    for i,x in enumerate(items):
        result[i]=x
    return result
print(create_dict_from_list(["cat", "dog", "fish"]))
