from car import Car

car1 = Car("Mustang", 2024, "red", False)
car2 = Car("Corvette", 2025, "blue", True)

print(car1.model)
print(car2.year)

car1.drive()
car2.stop()

car1.describe()
car2.describe()