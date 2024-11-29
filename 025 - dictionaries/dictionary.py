capitals = {"USA": "Washington D.C.",
            "India": "New Delhi", 
            "China": "Beijing",
            "Russia": "Moscow"}

print(capitals.get("USA")) # Washington D.C.

print("----------------------")

print(capitals.get("Japan")) # None

if capitals.get("Russia"):
    print("That capital exists")
else: 
    print("That capital doesn't exist")

print("----------------------")


capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "Detroit"})
capitals.pop("China")
capitals.popitem()
capitals.update({"Germany": "Berlin"})

keys = capitals.keys() # Retorna todas as chaves no dicionário (se asemelha uma lista)

print(keys)

print("----------------------")

for key in capitals.keys():
    print(key)

print("----------------------")

values = capitals.values() #Retorna os valores (se asemelha uma lista)

for value in capitals.values():
    print(value)

print("----------------------")

items = capitals.items() # Retorna um objeto de um dicionário que se assemelha a uma lista 2d com tuples dentro
for key, value in capitals.items():
    print(f"{key}: {value}")

capitals.clear()