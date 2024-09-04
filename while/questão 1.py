import os
os.system ("cls || clear")
contador = 0

while True:
    numero = float (input("Digite um numero (0 ou positivo para parar): "))
    if numero >= 0:
      break 
contador += 1       
print(f"Quantidade de numeros negativos inseridos: {contador}")    