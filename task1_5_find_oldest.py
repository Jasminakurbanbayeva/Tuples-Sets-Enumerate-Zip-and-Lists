def find_oldest(people: list) -> tuple:
    """
    Find the oldest person from a list of tuples (name, age).
    Args:
        people (list): List of tuples containing (name, age) pairs
    Returns:
        tuple: A tuple containing (name, age) of the oldest person
    """
    # if people[0]>people[1]:
    #     return people[0]
    # elif people[1]>people[0]:
    #     return people[1]
    # elif people[2]>people[1]:
    #     return people[2]
    # a=person[0]
    # b=oldest[0]
    a=people[0]
    for i in people:
        if i[1]>a[1]:
            a=i
            
    return a        
        
        
print(find_oldest([("Ali", 200), ("Sara", 30), ("John", 220)]))    