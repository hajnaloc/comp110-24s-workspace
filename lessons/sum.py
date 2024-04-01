"""Summing the elements of a list using different loops!""" 

__author__ = "730468225"


# Part 1
def w_sum(vals: list[float]) -> float:
    """Calculates the sum of elements using a while loop."""
    total = 0.0
    index = 0
    while index < len(vals):
        total += vals[index]
        index += 1
    return total


# Part 2
def f_sum(vals: list[float]) -> float: 
    """Calculates the sum of elements using a for...in loop."""
    total = 0.0
    for val in vals:
        total += val
    return total


# Part 3
def f_range_sum(vals: list[float]) -> float: 
    """Calculates the sum of elements using a for...in range loop."""
    total = 0.0
    for index in range(len(vals)):
        total += vals[index]
    return total
