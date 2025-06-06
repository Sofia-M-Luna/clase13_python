import random #librería para llamar y crear números random

numeros = []

for i in range(100): #Ciclo para repetir 100 veces las iteraciones
    n = random.randint(1,100)
    numeros.append(random.randint(1,100)) #Guardamos en la lista el numero

    numeros.sort()
    print(numeros)

#numero = random.randint(1,100) #rango para el numero random

    