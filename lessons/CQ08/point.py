"""CQ08: Pizza activity!"""
from __future__ import annotations
__author__ = "730468225"


class Point:
    """Method that returns its own point, made up of three defitions!"""

    def __init__(self, x_init: float, y_init: float):
        """Constructor that assigns inital values!"""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Mutates a point method, scale_by definition!"""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Creates a new point method, scale definition!"""
        new_x = self.x * factor
        new_y = self.y * factor
        return Point(new_x, new_y)