def prettyprintgrid(g):
    for row in g:
        print(row)

breedte, hoogte = 10, 10

def maak_wereld(breedte, hoogte):
    wereld = []
    for h in range(hoogte):
        nieuwe_rij = []
        for b in range(breedte):
            nieuwe_rij.append(0)
        wereld.append(nieuwe_rij)
    return wereld

wereld = maak_wereld(breedte, hoogte)


wereld[5][3] = 1 
wereld[5][4] = 1
wereld[5][5] = 1
wereld[4][5] = 1
wereld[3][4] = 1
wereld[0][9] = 1
wereld[0][0] = 1


nieuwe_cellen = []

def maak_lijst_buren(breedte, hoogte):
    for rij in range(hoogte):
        for cel in range(breedte):        
            aantal_buren = 0
            doelcel = (rij, cel)
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if not(i == 0 and j == 0): 
                        nieuwe_cel = ((doelcel[0] + i) % hoogte, (doelcel[1] + j) % breedte)
                        if wereld[nieuwe_cel[0]][nieuwe_cel[1]] == 1:
                            aantal_buren += 1
            nieuwe_cellen.append((doelcel, aantal_buren, wereld[doelcel[0]][doelcel[1]]))

nieuwe_wereld = maak_wereld(breedte, hoogte)

def maak_nieuwe_wereld(nieuwe_cellen):
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

iteration = 20

for number in range(iteration):
    if number == 0:
        prettyprintgrid(wereld)
        nieuwe_cellen.clear
        print()
    elif number % 2 == 1:
        maak_lijst_buren(breedte, hoogte)
        maak_nieuwe_wereld(nieuwe_cellen)
        prettyprintgrid(nieuwe_wereld)
        nieuwe_cellen.clear()
        wereld = nieuwe_wereld
        print()
    elif number % 2 == 0:
        maak_lijst_buren(breedte, hoogte)
        maak_nieuwe_wereld(nieuwe_cellen)
        prettyprintgrid(wereld)
        nieuwe_cellen.clear
        nieuwe_wereld = wereld
        print()