import os
("cls || clear")

nota = float (input("digite uma nota"))

while nota < 0 or nota > 10:
    print("\nA nota deve ser maior ou igual a 0 e menor e igual a 10.")
    nota = float (input("digite uma nota: "))

print (f"Nota: {nota}")    