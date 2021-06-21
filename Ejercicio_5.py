from algo1 import *
from linkedlist import *
from hashtable import *

def isAnagram(string1,string2):
    #utilizo una hash table organizada por double hashing.
    if len(string1) != len(string2):
        return False
    n = len(string1)
    m = primo_mayor(n)
    T = Array(m,LinkedList())
    #inserto los elementos de la primer cadena en la tabla hash.
    for i in range(0,n):
        pos = insertHash(T,string1[i])
        T[pos].head.value += 1

    #calulo la posición en donde se deberian insertar los elementos de la segunda cadena,
    # y verifica si en esa posicion ya está insertado el mismo elemento.
    for i in range(0,n):
        key = gen_key(string2[i],m)
        find = False
        j = 0
        while j < m and find == False:
            pos = hash(key,j,m)
            if T[pos] != None and T[pos].head.key == string2[i]:
                find = True
            j += 1

        if find == False:
            return False
    return True


s1 = String("golaaazoa")
s2 = String("zolagoaaa")

print(isAnagram(s1,s2))
        
