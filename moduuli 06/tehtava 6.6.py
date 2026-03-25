import math

def laske_neliöhinta(halkaisija_cm, hinta_euro):
    säde_m = (halkaisija_cm / 2) / 100

    pinta_ala = math.pi * (säde_m ** 2)

    yksikköhinta = hinta_euro / pinta_ala
    return yksikköhinta

def main():
    halkaisija1 = float(input("Anna 1. pizzan halkaisija (cm): "))
    hinta1 = float(input("Anna 1. pizzan hinta (€): "))

    halkaisija2 = float(input("Anna 2. pizzan halkaisija (cm): "))
    hinta2 = float(input("Anna 2. pizzan hinta (€): "))

    yksikko1 = laske_neliöhinta(halkaisija1, hinta1)
    yksikko2 = laske_neliöhinta(halkaisija2, hinta2)

    print(f"1. pizzan neliöhinta: {yksikko1:.2f} €/m2")
    print(f"2. pizzan neliöhinta: {yksikko2:.2f} €/m2")
    if yksikko1 < yksikko2:
        print("Ensimmäinen pizza antaa paremman vastineen rahalle.")
    elif yksikko2 < yksikko1:
        print("Toinen pizza antaa paremman vastineen rahalle.")
    else:
        print("Pizzat ovat saman hintaisia neliömetriltään.")
if __name__ == "__main__":
    main()