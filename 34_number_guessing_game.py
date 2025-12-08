# number guessing game
import random

secret_number = random.randint(1, 100)
chances = 10

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 100. You have 10 chances.")

for attempt in range(1, chances + 1):
    guess = int(input(f"Attempt {attempt}: Enter your guess: "))

    if guess == secret_number:
        print(f"Congratulations! You guessed it in {attempt} attempts.")
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")
else:
    print(f"Sorry, you've used all your chances. The number was {secret_number}.")
