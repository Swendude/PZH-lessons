def prettyprintgrid(g):
    for row in g:
        print(row)

def maak_wereld(breedte, hoogte):
    wereld = []
    for h in range(hoogte):
        nieuwe_rij = []
        for b in range(breedte):
            nieuwe_rij.append(0)
        wereld.append(nieuwe_rij)
    # if breedte == 0 or hoogte == 0:
    #     return None
    return wereld

def tel_buren(wereld):
    nieuwe_cellen = []
    for rij in range(len(wereld)):
        for cel in range(len(wereld[0])):
            aantal_buren = 0
            doelcel = (rij, cel)
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if not(i == 0 and j == 0):
                        nieuwe_cel = ((doelcel[0] + i) %
                                    len(wereld), (doelcel[1] + j) % len(wereld[0]))
                        if wereld[nieuwe_cel[0]][nieuwe_cel[1]] == 1:
                            aantal_buren += 1
            nieuwe_cellen.append(
                (doelcel, aantal_buren, wereld[doelcel[0]][doelcel[1]]))
    return nieuwe_cellen


def vul_wereld(cellen, w):
    for coord, buren, oude_status in cellen:
        if oude_status:
            if buren < 2:
                w[coord[0]][coord[1]] = 0
            if buren == 2 or buren == 3:
                w[coord[0]][coord[1]] = 1
            if buren > 3:
                w[coord[0]][coord[1]] = 0
        else:
            if buren == 3:
                w[coord[0]][coord[1]] = 1
    return w