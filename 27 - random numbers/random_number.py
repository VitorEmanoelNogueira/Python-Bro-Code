import random

low = 1
high = 100

options = ("rock", "paper", "scissors")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

number1 = random.randint(low, high)
number2 = random.random()
random.choice(options)
random.shuffle(cards)


print(number1)
print(number2)
print(options)
print(cards)