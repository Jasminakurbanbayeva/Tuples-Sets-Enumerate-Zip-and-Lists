def zip_three_lists(list1: list, list2: list, list3: list) -> list:
    """
    Zip three lists together.
    Args:
        list1 (list): First list
        list2 (list): Second list
        list3 (list): Third list
    Returns:
        list: List of tuples containing items from all three lists
    """
    result=[]
    for i in zip(list1,list2,list3):
        result.append(i)
    return result
print(zip_three_lists([1], [2], [3]))
