import os
os.system ("cls || clear")

resultado = 0

primeiro_numero = int(input("digite o primeiro numero: "))
segundo_numero = int(input("digite o segundo numero: "))
opcao = input ("digite uma opcao(+ - * /): ")

match(opcao):
    case "+":
        resultado = primeiro_numero + segundo_numero
    case"-":
    
       resultado = primeiro_numero - segundo_numero
    case "*":
        resultado = primeiro_numero* segundo_numero
    case"/":
        resultado = primeiro_numero / segundo_numero
    case "_":
      
     print ("opção inválida") 

print (f"resultado: {resultado}")
print ("===fim===")
    
  