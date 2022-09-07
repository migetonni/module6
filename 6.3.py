

def muuttaja(US_gallons):
    litra = US_gallons * 3.785
    return litra



Anna_gallonat = float(input("Anna gallonat: "))
litrat = muuttaja(Anna_gallonat)

while Anna_gallonat >-1:
    print(litrat)
    if litrat != "":
        Anna_gallonat = float(input("Anna gallonat: "))
        litrat = muuttaja(Anna_gallonat)




