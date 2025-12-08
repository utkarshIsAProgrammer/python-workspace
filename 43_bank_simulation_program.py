# ank simulation program

balance = 0


def deposit(amount):
    global balance
    if amount > 0:
        balance += amount
        print(f"Deposited: ₹{amount}. New balance: ₹{balance}")
    else:
        print("Deposit amount must be positive.")


def withdraw(amount):
    global balance
    if 0 < amount <= balance:
        balance -= amount
        print(f"Withdrew: ₹{amount}. New balance: ₹{balance}")
    else:
        print("Insufficient balance or invalid amount.")


def display_balance():
    print(f"Current Balance: ₹{balance}")


if __name__ == "__main__":
    display_balance()
    deposit(500)
    withdraw(200)
    display_balance()
