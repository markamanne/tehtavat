def main():
    luvut=[]

    while True:
        syöte = int(input("uusi arvo:"))

        if syöte == 0:
            print("moikka")
            break

        luvut.append(syöte)
        print(f"lista nytten: {luvut}")

        lista_jarjestyksessa = sorted (luvut)
        print(f"lista järkässä: {lista_jarjestyksessa}")

if __name__=="__main__":
    main()
