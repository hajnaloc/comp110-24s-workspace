"""Writing a Recursive Function!"""

__author__ = "730468225"


def f(n: int, k: int) -> int:
    """F Function for Recursive!"""
    if n == 0:  # Base case
        return 0
    else:  # Recursive rule
        return k + f(n - 1, k)
  


