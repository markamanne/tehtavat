import random

oikea_luku = random.randint (1,10)
arvaus=0

while arvaus != oikea_luku:
    arvaus=int(input("arvaa minkä luvun valitsin 1 ja 10 väliltä:"))
    if arvaus>oikea_luku:
        print("Liian suuri, kokeile uudestaan")
    elif arvaus<oikea_luku:
        print("Liian pieni, kokeile uudestaan")
    else:
        print("ooooikein")

