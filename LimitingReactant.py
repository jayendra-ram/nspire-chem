from ElementInfoClass import *
from MolarMass import*
def LimitingReactant(element1,amount1,coef1,*args):
  mm = MolarMass(element1)
  tempval = amount1 / mm
  tempval /= coef1
  val = tempval
  tempel = element1
  el = tempel
  mass = 0
  for arg in args:
    if(type(arg) is str):
      mm = MolarMass(arg)
      tempel = arg
    if(((type(arg) == int) or (type(arg) == float)) and mass == 1):
      tempval = arg / mm
    if(((type(arg) == int) or (type(arg) == float)) and mass == 2):
      tempval /= arg
      if(tempval <= val):
        val = tempval
        el = tempel
    mass += 1
    if(mass == 3):
      mass = 0
  return(el)
