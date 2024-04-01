"""EX05 - Dictionary!"""

__author__ = "730468225"

# Invert


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Invert Definiton!"""
    inverted_dict = {}
    for key, value in input_dict.items():
        if value in inverted_dict:
            raise KeyError(f"Duplicate value '{value}' encountered while inverting the dictionary.")
        inverted_dict[value] = key
    return inverted_dict


# Favorite Colors


def favorite_color(color_dict: dict[str, str]) -> str:
    """Favorite Color Definition!"""
    if not color_dict:
        raise ValueError
    
    def key_function(color: str) -> str:
        return color_counts[color], -first_appearance[color]
    color_counts: dict[str, int] = {}
    first_appearance: dict[str, int] = {}

    for name, color in color_dict.items():
        color_counts[color] = color_counts.get(color, 0) + 1
        if color not in first_appearance:
            first_appearance[color] = len(first_appearance)

    most_popular_color = max(color_counts, key=key_function)

    return most_popular_color


# Count


def count(input_list: list[str]) -> dict[str, int]:
    """Count Definition!"""
    result_dict: dict[str, int] = {}
    for item in input_list:
        if item in result_dict:
            result_dict[item] += 1
        else:
            result_dict[item] = 1
    return result_dict


# Aplhabetizer


def alphabetizer(words_list: list[str]) -> dict[str, list[str]]:
    """Aplhabetizer definition!"""
    result_dict: dict[str, list[str]] = {}
    for word in words_list:
        first_letter = word[0].lower()
        if first_letter in result_dict:
            result_dict[first_letter].append(word)
        else:
            result_dict[first_letter] = [word]
    return result_dict


# Update_Attendance


def update_attendance(attendance_dict: dict[str, list[str]], day: str, student: str) -> None:
    """Updates attendance Definition!"""
    if day in attendance_dict:
        attendance_dict[day].append(student)
    else:
        attendance_dict[day] = [student]
    
    return None
