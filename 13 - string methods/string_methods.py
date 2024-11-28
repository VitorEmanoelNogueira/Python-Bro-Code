# dar print em help(str) mostra todos os métodos de string disponíveis

# len() -> Tamanho da String (inclui espaços)
# .find() -> Achar a primeira ocorrência de algo (o search)
# .rfind() -> Achar a última ocorrência de algo
# .capitalize() -> Deixar primeira letra maiúscula
# .upper -> Deixar tudo maiúsculo
# .lower -> Deixar tudo minúsculo
# .isdigit() -> Retorna true ou falso com base na string só ter digitos ou não
# .isalpha() -> Mesma coisa do isdigit, só que agora com letras (ter espaço faz retornar false também)
# .count() -> Conta o tanto de vezes que algo aparece na string
# .replace("elem", "novo_elem") -> Substituir qualquer ocorrência de string por outra

# name = input("Enter your full name: ")
# phone_number = input("Enter your phone number #: ")

# result = len(name)
# result1= name.find("o")
# result = name.rfind("o")
# name = name.capitalize()
# name = name.upper()
# name = name.lower()
# result = name.isdigit()
# result = name.isalpha()

# result = phone_number.count("-")
# result = phone_number.replace("-", " ")

# print(result)


#Exercise - Validate user input:
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter a username: ")

if len(username) > 12:
    print("Username must be under 12 characters.")
elif not username.find(" ") == -1:
    print("Username must not contain spaces.")
elif not username.isalpha():
    print("Username must not contain digits.")
else:
    print(f"Hello, {username}!")


