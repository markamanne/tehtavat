# Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän. Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan. Käytä for-toistorakennetta

import random
arpakuutiot= int(input("kuinka monta arpakuutiota heitetään?"))

summa=0

for i in range(arpakuutiot):
    heitto = random.randint(1,6)
    summa+=heitto
    print(f"heitto {i}: {heitto}")


print("-"*20)
print(f"silmälukujen summa on:{summa}")

