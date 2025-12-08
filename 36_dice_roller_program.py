# dice roller program

import random

dice_art = {
    1: ("┌─────────┐", "│         │", "│    ●    │", "│         │", "└─────────┘"),
    2: ("┌─────────┐", "│  ●      │", "│         │", "│      ●  │", "└─────────┘"),
    3: ("┌─────────┐", "│  ●      │", "│    ●    │", "│      ●  │", "└─────────┘"),
    4: ("┌─────────┐", "│  ●   ●  │", "│         │", "│  ●   ●  │", "└─────────┘"),
    5: ("┌─────────┐", "│  ●   ●  │", "│    ●    │", "│  ●   ●  │", "└─────────┘"),
    6: ("┌─────────┐", "│  ●   ●  │", "│  ●   ●  │", "│  ●   ●  │", "└─────────┘"),
}


def roll_dice():
    roll = random.randint(1, 6)
    print("\nYou rolled:")
    for line in dice_art[roll]:
        print(line)
    return roll


print("Welcome to the Dice Roller!")
while True:
    input("Press Enter to roll the dice (or type 'quit' to exit): ")
    roll = roll_dice()
    if input("Roll again? (y/n): ").lower() != "y":
        break
print("Thanks for playing!")
