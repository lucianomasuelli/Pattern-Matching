from algo1 import *

def isContained(string1,string2):
    n = len(string1)
    j = 0
    for i in range(0,n):
        if string1[i] == string2[j]:
            j +=1
        if j == len(string2):
            return True
    return False


s1 = String("afffmmmarillzzzllhooo")

s2 = String("amarillo")

print(isContained(s1,s2))
