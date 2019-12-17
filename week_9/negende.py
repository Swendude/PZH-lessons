# DRY: DON'T REPEAT YOURSELF (GOED)
# WET: WRITE EVERYTHING TWICE (FOUT)

deelnemers = [['Erik'], ['Nicky'], ['Fiona'], ['Henk']]

# syntax voor functies:
# def <NAAM>(<ARGUMENTEN>):
#   <FUNCTIE BODY>

def vermen(foo, bar):
    return foo * bar

def verdub(foo):
    return vermen(2, foo)

def is_even(foo):
    return (foo % 2 == 0)

def raar(x):
    if x:
        return 8
    else:
        return {"Naam":"Hallo"}



# print(vermen)
# foobar = vermen
# print(foobar(2, 5))

prijzen = [1, 5 ,12, 90]
print(type(prijzen))
# nieuwe_prijzen = []
# for prijs in prijzen:
#     nieuwe_prijzen.append(vermen(2, prijs))

# print(nieuwe_prijzen)
# print(list(map(verdub,prijzen)))

# print(list(filter(is_even, prijzen)))

# schaap = vermen(10, 6)
# print(schaap)

# koe = vermen(bar=12, foo=6)
# print(koe)
# print(vermen(8, 5))

