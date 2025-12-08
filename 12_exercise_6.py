# hypotenuse of a right angled triangle

import math

a = float(input("Enter side A (cm): "))
b = float(input("Enter side B (cm): "))

hypotenuse = round(math.sqrt(pow(a, 2) + pow(b, 2)), 2)
print(f"Hypotenuse: {hypotenuse}cm")
