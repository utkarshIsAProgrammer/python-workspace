# random module

import random

# random integer
print(random.randint(1, 10))
print(random.randrange(10))

# random float
print(random.random())
print(random.uniform(1, 10))

# random selection
choices = ["apple", "banana", "cherry", "date"]
print(random.choice(choices))
print(random.sample(choices, 2))

# random shuffle
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)
