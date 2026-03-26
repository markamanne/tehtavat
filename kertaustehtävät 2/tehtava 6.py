def summa(a, b):
    return a + b


def erotus(a, b):
    return a - b


def tulo(a, b):
    return a * b


def osamäärä(a, b):
    if b == 0:
        return "Virhe: nollalla ei voi jakaa!"
    return a / b


def main():
    print("--- Funktiolaskin ---")

    luku1 = float(input("Anna ensimmäinen luku: "))
    luku2 = float(input("Anna toinen luku: "))

    print("\nValitse toiminto:")
    print("1: Summa (+)")
    print("2: Erotus (-)")
    print("3: Tulo (*)")
    print("4: Osamäärä (/)")

    valinta = input("Valintasi (1-4): ")

    if valinta == '1':
        tulos = summa(luku1, luku2)
        merkki = "+"
    elif valinta == '2':
        tulos = erotus(luku1, luku2)
        merkki = "-"
    elif valinta == '3':
        tulos = tulo(luku1, luku2)
        merkki = "*"
    elif valinta == '4':
        tulos = osamäärä(luku1, luku2)
        merkki = "/"
    else:
        print("Virheellinen valinta.")
        return

    print(f"\nTulos: {luku1} {merkki} {luku2} = {tulos}")
if __name__ == "__main__":
    main()