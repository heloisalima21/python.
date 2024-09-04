import os
os.system ("cls || clear")

#Declarando  valor a variável.
soma = 0

for i in range (3):
    notas = float (input(f"Digite a  {i+1} ª nota:"))
    if notas >= 0 and notas <= 10:
        break
    else:
         print("as notas tem que maior ou igusl a 0 e menor ou igual a 10")

soma += notas
media = soma / 3

#declarando a provocação. . .
if media >=7:
    print("aprovado")

elif media >= 5 and media <= 6.9:
    print ("recuperação")

else:
    print("reprovado")

print (f"media: {media: .2f}")       