# quiz game

questions = (
    "What is the capital of India?",
    "Which planet is known as the Red Planet?",
    "What is the largest mammal on Earth?",
)

options = (
    ("A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"),
    ("A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"),
    ("A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Hippopotamus"),
)

answers = ("B", "B", "B")

# Game logic
guesses = []
score = 0
question_num = 0

for question in questions:
    print("\n" + question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter your answer (A, B, C, D): ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

    question_num += 1

print(f"\nYour score: {score}/{len(questions)}")
