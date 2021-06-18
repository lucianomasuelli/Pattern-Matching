from algo1 import *
from linkedlist import *


def enqueue(Q,element):
  add(Q,element)
  return


def dequeue(Q):
  currentNode = Q.head
  if Q.head != None:
    lastPos = length(Q)
    element = access(Q,lastPos-1)
    if lastPos == 1:
      Q.head = None
      return element
    for i in range(0,lastPos-2):
      currentNode = currentNode.nextNode
    currentNode.nextNode = None
    return element
  else:
    return None