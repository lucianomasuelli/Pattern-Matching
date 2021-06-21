from algo1 import *
from linkedlist import *

def transition_function(pattern,sigma):
    m = len(pattern)+1
    n = length(sigma)
    matrix = Array(m,Array(n,0))
    for q in range(0,m): #recorre todos los estados.
        Pq = str(substr(pattern,0,q))
        current = sigma.head
        for a in range(0,n): #recorre todos los elementos del alfabeto.
            PqA = String(Pq + current.value)
            if q != m-1:  
                k = substr(pattern,0,q+1)
            else: #si se está analizando el ultimo estado, a PqA le quito el primer elemento de la cadena para que tenga el mismo tamaño de k.
                k = pattern
                PqA = substr(PqA,1,len(PqA))
            while strcmp(k,PqA) == False and len(k) != 0: #busca el mayor prefijo de "k" que sea sufijo de "PqA".
                k = substr(k,0,len(k)-1)
                PqA = substr(PqA,1,len(PqA))
            matrix[q][a] = len(k) #guardo el largo del mayor prefijo en una matriz.
            current = current.nextNode

    return matrix



def find_pattern(T,P):
    if len(P) > len(T):
        #si P es de mayor tamaño que T, lo acorto quitandole elementos del final.
        while len(P) != len(T):
            P = substr(P,0,len(P)-1)
    elif len(T) > len(P):
        #si T es de mayor tamaño que P, lo acorto quitandole elementos del principio.
        while len(P) != len(T):
            T = substr(T,1,len(T))

    while strcmp(T,P) == False and len(P) != 0: #busca el mayor prefijo de "P" que sea sufijo de "T".
        P = substr(P,0,len(P)-1)
        T = substr(T,1,len(T))
    if len(P) != 0:
        return P
    else:
        return False


P = String("moinabcdeefmke")
T = String("imcsodabnnicinmoin")

print(find_pattern(T,P))
