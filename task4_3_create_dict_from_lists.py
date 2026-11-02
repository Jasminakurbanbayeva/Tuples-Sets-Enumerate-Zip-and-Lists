def create_dict_from_lists(keys: list, values: list) -> dict:
    """
    Create a dictionary from two lists.
    Args:
        keys (list): List of keys for the dictionary
        values (list): List of values for the dictionary
    Returns:
        dict: Dictionary created from the two lists
    """
    result=[]
    for i,x in zip(keys,values):
        result[i]=x
    return result 
print(create_dict_from_lists(["name", "age"], ["Alice", 30]))
