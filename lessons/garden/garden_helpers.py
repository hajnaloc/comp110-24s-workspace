"""Some functions for my garden plan!"""

__author__ = "730468225"


def add_by_kind(garden_dict: dict[str, list[str]], kind: str, plant: str) -> None:
    """Add by Kind Function!"""
    if kind in garden_dict:
        garden_dict[kind].append(plant)
    else:
        garden_dict[kind] = [plant]


def add_by_date(garden_dict: dict[str, list[str]], month: str, kind: str) -> None:
    """Add by Date Function!"""
    if month in garden_dict:
        garden_dict[month].append(kind)
    else:
        garden_dict[month] = [kind]


def lookup_by_kind_and_date(by_kind: dict[str, list[str]], by_date: dict[str, list[str]], kind: str, month: str) -> str:
    """Look up by kind & date Function!"""
    if kind not in by_kind or month not in by_date:
        return f'No {kind} to plant in {month}.'

    kind_plants = set(by_kind[kind])
    date_plants = set(by_date[month])

    plants_to_plant = kind_plants.intersection(date_plants)

    if plants_to_plant:
        return f'{kind} to plant in {month}: {list(plants_to_plant)}'
    else:
        return f'No {kind} to plant in {month}.'