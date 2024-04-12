"""Functions that implement sorting algorithms."""

__author__ = "730468225"


def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm. Insert into an already sorted list."""
    n = len(x)
    for i in range(1, n):
        current_element = x[i]
        j = i - 1
        while j >= 0 and x[j] > current_element:
            x[j + 1] = x[j]
            j -= 1
        x[j + 1] = current_element 
    return None 


def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm. Repeatedly find the minimum and swap it."""
    n = len(x)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if x[j] < x[min_index]:
                min_index = j
        x[i], x[min_index] = x[min_index], x[i]
    return None
    