def toinenfunktio():
    print("Ollaan toisessa funktiossa")
    

def tervehdi():
    print("MOi")
    toinenfunktio()
    print("Tämä on tervehdys funktiosta")
    return

print("Ollaan pääohjelmassa")
tervehdi()
tervehdi()
toinenfunktio()
print(f"Olemme \n takaisin pääohjelmassa")