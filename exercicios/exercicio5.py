import os
os.system ("cls || clear")

login_salvo = "senai"
senha_salva =  "123"

while True:
  login = input("digite o login: ")
  senha = input ("digite a senha: ")
  
  if login_salvo == login and senha_salva == senha: 
    print ("Bem-vindo!")
    break
   
  else:  
     print("!login ou senha invalidos.")

print("=== FIM ===")     

