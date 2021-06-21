from algo1 import *
from linkedlist import *

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
