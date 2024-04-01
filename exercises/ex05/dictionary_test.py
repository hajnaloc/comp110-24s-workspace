
"""EX06 - Dictionary Tests!"""

__author__ = "730468225"

from exercises.ex05.dictionary import invert, favorite_color, count, alphabetizer, update_attendance
import pytest

# Test invert function


def test_invert_expected_use_case_1() -> None:
    """Test invert function with use case!"""
    input_dict: dict[str, str] = {'a': 'b', 'c': 'd'}
    invert(input_dict)
    new_input_dict = {'b': 'a', 'd': 'c'}
    assert invert(input_dict) == new_input_dict


def test_invert_use_case_2() -> None:
    """Test invert function with use case!"""
    input_dict: dict[str, str] = {}
    inverted_dict = {}
    for key, value in input_dict.items():
        inverted_dict[value] = key
    new_input_dict = {}
    assert invert(input_dict) == new_input_dict


def test_invert_edge_case() -> None:
    """Testing invert function with edge case!"""
    input_dict: dict[str, str] = {'a': 'b', 'c': 'b', 'd': 'e'}
    with pytest.raises(KeyError):
        invert(input_dict)


# Test favorite color function
        
def test_favorite_color_use_case_1() -> None:
    """Favorite color with use case!"""
    color_dict = {"oceane": "yellow", "cha": "orange", "taman": "orange"}
    assert favorite_color(color_dict) == "orange"

    
def test_favorite_color_use_case_2() -> None:
    """Favorite color with use case!"""
    color_dict = {}
    with pytest.raises(ValueError):
        favorite_color(color_dict)


def test_favorite_color_edge_case() -> None:
    """Favorite color with edge case!"""
    color_dict = {"oceane": "yellow", "cha": "orange", "taman": "orange", "sri": "yellow"}
    assert favorite_color(color_dict) == "yellow"


# Test count function 

def test_count_use_case() -> None:
    """Count with use case!"""
    input_list = ["apple", "apple", "apple", "grape"]
    assert count(input_list) == {"apple": 3, "grape": 1}


def test_count_use_case_2() -> None:
    """Count with use case!"""
    input_list = ["apple", "juice", "basil", "grape"]
    assert count(input_list) == {"apple": 1, "juice": 1, "basil": 1, "grape": 1}


def test_count_edge_case() -> None:
    """Count with edge case!"""
    input_list = []
    assert count(input_list) == {}


# Test alph. function

def test_alphabetizer_use_case_1() -> None:
    """Aplh with use case!"""
    words_list = ["bone", "dog", "burrow", "elephant"]
    assert alphabetizer(words_list) == {"b": ["bone", "burrow"], "d": ["dog"], "e": ["elephant"]}


def test_alphabetizer_use_case_2() -> None:
    """Aplh with use case!"""
    words_list = ["bone", "dog", "elephant"]
    assert alphabetizer(words_list) == {"b": ["bone"], "d": ["dog"], "e": ["elephant"]}


def test_alphabetizer_edge_case() -> None:
    """Alph with edge case!"""
    words_list = []
    assert alphabetizer(words_list) == {}


# Test update attendance function

def test_update_attendance_use_case_1() -> None:
    """Update attendance with use case!"""
    attendance_dict = {"Monday": ["Sally", "Mark"], "Tuesday": ["Sally"]}
    day = "Tuesday"
    student = "Mark"
    update_attendance(attendance_dict, day, student)
    new_attendance_dict = {"Monday": ["Sally", "Mark"], "Tuesday": ["Sally", "Mark"]}
    assert attendance_dict == new_attendance_dict


def test_update_attendance_use_case_2() -> None: 
    """Update attendance with use case!"""
    attendance_dict = {"Monday": ["Sally", "Mark"], "Tuesday": ["Sally"]}
    day = "Wednesday"
    student = "Mark"
    update_attendance(attendance_dict, day, student)
    new_attendance_dict = {"Monday": ["Sally", "Mark"], "Tuesday": ["Sally"], "Wednesday": ["Mark"]}
    assert attendance_dict == new_attendance_dict


def test_update_attendance_edge() -> None:
    """Update attendance with edge case!"""
    attendance_dict = {}
    day = "Wednesday"
    student = "Mark"
    update_attendance(attendance_dict, day, student)
    new_attendance_dict = {"Wednesday": ["Mark"]}
    assert attendance_dict == new_attendance_dict
