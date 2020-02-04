# doelgetal = 42
# opties = {10:"rond getal!", 42:"goed getal!"}

# antwoord = input("Welk nummer heb ik in mijn hoofd?")
# try:
#     antwoord = int(antwoord)
#     print(opties[antwoord])
#     print("Einde try")

# except ValueError:
#     print("er is iets mis gegaan")
# except KeyError:
#     print("Deze waarde zit niet in optie")

# if antwoord == doelgetal:
#     print("Je hebt het goed!")
# else:
#     print("Je hebt het fout!")


class cat:
    def __init__(self, kleur, geslacht, leeftijd):
        self.kleur = kleur
        self.leeftijd = leeftijd * 3 # kattenleeftijd

    def maakLeeftijd(self, leeftijd):
        self.leeftijd = leeftijd

    def spreek(self):
        print(f'Ik ben {self.leeftijd}')

    def __len__(self):
        return 42
len([1,2,3])

loes = cat("Blauw", "Vrouw", 8)
print(len(loes))
# print(loes)
loes.spreek()
loes.maakLeeftijd(12)
loes.spreek()
# print(loes.kleur)











    