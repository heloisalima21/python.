import os 
os.system("clls| clear")

print (" Bem vindo !")
print ("""
1- Picanha | Valor : 25.00
2- Lasanha | Valor : 20.00
3- Strogonoff | Valor : 18.00
4- Bífe acebolado | Valor : 15.00
5- Pão com ovo | Valor : 5.00
      """)

opcao = int (input (" Digite a sua opção : "))
match (opcao):
    case 1:
        print("Você escolheu picanha !")
    case 2:
        print ("Você escolheu lasanha !")
    case 3:
        print ("Você escolheu strogonoff !")
    case 4:
        print ("Você escolheu bífe acebolado ! ")
    case 5 :  
        print ("Você escolheu pão com ovo !")
    case   " ":
        print ("Você não escolheu nada das opções acima ")
    
