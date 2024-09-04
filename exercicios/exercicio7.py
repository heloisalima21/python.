import os
os.system ("cls || clear")

while True:
    primeira_nota = float(input("Digite primeira nota: "))
    segunda_nota = float  (input("Digite  segunda nota: "))

    if (primeira_nota < 0 or primeira_nota > 10) or (segunda_nota < 0 or segunda_nota > 10):
       print ("\nA nota deve ser maior ou igual a 0 e menor e igual a 10")
    else: 
        break # Para o laço de repetição.

    soma = primeira_nota + segunda_nota
    media = soma / 2

    print (f"Media: {media}")  