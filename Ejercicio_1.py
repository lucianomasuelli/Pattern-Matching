from algo1 import *

string = String("icmsdocm")
c = "c"

def existChar(string,c):
    n = len(string)
    for i in range(0,n):
        if string[i] == c:
            return True
    return False

print(existChar(string,c))    
