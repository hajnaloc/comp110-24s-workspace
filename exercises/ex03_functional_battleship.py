
"""EX03 - Functional Battlehsip!"""

__author__ = "730468225"
import random


# Input Guess
def input_guess(size: int, guess_type: str) -> int:
    """Input guess function."""
    assert guess_type == "row" or guess_type == "column"

    guess: int = int(input(f"Guess a {guess_type}: "))

    while guess > size or guess < 1:
        guess = int(input(f"The grid is only {size} by {size}. Try again: "))

    return guess


# Print Grid
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"


def print_grid(size: int, row_guess: int, col_guess: int, is_correct: bool) -> None:
    """Print grid function."""
    row = 0
    while row < size:
        col = 0
        while col < size:
            if row + 1 == row_guess and col + 1 == col_guess:
                if is_correct:
                    print(RED_BOX, end='')
                else:
                    print(WHITE_BOX, end='')
            else:
                print(BLUE_BOX, end='')
            col += 1
        print()
        row += 1


# Correct Guess
def correct_guess(secret_row: int, secret_col: int, row_guess: int, col_guess: int) -> bool:
    """Correct guess function.""" 
    return secret_row == row_guess and secret_col == col_guess


# Main
def main(grid_size: int, secret_row: int, secret_col: int) -> None:
    """Main function."""
    turns = 5
    current_turn = 1

    while turns > 0:
        print(f"=== Turn {current_turn}/{5} ===")
        row_guess: int = input_guess(grid_size, "row")
        col_guess: int = input_guess(grid_size, "column")
        if correct_guess(secret_row, secret_col, row_guess, col_guess):
            print_grid(grid_size, row_guess, col_guess, True)
            print("Hit!")
            print(f"You won in {current_turn}/{5} turns!")
            return
        else:
            print_grid(grid_size, row_guess, col_guess, False)
            print("Miss!")
        turns -= 1
        current_turn += 1

# Print ""== Turn ==""
    print("X/5 - Better luck next time!")


if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))