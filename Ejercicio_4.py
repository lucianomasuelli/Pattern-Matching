from algo1 import *

def getBiggestIslandLen(string):
    max = 0
    cont = 1
    n = len(string)
    for i in range(0,n):
        #recorre la cadena, si el elemento actual es igual al anterior suma 1 al contador.
        #cuando el elemento en analisis es distinto al anterior, 
        # se verifica si el contador es el mayor hasta el momento y se reinicia el contador.
        if i == 0:
            max = 1
        elif string[i] == string[i-1]:
            cont += 1
        else:
            if cont > max:
                max = cont
            cont = 1
    if cont > max:
        max = cont
    return max


s = String("cccccccdaaasssbbb")

print("La isla mas grande tiene un tamaño de:", getBiggestIslandLen(s))