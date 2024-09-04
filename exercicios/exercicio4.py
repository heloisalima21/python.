import os
os.system ("cls || clear")

while True:
    notas = float(input("Digite duas notas: "))

    if notas < 0 or notas > 10:
        print ("nota invalida")

    else:
       break

print (f"nota: {notas}")      


    


