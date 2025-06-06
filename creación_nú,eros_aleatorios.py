import random #librería para llamar y crear números random

numeros = []

for i in range(10): #Ciclo para repetir 100 veces las iteraciones
    n = random.randint(1,100)
    numeros.append(random.randint(1,100)) #Guardamos en la lista el numero

    print(numeros)

cont = 0
for i in range(len(numeros)):
    if numeros[i]%2==0:
        cont+=1

print(f"Cantidad de números pares : {cont}")