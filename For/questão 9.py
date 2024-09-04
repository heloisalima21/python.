import os
os.system ("cls || clear")

num_linhas = 4
num_columas = 6

#Laço para cada linha
for i in range (num_linhas):
    #Laço para cada coluna dentro da linha
    for j in range (num_columas):
        #Imprime um asteristico sem pular linha 
        print ('*', end='')
    print ()    
