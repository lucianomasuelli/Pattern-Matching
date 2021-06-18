from linkedlist import LinkedList, length
from algo1 import *
from myqueue import *

def verifyBalancedParentheses(string):
    Q = LinkedList()
    n = len(string)
    for i in range(0,n):
        if string[i] == "(":
            enqueue(Q,i)
        elif string[i] == ")":
            if Q.head != None:
                dequeue(Q)
            else:
                return False
    if Q.head == None:
        return True
    else:
        return False


s = String("(c)cc((ccc)cc((ccc(c))))")

print(verifyBalancedParentheses(s))
