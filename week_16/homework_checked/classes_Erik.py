# Maak een class genaamd vierkant met methodes oppervlakte en omtrek
# Maak een class genaamd vierhoek met methodes oppervlakte en omtrek
# Maak een class genaamd cirkel met methodes oppervlakte en omtrek
# Denk na over de argumenten voor initialisatie en de argumenten en return van de verschillende methodes
# Kan je een object van het type vierkant 'simuleren' dmv vierhoek

import math
print(math.pi)

# class vierkant:
#     def __init__(self, lengte, breedte):
#         self.lengte = lengte
#         self.breedte = breedte

#     def printoppervlakte(self):
#         oppervlakte = self.lengte * self.breedte
#         print(oppervlakte)
    
#     def printomtrek(self):
#         omtrek = self.lengte * 2 + self.breedte * 2
#         print(omtrek)

## SWEN: Goed gedaan, je implementatie is correct. Echter heeft een vierkant als het goed is 
## maar één waarde voor de init nodig (lengte en breedte zijn hetzelfde)

class vierhoek:
    def __init__(self, nzijden, nhoeken, lengte, breedte):
        ## SWEN: Waarom geef je hier nzijden en nhoeken als argumenten? Je gebruikt ze vervolgens nergens
        self.nzijden = 4
        self.nhoeken = 4
        self.lengte = lengte
        self.breedte = breedte

    def printoppervlakte(self):
        oppervlakte = self.lengte * self.breedte
        print(oppervlakte)
    
    def printomtrek(self):
        omtrek = self.lengte * 2 + self.breedte * 2
        print(omtrek)

    def printzijden(self):
        print(f'ik heb {self.nzijden} zijden')

    def printhoeken(self):
        print(f'ik heb {self.nhoeken} hoeken')

scherm = vierhoek(1, 1, 50, 30)
scherm.printoppervlakte()
scherm.printomtrek()
scherm.printzijden()
scherm.printhoeken()

class cirkel:
    def __init__(self, straal, diameter):
        ## SWEN: De straal en diameter hangen samen (diameter = 2 x straal)
        self.straal = straal
        self.diameter = diameter
    
    def printoppervlakte(self):
        oppervlakte = math.pi * self.straal ** 2
        print(oppervlakte)

    def printomtrek(self):
        omtrek = math.pi * self.diameter
        print(omtrek)

sticker = cirkel(6, 12)
sticker.printoppervlakte()
sticker.printomtrek()

## SWEN: Inheritance was nog niet de bedoeling, maar het idee is goed. Echter heb je weer een argument te veel
class vierkant(vierhoek):
    def __init__(self, lengte, breedte):
        self.lengte = lengte
        self.breedte = breedte

knop = vierkant(20, 20)
knop.printoppervlakte()
knop.printomtrek()
