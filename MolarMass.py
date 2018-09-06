from ElementInfoClass import *
def MolarMass(formula):
  l = len(formula)
  temp = ""
  count = 0
  mass = 0
  for i,c in enumerate(formula):
    if(c.istitle()):
      temp += c
      count = 1
    if(not c.istitle()): 
      temp += c
      count +=1
    if(c.isdigit())
      if(not formula[i+1].isdigit()):
        
      else:
        mass += MolarMass(temp)
  return mass
  print(eval(formula + '.atomicMass'))

string = "CaCl2"
