while True:
    tuumat = float(input("anna tuumat: "))
    if tuumat <0:
        print("eihän ne tuumat varmaan miinuksella ole")
        break

    sentit=tuumat*2.54
    print(f"{tuumat} tuumaa on {sentit} senttimetriä")


