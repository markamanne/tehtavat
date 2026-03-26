def suurin_arvo(luku1, luku2, luku3):
    if luku1 >= luku2 and luku1 >= luku3:
        return luku1
    elif luku2 >= luku1 and luku2 >= luku3:
        return luku2
    else:
        return luku3
def main():
    a = float(input("Anna ensimmäinen luku: "))
    b = float(input("Anna toinen luku: "))
    c = float(input("Anna kolmas luku: "))
    tulos = suurin_arvo(a, b, c)
    print(f"Luvuista {a}, {b} ja {c} suurin on: {tulos}")
if __name__ == "__main__":
    main()