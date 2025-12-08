# list comprehension

squares = [x**2 for x in range(5)]
print(squares)

evens = [x for x in range(10) if x % 2 == 0]
print(evens)

labels = ["Even" if x % 2 == 0 else "Odd" for x in range(1, 6)]
print(labels)
