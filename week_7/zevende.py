# string, boolean, integers, floats,
# lists, tuples, dictionaries

# pets = [('Dog', 5), ('Cat',2), ('Hamster', 10), ("Goldfish", 9)]

# for animal, price in pets:
#     print(f'{animal} -> {price} euro')

# pets[2] = (pets[2][0], 11)

# print(pets)

# for i in range(len(pets)):
#     print(f'{pets[i]} -> {prices[i]}')

# prices[2] = 11
# print(prices)

# pets = ['Dog', 'Cat', 'Hamster', "Goldfish"]
# prices = [5, 2, 10, 9]

# petshop = {} # een lege dict
# petshop['Dog'] = 5
# petshop['Cat'] = 2
# petshop['Hamster'] = 10
# petshop['Goldfish'] = 9

# petshop = {'Dog': 5, 'Cat': 2, 'Hamster': 10, 'Goldfish': 9}
# petshop['Dog'] = 90
# print(petshop.pop('Dog'))
# print(petshop)

# petslist = ['Dog', 'Cat', 'Hamster', "Goldfish"]
# petsdict = { 1: 'Dog', True: 'Cat', 1.0: 'Hamster', 'Goudvis': 'Goldfish'}

# print(petsdict[1.0])

# deelnemers = [{'naam':'Erik', 'achternaam':'Verhaar', 'bedrijf':'PZH'}, 'Nicky', 'Fiona', 'Henk', 'Tom', 'Swen']



# presentie = {True: {}, False: {}}

# presentie[True]['Hond'] = 5
# print(presentie)

petshop = {'Dog': 5, 'Cat': 2, 'Hamster': 10, 'Goldfish': 9}

# for dier, prijs in petshop.items():
#     print(dier)
#     print(prijs)
    # print(petshop[foo])


# resultaat = petshop.get('Snake')
# if not resultaat:
#     print("Dit dier verkopen wij niet")

petshop2 = dict([('Dog', 5), ('Cat',2), ('Hamster', 10), ("Goldfish", 9)])
# print(petshop2)
totaal = 0
for prijs in petshop2.values():
    totaal+= prijs
print(totaal/len(petshop2))

for dier in petshop2:
    print(dier)














