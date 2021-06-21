from algo1 import *

def my_hash(string):
  #genera un key numerico a partir de la string.

  if len(string) > 1:
    key = 0
    for i in range(0,len(string)):
      j = abs(i-len(string))
      key += ord(string[i])*255^j
  else:
    key = ord(string) - ord("a")
  return key


def rubin_karp(t,p):
    m = len(p)
    n = len(t)+1
    hash = my_hash(p)
    for s in range(0,n-m):
        ts = substr(t,s,s+m)
        if my_hash(ts) == hash:
            if strcmp(ts,p):
                print(p,"encontrado en:",s)
                return True
    return False


s = String("holanda")
c = String("anda")

print(rubin_karp(s,c))