"""EX04 - List Utility Functions!"""

__author__ = "730468225"


# All
def all(lst: list[int], num: int) -> bool:
    """All function!"""
    if not lst:
        return False 

    for element in lst:
        if element != num:
            return False  

    return True  


# Max
def max(lst: list[int]) -> int:
    """Max function!"""
    if not lst:
        raise ValueError("max() arg is an empty List")

    max_value = lst[0]
    for num in lst[1:]:
        if num > max_value:
            max_value = num

    return max_value


# is_equal
def is_equal(lst1: list[int], lst2: list[int]) -> bool:
    """Is Equal function!"""
    if len(lst1) != len(lst2):
        return False  

    for i in range(len(lst1)):
        if lst1[i] != lst2[i]:
            return False  

    return True  


# Extend
def extend(lst1: list[int], lst2: list[int]) -> None:
    """Extend function!"""
    for num in lst2:
        lst1.append(num)
