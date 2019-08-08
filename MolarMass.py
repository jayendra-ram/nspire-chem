from ElementInfoClass import *
def NumAnalyze(string,pos):
  string[pos]
  tempbool = True
  runvar = 0
  while tempbool == True:
    runvar += 1
    if(not(string[pos+runvar].isdigit())):
      tempbool = False
  strval = string[pos:pos+runvar]
  intval = int(strval)
  return(intval)

def MolarMass(formula):
  formula += "   "
  temp = ""
  mass = 0
  tempMass = 0
  PAtempMass = 0
  PAMass = 0
  tempAmount = 1
  amount = 1
  polyAtomicIon = False
  for i,c in enumerate(formula):
    if(c == "("):
      polyAtomicIon = True
    if(c == ")"):
      if(formula[i+1].isdigit()):
        amount = NumAnalyze(formula,i+1)
      mass += PAMass * tempAmount
      polyAtomicIon = False
      tempAmount = 1
      PAMass = 0
    if(c.istitle()):
      temp += c
      if(formula[i+1].isdigit()):
        amount = NumAnalyze(formula,i+1)
      if(formula[i+1].islower()):
        temp += formula[i+1]
        if(formula[i+2].isdigit()):
          amount = NumAnalyze(formula,i+2)
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
  return round(mass,2)
