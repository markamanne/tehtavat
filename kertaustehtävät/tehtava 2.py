tuntipalkka=float(input("Paljonko tuntipalkkasi on?:"))
Tunnit=float(input("Tehdyt tunnit:"))
Paiva=input("viikonpäivä:").lower()

if Paiva == "sunnuntai":
    print(f"Päivän palkkasi on :{tuntipalkka*2*Tunnit}")

else:
    print(f"Päivän palkkasi on:{tuntipalkka*Tunnit}")