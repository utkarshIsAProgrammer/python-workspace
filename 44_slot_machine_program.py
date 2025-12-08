# slot machine program

import random

symbols = ["🍒", "🍋", "🔔", "⭐", "7"]


def spin_row():
    return [random.choice(symbols) for _ in range(3)]


def print_row(row):
    print(" | ".join(row))


def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "7":
            return bet * 20
        elif row[0] == "⭐":
            return bet * 10
        elif row[0] == "🔔":
            return bet * 5
        else:
            return bet * 3
    else:
        return 0


def main():
    balance = 100
    print("Welcome to the Slot Machine!")

    while balance > 0:
        print(f"Current balance: ₹{balance}")
        bet = input("Place your bet (or 'q' to quit): ")

        if bet.lower() == "q":
            break

        if not bet.isdigit():
            print("Please enter a valid number.")
            continue

        bet = int(bet)
        if bet <= 0 or bet > balance:
            print("Invalid bet amount.")
            continue

        balance -= bet
        row = spin_row()
        print_row(row)

        payout = get_payout(row, bet)
        if payout > 0:
            print(f"You won ₹{payout}!")
            balance += payout
        else:
            print("No win this time.")

    print(f"Game over! Final balance: ₹{balance}")


if __name__ == "__main__":
    main()
