"""Splitting a dictionary into two lists!"""

__author__ = "730468225"

# Get_Keys()


def get_keys(input_dict: dict[str, int]) -> list[str]:
    """Get Keys Definition!"""
    return list(input_dict.keys()) if input_dict else []


# Get_Values()

def get_values(input_dict: dict[str, int]) -> list[int]:
    """Get Values Definition!"""
    return list(input_dict.values()) if input_dict else []
