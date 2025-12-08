age = int(input("Enter your age: "))

# conditional statements
if age > 120:
    print("You are too old to watch this content!")
elif age >= 18:
    print("You can watch this movie.")
elif age < 0:
    print("You don't exist in this world!")
else:
    print("You cannot watch this movie")
