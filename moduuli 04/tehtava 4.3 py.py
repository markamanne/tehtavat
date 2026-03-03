
pienin=None
suurin=None

print("syötä lukuja, tyhjä syöte lopettaa ohjelman.")

while True:
    syöte=input("anna luku")

    if syöte=="":
        break

    luku=float(syöte)

    if pienin is None or luku < pienin:
        pienin=luku
    if suurin is None or luku > suurin:
        suurin=luku

print(f"pienin oli {pienin} ja suurin oli {suurin}")




