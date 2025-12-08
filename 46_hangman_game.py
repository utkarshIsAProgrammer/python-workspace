# hangman game


import random
from __hangman_art import hangman_art
from __hangman_words import words

secret = random.choice(words)
guessed = []
wrong = []
lives = 10


def get_display_word(secret, guessed):
    result = ""
    for ch in secret:
        if ch in guessed:
            result += ch + " "
        else:
            result += "_ "
    return result.strip()


while True:
    print("\n" + hangman_art[len(wrong)])
    print("Word:", get_display_word(secret, guessed))
    print("Wrong letters:", " ".join(wrong))
    print("Lives left:", lives)

    if all(ch in guessed for ch in secret):
        print("You won! The word was:", secret)
        break
    if lives == 0:
        print("You lost! The word was:", secret)
        break

    guess = input("Enter a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue
    if guess in guessed or guess in wrong:
        print("You already tried that letter.")
        continue

    if guess in secret:
        guessed.append(guess)
    else:
        wrong.append(guess)
        lives -= 1
