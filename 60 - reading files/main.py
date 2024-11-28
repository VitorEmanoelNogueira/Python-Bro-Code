import json
import csv

# file_path = "D:/Users/Vitor/Desktop/Cursos/Python - Bro Code/59 - writing files/output.txt"

# try:
#     with open(file_path, "r") as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print("File not found!")
# except PermissionError:
#     print("YOu do not have permission to read that file!")

# file_path = "D:/Users/Vitor/Desktop/Cursos/Python - Bro Code/59 - writing files/output.json"

# try:
#     with open(file_path, "r") as file:
#         content = json.load(file)
#         print(content["Name"])
# except FileNotFoundError:
#     print("File not found!")
# except PermissionError:
#     print("You do not have permission to read that file!")

file_path = "D:/Users/Vitor/Desktop/Cursos/Python - Bro Code/59 - writing files/output.csv"

try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line[2])
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("You do not have permission to read that file!")