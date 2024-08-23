import os
os.system ("cls || clear")

#declarando variáveis.
desconto = 0
preco_final = 0
preco_parcelado = 0

print("solicitando dados para o usuário")
preco_produto = int(input("digite o valor do produto: "))

print("\nEscolha uma das formas de pagamento abaixo.")
print("1 - pagamento a vista")
print("2 - pagamento a prazo")
opcao = int(input('informe a opcao desejada: '))

match (opcao):
    case 1:
        desconto = preco_produto * 0.10
        preco_final = preco_produto - desconto

        print(f"\nPreço do produto: R$ {preco_produto}")
        print(f"forma d e pagamento: a vista")
        print(f"Valor do desconto: R$ {desconto}")
        print(f"Total a pagaar: R$ {preco_final}")
    case 2: 
        parcelas = int(input("\nDigite a quantidade de parcdelas: "))

        preco_parcelado = preco_produto / parcelas
        preco_final = preco_produto
          
        print(f"\nPreço do produto: R$ {preco_produto}")
        print(f"Forma de pagamento: a prazo")
        print(f"Quantidade de parcelas: {parcelas}")  
        print(f"Valor por parcelas: R$ {preco_final: 2f}")
        print(f"Total a prazo: R$ {preco_final: 2f}")
    case _:
        print ("Opção imnválida: \n")
      
        
