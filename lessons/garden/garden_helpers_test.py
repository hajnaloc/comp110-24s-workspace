"""Test my garden functions."""

__author__ = "730468225"

import unittest
from garden_helpers import add_by_kind, add_by_date, lookup_by_kind_and_date

test_add_by_kind_edge_case() -> None:
 """Test add_by_kind function edge case!"""
by_kind = {}
new_plant_kind = "Tree"
new_plant = "Oak"
add_by_kind(by_kind, new_plant_kind, new_plant)
new_by_kind = {"Tree": ["Oak"]}
assert by_kind == new_by_kind
    
test_add_by_kind_use_case() -> None:
"""Testing the add_by_kind function use case!"""
by_kind = {"Flower" : ["marigold", "tulip"]}
new_plant_kind = "Flower"
new_plant = "daisy"
add_by_kind(by_kind, new_plant_kind, new_plant)
new_by_kind = {"Tree": ["Oak"]}
assert by_kind == new_by_kind


test_add_by_date_edge_case() -> None:
"""Test add_by_date function edge case!"""
garden_by_date = {}
month = "January"
plant = "Rose"
add_by_date(garden_by_date, month, plant)
new_garden_by_date = {"Janurary": ["Rose"]}
assert garden_by_date == new_garden_by_date

test_add_by_date_use_case() -> None:
"""Test add_by_date function use case!"""
garden_by_date = {"March": ["Tulip"]}
month = "March"
plant = "Rose"
add_by_date(garden_by_date, month, plant)
new_garden_by_date = {"March": ["Tulip", "Rose"]}
assert garden_by_date == new_garden_by_date


test_lookup_by_kind_and_date():
"""Test lookup_by_kind_and_date function with edge cases!."""


if __name__ == '__main__':
    unittest.main()