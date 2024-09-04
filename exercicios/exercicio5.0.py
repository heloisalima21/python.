import os
os.system ("cls || clear")

login_salvo = "senai"
senha_salva =  "123"
contador = 0

while True:
  login = input("digite o login: ")
  senha = input ("digite a senha: ")
  contador += 1
  
  if login_salvo == login and senha_salva == senha: 
    print ("Bem-vindo!")
    break
   
  else:  
     print("!login ou senha invalidos.")
     print(f"Tentativas: {contador} \n")
     if contador == 3:
        break
     
     print ("===FIM===")    