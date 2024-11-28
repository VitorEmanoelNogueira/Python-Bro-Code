import math

# x = 9.9

# print(math.pi) 
# print(math.e) 
# result = math.sqrt(x) # Raiz
# result = math.ceil(x) # Arredondar um número para cima SEMPRE, mesmo que só tenha .1
# result = math.floor(x) # Sempre arredonda números para baixo

# print(result)


# # Calc of a circuference of a circle
radius = float(input("Enter the radius of a circle: "))
circumference = 2 * math.pi * radius
print(f'The circumference is: {round(circumference, 2)}cm')

# #Calc of the area
area = math.pi * pow(radius, 2)
print(f'The area of the circle is: {round(area, 2)}cm²')

#Calc of the hypotenuse of a right triangle
a = float(input("Enter side A: "))
b = float(input("Enter side B: "))
c = math.sqrt((pow(a, 2) + pow(b, 2)))

print(f"Side C = {c}")