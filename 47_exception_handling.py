# exception handling

try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("Please enter a valid number.")
except ZeroDivisionError:
    print("You can't divide by zero.")
else:
    print("Result is", result)
finally:
    print("Execution complete.")
