# indexing = accessing elements of a sequence using [] (indexing operator)
# [start : end : step]

credit_number = "1234-5678-9012-3456"

print(credit_number[3])
print(credit_number[:4]) # Só ter o end, faz supor que o que está antes dos dois pontos é um 0
print(credit_number[5:9]) # pega do index 5 ao 9
print(credit_number[5:]) #pega do 5 até o final
print(credit_number[-1]) #pega o último digito (sim, dá pra usar números negativos)
print(credit_number[::2]) #Vai pegar do começo ao fim, já que o start e end estão vazios, pulando de 2 em 2 (step)

last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")

credit_number = credit_number[::-1] #Inverte a string
print(credit_number)