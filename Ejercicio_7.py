from algo1 import *


def reduceLen(string):
    #funcion recursiva que cuando encuentra dos elementos consecutivos iguales los elimina de la cadena 
    # y llama a la funcion con la cadena acortada hasta que no hay mas elementos duplicados.
    n = len(string)
    for i in range(1,n):
        if string[i] == string[i-1]:
            preStr = str(substr(string,0,i-1)) #crea la subcadena con los elementos antes de los duplicados.
            posStr = str(substr(string,i+1,n)) #crea la subcadena con los elementos despues de los duplicados.
            newStr = String(preStr + posStr) #crea la nueva cadena con la unión de las dos anteriores.
            string = reduceLen(newStr) #llama a la función con la nueva cadena.
            break
    return string



s = String("aaabccddd")

print(reduceLen(s))
