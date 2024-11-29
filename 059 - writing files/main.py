# Python writting files (.txt, .json, .csv)
import json
import csv

txt_data = "I like pizza!"
file_path = "output.txt"

# try:
#     with open(file=file_path, mode="x") as file: 
#         file.write(txt_data)
#         print(f"txt file '{file_path}' was created")
# except FileExistsError:
#     print(f"File '{file_path}' already exists!")

# try:
#     with open(file=file_path, mode="a") as file: 
#         file.write("\n" + txt_data)
#         print(f"txt file '{file_path}' was created")
# except FileExistsError:
#     print(f"File '{file_path}' already exists!")


# employees = ["Eugene", "Squidward", "Spongebob", "Patrick"]
# file_path = "employees.txt"

# try: 
#     with open(file_path, "w") as file:
#         for employee in employees:
#             file.write(employee + ", ")
#         print(f"txt file '{file_path}' was created")
# except FileExistsError:
#     print("That file already exists!")


# employee = {
#     "Name": "Spongebob",
#     "Age": 30,
#     "Job": "Cook" 
# }
# file_path = "output.json"

# try: 
#     with open(file_path, "w") as file:
#         json.dump(employee, file, indent=4)
#         print(f"json file '{file_path}' was created")
# except FileExistsError:
#     print("That file already exists!")

employees = [["Name", "Age", "Job"],
             ["Spongebob", 30, "Cook"],
             ["Patrick", 38, "Unemployed"],
             ["Sandy", 27, "Scientist"]]

file_path = "output.csv"

try: 
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!")
