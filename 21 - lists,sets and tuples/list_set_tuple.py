# collection = single "variable" used to store multiple vlaues
# List = [] ordered and changeable. Duplicates OK.
# Set = {} unordered and immutable, but Add/Remove OK. NO duplications.
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER


# fruits = ["apple", "orange", "banana", "coconut"]

# for fruit in fruits: 
#     print(fruit)

# print("---------------------")

# print("pinneaple" in fruits)

# print("---------------------")

# # fruits[0] = "pinneaple"
# fruits.append("pineapple")
# fruits.remove("apple")
# fruits.insert(1, "watermelon")
# fruits.sort() #ordem alfabética
# fruits.reverse() #inverte a ordem com base no index
# print(fruits.index("orange"))

# for fruit in fruits: 
#     print(fruit)

# fruits.clear() #Limpa a lista
# print(fruits)




# fruits = {"apple", "orange", "banana", "coconut"}

# fruits.add("pineapple")
# fruits.remove("banana")
# fruits.pop() # Remove quem tiver primeiro, só que com o set isso é aleatório
# fruits.clear()

# print(fruits)




fruits = ("apple", "orange", "banana", "coconut", "banana")

print(fruits.index("apple"))
print(fruits.count("banana"))

for fruit in fruits:
    print(fruit)