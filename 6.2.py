import random


def heitaNoppaa(tahkot):
    luku = random.randint(1, tahkot)
    return luku

tahkoLKM = int(input("Kuinka monta tahkoa?"))
while True:
    silmäluku = heitaNoppaa(tahkoLKM)
    print(silmäluku)
    if silmäluku == tahkoLKM:
        break