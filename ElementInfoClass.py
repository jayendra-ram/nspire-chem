class Element:
	def __init__(self,symbol,name,atomicNumber,atomicMass,charge):
		self.symbol = symbol
		self.name = name
		self.atomicNumber = atomicNumber
		self.atomicMass = atomicMass
		self.charge = charge

H = Element("H","Hydrogen",1,1.01,1)
He = Element("He","Helium",2,4.00,0)
Li = Element("Li","Lithium",3,6.94,1)
Be = Element("Be","Beryllium",4,9.01,2)
B = Element("B","Boron",5,10.81,3)
C = Element("C","Carbon",6,12.01,4)
N = Element("N","Nitrogen",7,14.01,-3)
O = Element("O","Oxygen",8,16.00,-2)
F = Element("F","Fluorine",9,19.00,-1)
Ne = Element("Ne","Neon",10,20.18,0)
Na = Element("Na","Sodium",11,22.99,1)
Mg = Element("Mg","Magnesium",12,24.31,2)
Al = Element("Al","Aluminum",13,26.98,3)
Si = Element("Si","Silicon",14,28.09,4)
