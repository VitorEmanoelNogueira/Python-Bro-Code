age = int(input("Enter your age: "))

if age >= 100:
    print("You are too old to sign up.")
elif age >= 18:
    print("You are now signed up!")
elif age < 0:
    print("You haven't been born yet lmaoooooo!")
else: 
    print("You must be 18+ to sign up!")


response = input("would you like food? (Y/N): ")

if response == "Y":
    print("Have some food!")
elif response == "N":
    print("No food for you!")
else:
    print("Please, enter Yes(Y) or No(N)!")


name = input("Type your name: ")

if name == "":
    print("You did NOT type your name!")
else:
    print(f"Hello, {name}!")