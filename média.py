import os
os.system ("cls || clear")

#solicitando dados.
nome = input ("digite seu nome:")
idade = int (input("digite sua idade"))
primeira_nota = float (input("digite a primeira nota:"))
segunda_nota = float (input("digite a segunda nota"))
terceira_nota = float(input("digite a terceira nota"))

media = (primeira_nota + segunda_nota + terceira_nota) / 3

#verificando
print ("\nexibindo dados")
print (f"nome: {nome}")
print (f"idade: {idade}")
print (f"media: {media}")

if media >= 7:
     print ("voce foi aprovado")

else:
     print ("voce foi reprovado")     