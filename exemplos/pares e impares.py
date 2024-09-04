import os
os.system ("cls || clear")

pares = 0
impares = 0

numero =  int(input("digite um numero: "))
if numero % 2 == 0:
    pares = pares
else: 
    impares = impares    

print (f"quabtidade de pares: {pares}")
print (f"quantidade de imapres: {impares}")  