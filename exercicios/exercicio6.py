import os
os.system ("cls || clear")

QUANTIDADE_NOTAS = 2
soma = 0

for i in range (QUANTIDADE_NOTAS):
    while True:
        nota = float(input(f"Digite {i+1}ª nota: "))

        if nota >= 0 and nota <= 10:
            break # Para o laço de repetição.
    soma += nota

media = soma / QUANTIDADE_NOTAS

print (f"Media: {media}")