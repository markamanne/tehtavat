luvut = []
syote = input("anna luku tai lopeta painamalla enteriä")

while syote != "":
    luku=float(syote)
    luvut.append(luku)

    syote=input("anna seuraava luku tai lopeta painamaalla enteriä ")

luvut.sort(reverse=True)

print("\nViisi suurinta lukua ovat: ")

for n in luvut [0:5]:
    print(n)

