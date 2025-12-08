# weight conversions program

weight = float(input("Enter your weight: "))
unit = input("Kg or Pounds (k/l):")

if unit == "k":
    weight = weight * 2.205
    unit = "lbs"
    print(f"You converted weight is {round(weight,2)} {unit}.")
elif unit == "l":
    weight = weight / 2.205
    unit = "kgs"
    print(f"You converted weight is {round(weight,2)} {unit}.")
else:
    print(f"{unit} is not a valid unit!")
