def happy_birthday(name, age):
    print(f"Happy birthday to {name}!")
    print(f"You are {age} years old!")
    print(f"Happy Birthday to {name}!")
    print()

happy_birthday("Josue", 25)
happy_birthday("Marilda", 23)
happy_birthday("Sonic", 15)


def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")


display_invoice("BroCode", 42.50, "02/02")


def add(x, y):
    z = x + y
    return z

def subtract(x, y): 
    z = x - y
    return z

def multiply(x, y): 
    z = x * y
    return z

def divide(x, y): 
    z = x / y
    return z


print(add(1, 2))
print(subtract(1, 2))
print(multiply(1, 2))
print(divide(1, 2))

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return f"{first} {last}"

full_name = create_name("vitor", "nogueira")

print(full_name)