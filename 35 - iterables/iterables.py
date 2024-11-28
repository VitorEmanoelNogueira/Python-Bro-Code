numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number, end=" - ")

print()

numbers = (1, 2, 3, 4, 5)


for number in numbers:
    print(number, end=" - ")


fruits = {"apple", "orange", "banana", "coconut"}

for fruit in fruits:
    print(fruit)

name = "Vitor Nogueira"

for character in name:
    print(character, end=" ")
print()

my_dictionary = {"A": 1, "B":2, "C": 3}

for key in my_dictionary:
    print(key)

for value in my_dictionary.values():
    print(value)

for key, value in my_dictionary.items():
    print(f"{key} = {value}")