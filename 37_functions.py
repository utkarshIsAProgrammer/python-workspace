# functions


def hello(name: str):
    print("hello! " + name)
    print("have a nice day!")


hello("wtk")


# keyword arguments
def hello_2(first: str, middle: str, last: str):
    print(first, middle, last)


hello_2(last="k", first="w", middle="t")


# *args
def add(*numbers):
    all_sum = 0
    stuff = list(numbers)
    for i in stuff:
        all_sum += i
    return all_sum


print(add(1, 2, 5))


# **kwargs = parameter that will pack all arguments into dictionary
def hello_3(**name):
    print(f"Hello {name.get("first")} {name.get("last")}")


hello_3(first="Indie", last="Dev")
