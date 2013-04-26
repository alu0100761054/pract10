import random, sys
from math import *
from error import error

l = [('(a*b)**3','(a**3)*(b**3)'),
('a/b','1/(b/a)'),
('a-b','-(b-a)'),
('(a*b)**4','(a**4)*(b**4)'),
('(a+b)**2','(a**2)+(2*a*b)+(b**2)'),
('(a+b)*(a*b)','(a**2)-(b**2)'),
('log10(a*b)','(log10(a))*(log10(b))'),
('1/((1/a)+(1/b))','(a*b)/(a+b)'),
('a*(((sin(b))**2)+((cos(b))**2))','a'),
('tan(a+b)','(sin(a+b))/(cos(a+b))'),
('sin(a+b)','((sin(a))*(cos(b)))+((sin(b))*(cos(a)))')]

if __name__=='__main__':
  A = float(sys.argv[1])
  B = float(sys.argv[2])
  n = int(sys.argv[3])
  resultados = (sys.argv[4])
  f = open('resultados', 'w')
  
  umbral = [1.e-10, 1.e-50, 1.e-100, 1.e-150, 1.e-200]
  
  for elem in l:
    exp1 = elem[0]
    exp2 = elem[1]
    f.write("%s\n%s\n"%(exp1, exp2))
    for u in umbral:
      r = error(exp1, exp2, A, B, n, u)
      print '%40s %40s %10.1f'% ( exp1, exp2, r)
      f.write("%g\n"%(r))
      
    f.write("\n")
  
  f.close()