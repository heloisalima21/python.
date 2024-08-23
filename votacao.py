import os
os.system ("cls || clear")

#solicitando dados.
idade = int(input("digite sua idade: "))

#verificando.
if  idade < 18 or idade > 65: 
    print ("não é obrigado a votar")
else: 
    print ("voto obrigátorio: ")
