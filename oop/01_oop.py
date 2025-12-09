# oop

from __car import Car

# object
car1 = Car("Mustang", 2025, "red", True)
print(car1.model, car1.year, car1.color, car1.for_sale)

car2 = Car("Corvette", 2024, "black", False)
print(car2.model, car2.year, car2.color, car2.for_sale)

car1.drive()
car2.stop()
