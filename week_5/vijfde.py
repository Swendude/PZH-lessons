# fruits = ['Tomato', 'Pumpkin', 'Cucumber', 'Eggplant']
# print(fruits)
# print(fruits.pop(1))
# print(fruits)

# x = 0
# y = 1

# while y < 50:
#     x, y  = y, x+y
#     print(y)

# foo = [1, 34, 42, 8, 100, -300, 6253]
# deelnemers = ["Erik", "Nicky", "Henk", "Tom", "Fiona"]
# bbs = [["maatregel 1", "Opgave 3", "Werkingsgebied 4"], ["Ambitie 7", "Relatie 12"], []]

# for bb in bbs:
#     print("Ik ben in de eerste loop")
#     for link in bb:
#         print("Ik ben in de tweede loop")
#         print(link)

# x = 2

# for _ in range(50):
#     x = x * 2

# print(x)


# n = 0
# while n < len(foo):
#     element = foo[n]
#     print(element/2)
#     n += 1


# for element in foo:
#     print(element/2)

# # for getal in foo:
# #     if getal == 8:
# #         print("Acht gevonden!")
# #         break

# print("klaar")

# print(schaap)

# for deelnemer in deelnemers:
#     print(deelnemer)

getal = "42"
userquit = False

while not(userquit):
    keuze = input("Raad een getal?")
    if keuze == getal:
        userquit = True
    else:
        print("Fout!")