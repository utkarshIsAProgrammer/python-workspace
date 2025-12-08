# calculator program

print("Operations: (+, -, *, /)")
operation = input("Choose an operation: ")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operation == "+":
    print(round(num1 + num2, 2))
elif operation == "-":
    print(round(num1 - num2, 2))
elif operation == "*":
    print(num1 * num2)
elif operation == "/":
    print(round(num1 / num2, 2))
else:
    print("Operation is invalid!")
