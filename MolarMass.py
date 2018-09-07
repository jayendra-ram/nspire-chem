from ElementInfoClass import *
def MolarMass(formula):
  #INITIALIZATION
  formula += "   "#DO NOT DELETE
  temp = ""
  mass = 0
  tempMass = 0
  amount = 1
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
          amount = int(formula[i+1])
          if(formula[i+3].isdigit()):
            amount = (10 * int(formula[i+2])) + int(formula[i+3])
      #Finalization
      tempMass = eval(temp + '.atomicMass')
      tempMass *= amount
      mass += tempMass
      temp = ""
      tempMass = 0
      amount = 1
  return round(mass,2)

#NOTE:
#-Subscript following variable cannot be larger than 100
#-Input must be string
