import math

class Vierkant:
  def __init__(self, zijde):
    self.oppervlakte = zijde * zijde
    self.omtrek = 4 * zijde

  def printmijnVierkant(self):
    print("De oppervlakte van de vierkant is " + str(self.oppervlakte))
    print("De omtrek van de vierkant is " + str(self.omtrek))

class Rechthoek:
  def __init__(self, lengte, breedte):
    self.oppervlakte = lengte * breedte
    self.omtrek = 2 * (lengte + breedte)

  def printmijnRechthoek(self):
    print("De oppervlakte van de rechthoek is " + str(self.oppervlakte))
    print("De omtrek van de rechthoek is " + str(self.omtrek))

class Cirkel:
  def __init__(self, straal):
    self.oppervlakte = math.pi * straal ** 2
    self.omtrek = 2 * math.pi * straal

  def printmijnCirkel(self):
    print("De oppervlakte van de cirkel is " + str(self.oppervlakte))
    print("De omtrek van de cirkel is " + str(self.omtrek))

Vierkant1 = Vierkant(10)
Vierkant1.printmijnVierkant()

Rechthoek1 = Rechthoek(10,5)
Rechthoek1.printmijnRechthoek()

Cirkel1 = Cirkel(1)
Cirkel1.printmijnCirkel()

SimulatieVierkant = Rechthoek(10,10)
SimulatieVierkant.printmijnRechthoek()

## SWEN: Mooi gedaan, de implementatie is goed! Volgende keer beter lezen want de opdracht was om aparte printfuncties te maken.
## Tip: Je berekent bij al je objecten meteen de oppervlakte en omtrek, dat is prima maar daarmee 
##   verlies je na het aanmaken van het object je originele input waarden (straal bijvoorbeeld). 
##   Misschien komt de klant later met een requirement om de straal aan te passen, dan heb je een probleem. 