"""Mutating functions."""

__author__ = "730468225"


# manual_append()
def manual_append(lst: list[int], num: int) -> None:
    """Manual append function."""
    lst.append(num)


# double()
def double(lst: list[int]) -> None:
    """Double function."""
    index = 0
    while index < len(lst):
        lst[index] *= 2
        index += 1
