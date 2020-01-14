# Opmerking van Henk: Aanpassingen in apart grid! Dus niet bewerken in huidig grid.

def prettyprintgrid(g):
    for row in g:
        print(row)

breedte, hoogte = 10, 10

# wereld = [row for row in ([0 for i in range(breedte)] for i in range(hoogte))]
# prettyprintgrid(wereld)

# wereld = []

# for h in range(hoogte):
#     nieuwe_rij = []
#     for b in range(breedte):
#         nieuwe_rij.append(0)
#     wereld.append(nieuwe_rij)
def maak_wereld(breedte, hoogte):
    wereld = []
    for h in range(hoogte):
        nieuwe_rij = []
        for b in range(breedte):
            nieuwe_rij.append(0)
        wereld.append(nieuwe_rij)
    return wereld

wereld = maak_wereld(breedte, hoogte)



wereld[2][4] = 1 
wereld[1][4] = 1
wereld[3][4] = 1
wereld[0][9] = 1
wereld[0][0] = 1

nieuwe_cellen = []

for rij in range(hoogte):
    for cel in range(breedte):        
        aantal_buren = 0
        doelcel = (rij, cel)
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if not(i == 0 and j == 0): 
                    nieuwe_cel = ((doelcel[0] + i) % hoogte, (doelcel[1] + j) % breedte)
                    # print(nieuwe_cel)
                    if wereld[nieuwe_cel[0]][nieuwe_cel[1]] == 1:
                        aantal_buren += 1  
        nieuwe_cellen.append((doelcel, aantal_buren, wereld[doelcel[0]][doelcel[1]]))

# print(nieuwe_cellen)
# testcel = ((0,5), 0, 1)

prettyprintgrid(wereld)
print("-----")
nieuwe_wereld = maak_wereld(breedte, hoogte)

for coord, buren, oude_status in nieuwe_cellen:
    if oude_status:
        if buren < 2:
            nieuwe_wereld[coord[0]][coord[1]] = 0
        if buren == 2 or buren == 3:
            nieuwe_wereld[coord[0]][coord[1]] = 1
        if buren > 3:
            nieuwe_wereld[coord[0]][coord[1]] = 0
    else:
        if buren == 3:
            nieuwe_wereld[coord[0]][coord[1]] = 1

prettyprintgrid(nieuwe_wereld)

# for rij in nieuwe_wereld:
#     for cel in rij:
#         doelcel = (rij, cel)
#         for ncel in nieuwe_cellen:
#             if ncel[0] == doelcel:
#                 if ncel[2] == 1:
#                     if ncel[1] < 2:
#                         nieuwe_wereld[rij][cel] = 0


# prettyprintgrid(wereld)



# # 1, 4
# # 3, 4
# # 2, 5
# # 2, 3
# # 1, 3
# # 1, 5
# # 3, 3
# # 3, 5

# # buren = [(1, 4),
# # (3, 4),
# # (2, 5),
# # (2, 3),
# # (1, 3),
# # (1, 5),
# # (3, 3),
# # (3, 5)]

# # for buur_rij, buur_kolom in buren:
# #     print(wereld[buur_rij][buur_kolom])


