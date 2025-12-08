# temperature converter program

unit = input("It's the temperature in celsius or fahrenheit (c/f): ")
temp = float(input("Enter the temperature: "))

if unit == "c":
    temp = (temp * (9 / 5)) + 32
    print(f"Converted temperature is {round(temp,2)}°F")
elif unit == "f":
    temp = (temp - 32) * (5 / 9)
    print(f"Converted temperature is {round(temp,2)}°C")
else:
    print(f"{unit} is not a valid measure!")
