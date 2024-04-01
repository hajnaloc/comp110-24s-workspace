"""EX02 - One Shot Battlehsip!"""

__author__ = "730468225"

# Establish a secret
grid_size = 4
secret_row = 3
secret_column = 2

# Prompt for a Guess
user_row_guess = int(input("Guess a row: "))

while user_row_guess < 1 or user_row_guess > grid_size :
    user_row_guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

user_column_guess = int(input("Guess a column: "))

while user_column_guess < 1 or user_column_guess > grid_size:
    user_column_guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

# Print a Grid
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

row_counter = 1
result = str("")

while row_counter <= grid_size:
    row_str = ""
    column_counter = 1

    if user_row_guess == row_counter:
        # Check if the current position matches the user's guess
        while column_counter <= grid_size:
            if user_column_guess == column_counter:
                if user_column_guess == secret_column:
                    result = RED_BOX  # Correct guess: red box
                else: 
                    result = WHITE_BOX # Wrong guess:2
                row_str += result
            else:
                row_str += BLUE_BOX
            column_counter += 1
    else:
        while column_counter <= grid_size:
            row_str += BLUE_BOX  # Other positions: blue box
            column_counter += 1

    print(row_str)
    row_counter += 1

# Giving a hint to user
if user_row_guess == secret_row and user_column_guess == secret_column:
    print("Hit!")
elif user_row_guess == secret_row:
    print("Close! Correct row, wrong column.")
elif user_column_guess == secret_column:
    print("Close! Correct column, wrong row.")
else:
    print("Miss!")
