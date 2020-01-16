from goller import maak_wereld, prettyprintgrid, maak_wereld, vul_wereld, tel_buren

breedte, hoogte = 10, 10

wereld = maak_wereld(breedte, hoogte)

wereld[2][4] = 1
wereld[1][4] = 1
wereld[3][4] = 1
wereld[0][9] = 1
wereld[0][0] = 1

iteraties = 20
for it in range(iteraties):
    prettyprintgrid(wereld)
    print("-----")
    nieuwe_cellen = tel_buren(wereld)    
    nieuwe_wereld = maak_wereld(breedte, hoogte)
    wereld = vul_wereld(nieuwe_cellen, nieuwe_wereld)