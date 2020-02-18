# class Vierkant:
#   def __init__(self, zijde):
#     self.oppervlakte = zijde * zijde
#     self.omtrek = 4 * zijde

#   def printmijnVierkant(self):
#     print("De oppervlakte van de vierkant is " + str(self.oppervlakte))
#     print("De omtrek van de vierkant is " + str(self.omtrek))

# #   def __gt__(self, andere):
# #       if self.oppervlakte > andere.oppervlakte:
# #           return True
# #       else:
# #           return False

# v1 = Vierkant(5)
# v2 = Vierkant(6)

# x = 5
# y = 7

# if v1 > v2:
#     print("v1 wint")
# else:
#     print("v2 wint")

import employees

# class Employee:
#     def __init__(self, naam, id, leeftijd):
#         self.naam = naam.lower()
#         self.id = id
#         self.leeftijd = leeftijd / 2
    
#     def bedrijfsnaam(self):
#         return f"{self.naam}-{self.id}"


# class Salesman(Employee):
#     def __init__(self, naam, leeftijd, cr, sales):
#         super().__init__(naam, cr * sales, leeftijd)
#         self.cr = cr
#         self.sales = sales

#     def berekensalaris(self):
#         return self.cr * self.sales

#     def bedrijfsnaam(self):
#         return f"SM-{self.naam}-{self.id}"

# class Marketeer(Employee):
#     def geefsalaris(self, salaris):
#         self.salaris = salaris
    
#     def berekensalaris(self, br):
#         return br * self.salaris
    
#     def bedrijfsnaam(self):
#         return f"MT-{self.naam}-{self.id}"

henk = employees.Salesman("Henk", 23, 0.3, 8000)
print(henk.berekensalaris())
# jan = Salesman("Jan", 12, 83)
# ella = Marketeer("Ella", 7, 35)

print(henk.bedrijfsnaam())
# henk.noteersales(7000)
# print(henk.berekensalaris(0.3))

# print(ella.bedrijfsnaam())
# ella.geefsalaris(3000)
# print(ella.berekensalaris(1.2))