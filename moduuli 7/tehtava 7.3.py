lentoasemat = {}

while True:
    print("\nValitse toiminto:")
    print("1 - Syötä uusi lentoasema")
    print("2 - Hae lentoaseman tiedot")
    print("0 - Lopeta")

    valinta = input("Valintasi: ")

    if valinta == "1":
        icao = input("Anna lentoaseman ICAO-koodi: ").upper()
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[icao] = nimi
        print("Tiedot tallennettu.")

    elif valinta == "2":
        icao = input("Anna haettava ICAO-koodi: ").upper()
        if icao in lentoasemat:
            print(f"Lentoasema: {lentoasemat[icao]}")
        else:
            print("Koodia ei löydy järjestelmästä.")

    elif valinta == "0":
        print("Ohjelma päättyy.")
        break
    else:
        print("Virheellinen valinta.")