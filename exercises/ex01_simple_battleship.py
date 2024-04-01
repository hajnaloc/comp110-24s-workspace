"""EX01 - Simple Battleship"""

__author__ = "730468225"

# User 1
user_value: int = input("Pick a secret boat location between 1 and 4: ")
if int(user_value) < 1:
    print("Error! " + user_value + " too low!")
elif int(user_value) > 4:
    print("Error! " + user_value + " too high!")

# User 2
user2_value: int = input("Guess a number between 1 and 4:")
if int(user2_value) < 1:
    print("Error! " + user2_value + " too low!")
elif int(user2_value) > 4:
    print("Error! " + user2_value + " too high!")
    
# Printing string of boxes
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

# Checking user input for match
if int(user_value and user2_value) == 1:
    print(f"{RED_BOX}{BLUE_BOX}{BLUE_BOX}{BLUE_BOX}")
elif int(user_value and user2_value) == 2:
    print(f"{BLUE_BOX}{RED_BOX}{BLUE_BOX}{BLUE_BOX}")  
elif int(user_value and user2_value) == 3:
    print(f"{BLUE_BOX}{BLUE_BOX}{RED_BOX}{BLUE_BOX}")   
elif int(user_value and user2_value) == 4:
    print(f"{BLUE_BOX}{BLUE_BOX}{BLUE_BOX}{RED_BOX}")
else:
    exit()

if int(user2_value) == int(user_value):
    print("Correct! You hit the ship.")
else:
    print("Incorrect! You missed the ship.")
