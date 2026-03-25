def karsi_parittomat(alkuperainen_lista):
    parilliset = []
    for luku in alkuperainen_lista:
        if luku % 2 == 0:
            parilliset.append(luku)
    return parilliset


def main():
    testi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    karsittu_lista = karsi_parittomat(testi_lista)
    print(f"Alkuperäinen lista: {testi_lista}")
    print(f"Karsittu lista (vain parilliset): {karsittu_lista}")
if __name__ == "__main__":
    main()