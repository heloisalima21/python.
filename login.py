import os
os.system ("cls || clear")

#declarando variáveis.
login_salvo = "senaids"
senha_salva =  "123"

#solicitando dados.
login = input("digite o login: ")
senha = input ("digite a senha: ")

#verificar.

if login == "senaids" and senha == "123":
    print("bem-vindo!")
else:
    print("login ou senha inválidos. ")