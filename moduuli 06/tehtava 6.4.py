def laske_summa(lukulista):
    summa = 0
    for luku in lukulista:
        summa += luku
    return summa
def main():
    minun_lista = [5, 10, 15, 20, 25]
    tulos = laske_summa(minun_lista)

    print(f"Listan {minun_lista} lukujen summa on: {tulos}")
if __name__ == "__main__":
    main()
    