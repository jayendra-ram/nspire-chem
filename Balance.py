import numpy as np
from sympy import *
from math import gcd

def insert(original, new, pos):
  return original[:pos] + new + original[pos:]

def output(string,coefs):
  finalstring = string
  strList = []
  runval = 0
  addval = 0
  for x,v in enumerate(coefs):
    strList.append(str(v))
  for i,c in enumerate(string):
    if((i == 0) or (c.istitle() and string[i-1] == ' ')):
      finalstring = insert(finalstring, strList[runval], i+addval)
      addval += len(strList[runval])
      runval += 1;
  return(finalstring)

def lcm(a):
  lcm = a[0]
  for i in a[1:]:
    lcm = lcm*i/gcd(lcm, i)
  return lcm

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

def PolyAtomicIonAnalyzer(string,pos):
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
def Balance(Equation):
  elcount = 0
  temp = ""
  ellist = []
  Equation += "   "
  compcount = 1
  for i,c in enumerate(Equation):
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

  Mat = [[0 for x in range(compcount)] for y in range(elcount)]

  rowcount = 0
  PolyAtomicIon = False
  tempAmount = 0
  amount = 1
  Reactant = False
  for i,c in enumerate(Equation):
    if(c == '>'):
      Reactant = True
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
  tempMatrix = Matrix(np.asmatrix(Mat))
  Mat = tempMatrix.rref()
  FracRow = abs(Mat[0].col(-1))
  listFracs = []
  listDenoms = []
  notfinalList = []
  finalList = []

  for x in range(len(FracRow)):
    listFracs.append(fraction(FracRow[x]))
  for x in range(len(listFracs)):
    listDenoms.append(listFracs[x][1])
  lcmDenom = lcm(listDenoms)
  finalMatrix = FracRow*lcmDenom
  for x in range(len(finalMatrix)):
    notfinalList.append(finalMatrix[x])
  for x in range(len(notfinalList)):
    if(notfinalList[x] != 0):
      finalList.append(notfinalList[x])
    else:
      finalList.append(lcmDenom)
  if(len(finalList) < tempMatrix.shape[1]):
    finalList.append(lcmDenom)
  if(len(FracRow) > tempMatrix.shape[1]):
    finalList = finalList[:-1]
  return(output(Equation,finalList))

print(Balance("K4Fe(CN)6 + KMnO4 + H2SO4 -> KHSO4 + Fe2(SO4)3 + MnSO4 + HNO3 + CO2 + H2O"))
# Answer for 'K4Fe(CN)6 + KMnO4 + H2SO4 -> KHSO4 + Fe2(SO4)3 + MnSO4 + HNO3 + CO2 + H2O' should be [10,122,299,162,5,122,60,60,188]
# Answer for 'HIO3 + FeI2 + HCl -> FeCl3 + ICl + H2O' should be [5,4,25,4,13,15]
# Answer for 'C12H26 + O2 -> CO2 + H2O' should be [2,37,24,26]
# Answer for 'K4Fe(SCN)6 + K2Cr2O7 + H2SO4 -> Fe2(SO4)3 + Cr2(SO4)3 + CO2 + H2O + K2SO4 + KNO3' should be [6,97,355,3,97,36,355,91,36]
