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



def finite_automaton_matcher(T,P):
    sigma = LinkedList()
    append(sigma,"a")
    append(sigma,"b")
    append(sigma,"c")
    n = len(T)
    m = len(P)
    mat = transition_function(P,sigma)
    q = 0
    for i in range(0,n):
        c = search(sigma,T[i])
        q = mat[q][c]
        if q == m:
            print("El patrón se encuentra entre:",(i+1)-m," y ",i)




finite_automaton_matcher("aaababaabaababaab","aabab")

#m = transition_function("ababaca",sigma)

"""
for i in range(0,len(m)):
    for j in range(0,length(sigma)):
        print(m[i][j], end=" ")
    print("")

"""

