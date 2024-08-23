import os
os.system("cls || clear")

#solicitando dados.
numero = int(input ('digite um numero para tabuada'))
             
print(f"\ntabuada de multiplicacao do numero: {numero}")

for i in range (1,11):
    print(f"{numero} * {1} = {numero * i }")