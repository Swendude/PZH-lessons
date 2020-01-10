# Opmerking van Henk: Aanpassingen in apart grid! Dus niet bewerken in huidig grid.

def prettyprintgrid(g):
    for row in g:
        print(row)

breedte, hoogte = 10, 10

# wereld = [row for row in ([0 for i in range(breedte)] for i in range(hoogte))]
# prettyprintgrid(wereld)

wereld = []

for h in range(hoogte):
    nieuwe_rij = []
    for b in range(breedte):
        nieuwe_rij.append(0)
    wereld.append(nieuwe_rij)

wereld[2][4] = 1 
wereld[1][4] = 1
wereld[3][4] = 1

for rij in range(hoogte):
    for cel in range(breedte):        
        aantal_buren = 0
        doelcel = (rij, cel)
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if not(i == 0 and j == 0): 
                    nieuwe_cel = (doelcel[0] + i, doelcel[1] + j)
                    if wereld[nieuwe_cel[0]][nieuwe_cel[1]] == 1:
                        aantal_buren += 1
        print((rij,cel), aantal_buren)



prettyprintgrid(wereld)



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


