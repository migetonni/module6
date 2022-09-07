import random

def heitaNoppaa():
    luku = random.randint(1, 6)
    return luku

while True:
    silmäluku = heitaNoppaa()
    print(silmäluku)
    if silmäluku == 6:
        break