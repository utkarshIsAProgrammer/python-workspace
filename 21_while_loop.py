# while loop

age = int(input("Enter your age: "))

while age <= 0:
    print("Age can't be zero or negative!")
    age = int(input("Enter your age: "))

print(f"Your age is {age}.")
