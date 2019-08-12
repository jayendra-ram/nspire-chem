# Elements are case-sensitive
# Coefficients must be integer values
# Do not input equation with Coefficients
# Separate reactants from products with ' -> '
# Separate reactants/products from each other with ' + '
import numpy as np
from sympy import *
from math import gcd

def lcm(a): #lcm finder
  lcm = a[0]
  for i in a[1:]:
    lcm = lcm*i/gcd(lcm, i)
  return lcm

def NumAnalyze(string,pos): # Number (subscript value) Analyzer
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

def PolyAtomicIonAnalyzer(string,pos): #PAI subscript Analyzer
  string[pos]
  newpos = 0
  tempbool = True
  runvar = 0
  while tempbool == True:
    if(string[pos+runvar] == ')'):
      newpos = runvar+pos
      tempbool = False
    else:
      runvar +=1
  return(NumAnalyze(string,newpos+1))

count = 0
def Balance(Equation): # THIS IS THE SPICY FUNCTION
  elcount = 0 # Number of elements in the formula
  temp = ""
  ellist = [] # List of elements in formula
  Equation += "   "
  compcount = 1
  for i,c in enumerate(Equation): # Determines the type of elements in the list, and how many there are
    if(c.istitle()) and c != ' ':
      if(Equation[i+1].islower()):
        temp = Equation[i:i+2]
        if(temp not in ellist):
          ellist.append(temp)
          elcount += 1
      else:
        temp = Equation[i]
        if(temp not in ellist):
          ellist.append(temp)
          elcount += 1
    if(c == '+' or c == '>'):
        compcount += 1

  Mat = [[0 for x in range(compcount)] for y in range(elcount)] # This creates a matrix with the width being the number of compounds, and the height being the number of elements

  rowcount = 0
  PolyAtomicIon = False
  tempAmount = 0
  amount = 1
  Reactant = False
  for i,c in enumerate(Equation): # This will analyze the equation and input the values into the Matrix
    if(c == '>'):
      Reactant = True # this makes the reactant side values negative
    if(c == '+' or c == '>'):
      rowcount += 1
    if(c == '('):
      PolyAtomicIon = True
    if(c == ')'):
      PolyAtomicIon = False
    if(c.istitle()):
      if(Equation[i+1].islower()):
        if(Equation[i+2].isdigit()):
          amount = NumAnalyze(Equation,i+2)
        if(PolyAtomicIon == True):
          tempAmount = PolyAtomicIonAnalyzer(Equation,i)
          amount = amount * tempAmount
        temp = Equation[i:i+2]
        val = ellist.index(temp)
        if(Reactant == True):
          amount = -1 * amount
        Mat[val][rowcount] += amount
        amount = 1
      else:
        if(Equation[i+1].isdigit()):
          amount = NumAnalyze(Equation,i+1)
        if(PolyAtomicIon == True):
          tempAmount = PolyAtomicIonAnalyzer(Equation,i)
          amount = amount * tempAmount
        temp = Equation[i]
        val = ellist.index(temp)
        if(Reactant == True):
          amount = -1 * amount
        Mat[val][rowcount] += amount
        amount = 1
  tempMatrix = Matrix(np.asmatrix(Mat)) # turns nested list into matrix
  Mat = tempMatrix.rref() # reduced row echelon form
  FracRow = abs(Mat[0].col(-1)) # '.col(-1)' is the last column
                                # NOTE: this column is made of variables that are RATIONALS
  listFracs = [] # this will be a list with the rationals in fraction form
  listDenoms = [] # this will be the list of denominators (should be whole numbers)
  notfinalList = [] # this should be the list of coeffs, but doesn't currently work 8/8/19

  #NOTE: Everything below this inefficient for the purposes of debugging
  for x in range(len(FracRow)):
    listFracs.append(fraction(FracRow[x]))
  for x in range(len(listFracs)):
    listDenoms.append(listFracs[x][1])
  lcmDenom = lcm(listDenoms)
  finalMatrix = FracRow*lcmDenom
  for x in range(len(finalMatrix)):
    notfinalList.append(finalMatrix[x])

  return(notfinalList, lcmDenom)
  

print(Balance("NaNO3 + PbO -> Pb(NO3)2 + Na2O"))

#PROBLEMS:

#'H3PO4 + (NH4)2MoO4 + HNO3 -> (NH4)3PO4(MoO3)12 + NH4NO3 + H2O'
# Should return [1,12,21,1,21,12], but reducing it to rref caused a lost row. ACTUAL OUTPUT: [1,12,21,1,21]
# For the example and work, see: https://www.wikihow.com/Balance-Chemical-Equations-Using-Linear-Algebra

#'Fe + Cl2 -> FeCl3' Should return [2,3,2], but actually returns [2,3]

#'KMnO4 + HCl -> KCl + MnCl2 + H2O + Cl2' Shuold return [2,16,2,2,8,5], but actually returns [2,16,2,2,8]

# In each of the above examples, the lcmDenom is the final coeff, but there are other issues


#OTHER ISSUES
#'PhCH3 + KMnO4 + H2SO4 = PhCOOH + K2SO4 + MnSO4 + H2' returns an extraneous '0' coefficient, when the lcmDenom should be the final solution
#'NaNO3 + PbO -> Pb(NO3)2 + Na2O' Does the same

#NEEDS TESTING!!!!!!!!
