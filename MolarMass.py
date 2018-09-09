from ElementInfoClass import *
def MolarMass(formula):
  #INITIALIZATION
  formula += "   "
  temp = ""
  mass = 0
  tempMass = 0
  PAtempMass = 0
  PAMass = 0
  tempAmount = 1
  amount = 1
  polyAtomicIon = False
  #LOOP
  for i,c in enumerate(formula):
    if(c.istitle()):
      temp += c
      if(formula[i+1].isdigit()):
        amount = int(formula[i+1])
        if(formula[i+2].isdigit()):
          amount = (10 * int(formula[i+1])) + int(formula[i+2])
      if(formula[i+1].islower()):
        temp += formula[i+1]
        if(formula[i+2].isdigit()):
          amount = int(formula[i+2])
          if(formula[i+3].isdigit()):
            amount = (10 * int(formula[i+2])) + int(formula[i+3])
      if(polyAtomicIon == False):
        tempMass = eval(temp + '.atomicMass')
        tempMass *= amount
        mass += tempMass
        temp = ""
        tempMass = 0
        amount = 1
      if(polyAtomicIon == True):
        PAtempMass = eval(temp + '.atomicMass')
        PAtempMass *= amount
        PAMass += PAtempMass
        PAtempMass = 0
        temp = ""
        amount = 1
    if(c == "("):
      polyAtomicIon = True
    if(c == ")"):
      if(formula[i+1].isdigit()):
        tempAmount = int(formula[i+1])
        if(formula[i+2].isdigit()):
          tempAmount = (10 * int(formula[i+1])) + int(formula[i+2])
      mass += PAMass * tempAmount
      polyAtomicIon = False
      tempAmount = 1
      PAMass = 0
  return round(mass,2)
#NOTE:
#-Subscript following variable cannot be larger than 100
#-Input must be string
