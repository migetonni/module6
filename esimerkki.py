def LaskeKolmionAla(kanta, korkeus):
    A = (kanta * korkeus) / 2
    print(f"Kolmion ala on {A:.2f}")

    return

ka = float(input("Anna kolmion kanta:"))
ko = float(input("Anna kolmion korkeus:"))
LaskeKolmionAla(ka, ko)
print(f"Pääohjelmassa kanta = {ka} ja korkeus = {ko}")