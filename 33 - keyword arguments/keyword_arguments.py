def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

hello("Hello", "Mr.", "Spongebob", "Squarepants")
hello("Hello", last="Squarepants", title="Mr.", first="Spongebob")

for x in range(1, 11):
    print(x, end=" ")

print()

print("1", "2", "3", "4", "5", sep="-")


def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=2, area=321, first=789, last=5412)

print(phone_num)