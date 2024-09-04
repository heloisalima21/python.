import os
("cls || clear")

contador = 0
continua = 's'

while continua == 's':
    #comandos a serem repetidos
    print("repetindo...")

    contador +=1

    continua = input ("Tecle 's' se deseja continuar: " ).strip ().lower()

if contador == 0:
        print("0 bloco NAO foi repetido")
else:
        print(f"o bloco foi repetido {contador} vezes")    