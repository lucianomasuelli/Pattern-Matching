from algo1 import *

def isPalindrome(string):
    n = len(string)
    i = 0
    j = n-1
    while i != j:
        if string[i] != string[j]:
            return False
        i += 1
        j -= 1
    return True


s = String("anitalavalatina")

print(isPalindrome(s))
