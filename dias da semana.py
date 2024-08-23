import os
os.system ("cls || clear")

print ("bem-vindo!")

print ("""
1- Domingo 
2- Segunda 
3- Terça
4- Quarta
5- Quinta
6- Sexta
7- Sabado 
       """)

opcao = int ( input(" Digite a sua opção: "))
match (opcao):
    case 1:
        print("Você escolheu domingo !")
        print ("fim de semana")
    case 2:
        print ("Você escolheu segunda !")
        print ("dia útil")
    case 3:
        print ("Você escolheu terca !")
        print ("dia útil")
    case 4:
        print ("Você escolheu quarta ! ")
        print ("dia útil")
    case 5 :  
        print ("Você escolheu quinta !")
        print ("dia útil")
    case   6:
        print ("Voce escolheu sexta! ")
        print ("dia útil")
    case 7 :
        print ("voce escolheu sabado!")
        print ("fim de semana")
    case _:
        print("voce não escolheu nehuma das opcoes acima")




