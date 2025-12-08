# area of circle

import math

pi = math.pi

radius = float(input("Enter radius of the circle (cm): "))
area = pi * (pow(radius, 2))
print(f"Area: {round(area,2)}cm²")
