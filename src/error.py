import random, sys
from math import *

def error(exp1, exp2, A, B, n, umbral):
  C = 0
  i=1
  while i<=n:
    a = random.uniform(A, B)
    b = random.uniform(A, B)
    if abs(eval(exp1)-eval(exp2)) > umbral:
      C+=1
    i+=1
  port = C*100/n
  return port
      
if __name__=='__main__':
  exp1 = (sys.argv[1])
  exp2 = (sys.argv[2])
  A = float(sys.argv[3])
  B = float(sys.argv[4])
  n = int(sys.argv[5])
  umbral = float(sys.argv[6])
  
  print 'El porcentaje de error es de un', error(exp1, exp2, A, B, n, umbral)