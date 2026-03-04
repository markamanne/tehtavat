while True:

    lasku=input("valitse seuraavista vaihtoehdoista : yhteenlasku, jakolasku, miinuslasku tai kertolasku  (muu merkintä lopettaa ohjelman):")
    luku1=float(input("anna ensimmäinen luku"))
    luku2= float(input("anna toinen luku"))

    if lasku =="yhteenlasku":
        print(f"{luku1+luku2}")
    elif lasku=="jakolasku":
        print(f"{luku1/luku2}")
    elif lasku=="miinuslasku":
        print(f"{luku1-luku2}")
    elif lasku=="kertolasku":
        print(f"{luku1*luku2}")
    elif lasku=="lopetus":
        print("haha nyt loppu")

        break

