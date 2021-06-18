from algo1 import *
from linkedlist import *
from hashtable import *


def mostRepeatedChar(string):
    mayor = 0
    n = len(string)
    m = primo_mayor(n)
    T = Array(m,LinkedList())
    for i in range(0,n):
        #inserta cada elemento del string en un a table hash 
        #cuando hay colisiones (osea cuando hay elementos repetidos) le suma 1 al campo key.
        pos = insertHash(T,string[i])
        T[pos].head.value += 1
        if T[pos].head.value > mayor:
            mayor = T[pos].head.value
            c_mayor = T[pos].head.key
    return c_mayor


s = String("haloamanolaoo")

print("caracter mas repetido:",mostRepeatedChar(s))
        


