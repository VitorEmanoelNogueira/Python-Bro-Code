# used to test wheter a value or variable is foun in a sequence (string, list, tuple, set or dictionary)
# 1. in
# 2. not in

word = "APPLE"

letter = input("Guess a letter in the secret word: ")

if letter not in word:
    print(f"{letter} was not found")   
else:
   print(f"There is a {letter}")


students = {"Spongebob", "Patrick", "Sandy"}

student1 = input("Enter the name of a student: ")

if student1 in students:
    print(f"{student1} is a student")
else:
    print(f"{student1} was not found")


grades = {"Sandy": "A", "Squidward": "B", "Spongebob": "C", "Patrick" : "D"}

student2 = input("Enter the name of a student: ")

if student2 in grades:
    print(f"{student2}'s grade is {grades[student2]}")
else:
    print(f"{student2} was not found")


email = "BroCode@gmail.com"

if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")
