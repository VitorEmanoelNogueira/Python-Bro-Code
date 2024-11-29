#Typecasting = the process of converting a variable from one data type to another
# str(), int(), float(), bool()

name = ""
age = 20
gpa = 3.5
is_student = True

print(age)
age = float(age)
print(age)

print(type(age))
age = str(age)
print(age)
print(type(age))


print(gpa)
gpa = int(gpa)
print(gpa)

print(name)
name = bool(name)
print(name)