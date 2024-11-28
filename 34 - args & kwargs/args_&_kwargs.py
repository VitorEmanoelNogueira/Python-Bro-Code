def add(*nums):
    total = 0
    for num in nums:
        total += num
    return total

print(add(1,2,3)) # 6
print(add(1,2,3,4,5)) # 15

print()

def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("Dr.", "Spongebob", "Harold", "Squarepants", "III")

print()
print()

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="123 Fake St.",
             apt="100",
             city="Detroit",
             state="MI",
             zip="54321")

print()

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')} {kwargs.get('state')}, {kwargs.get('zip')}")

# Manter a ordem de *args e **kwargs é necessário na chamada da função
shipping_label("Dr.", "Spongebob", "Squarepants", "III",
             street="123 Fake St.",
             pobox="PO box #1001",
             city="Detroit",
             state="MI",
             zip="54321")