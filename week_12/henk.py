# Opmerking van Henk: Aanpassingen in apart grid! Dus niet bewerken in huidig grid.

def prettyprintgrid(g):
    for row in g:
        print(row)

breedte, hoogte = 10, 10

# wereld = [row for row in ([0 for i in range(breedte)] for i in range(hoogte))]
# prettyprintgrid(wereld)

def maak_wereld(breedte, hoogte):
    wereld = []
    for h in range(hoogte):
        nieuwe_rij = []
        for b in range(breedte):
            nieuwe_rij.append(0)
        wereld.append(nieuwe_rij)
    return wereld

werelden = []
# wereld = maak_wereld(breedte, hoogte)
# werelden.append(wereld)
werelden.append(maak_wereld(breedte, hoogte))

werelden[0][5][3] = 1 
werelden[0][5][4] = 1
werelden[0][5][5] = 1
werelden[0][4][5] = 1
werelden[0][3][4] = 1
werelden[0][0][9] = 1
werelden[0][0][0] = 1

prettyprintgrid(werelden[0])

nieuwe_cellen = []
aantal_iteraties = 20

for iteratie in range(aantal_iteraties):
    # nieuwe_cellen = []

    for rij in range(hoogte):
        for cel in range(breedte):        
            aantal_buren = 0
            doelcel = (rij, cel)
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if not(i == 0 and j == 0): 
                        nieuwe_cel = ((doelcel[0] + i) % hoogte, (doelcel[1] + j) % breedte)
                        if werelden[iteratie][nieuwe_cel[0]][nieuwe_cel[1]] == 1:
                            aantal_buren += 1  
            nieuwe_cellen.append((iteratie, doelcel, aantal_buren, werelden[iteratie][doelcel[0]][doelcel[1]]))

    # print(nieuwe_cellen)

    nieuwe_wereld = maak_wereld(breedte, hoogte)
    werelden.append(nieuwe_wereld)
    
    for wereldnummer, coord, buren, oude_status in nieuwe_cellen:
        if oude_status:
            if buren < 2:
                werelden[iteratie+1][coord[0]][coord[1]] = 0
            if buren == 2 or buren == 3:
                werelden[iteratie+1][coord[0]][coord[1]] = 1
            if buren > 3:
                werelden[iteratie+1][coord[0]][coord[1]] = 0
        else:
            if buren == 3:
                werelden[iteratie+1][coord[0]][coord[1]] = 1
    # werelden.append(werelden[iteratie+1])
    print("-----" + str(iteratie+1) + "-----")
    prettyprintgrid(werelden[iteratie+1])
    
# print(len(werelden))