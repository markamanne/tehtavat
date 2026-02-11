sukupuoli= input("oletko mies vai nainen:")
if sukupuoli=="mies":
    marvo = float(input("mikä on hemoglobiiniarvosi?"))
    if marvo < 134 :
        print("hemoglobiinisi on alhainen")
    elif marvo >195:
        print("hemoglobiinisi on liian korkea")
    else:
        print("olet normaali")
elif sukupuoli == "nainen":
    nhemo = float(input("mikä on hemoglobiiniarvosi?"))
    if nhemo < 117 :
        print("hemoglobiinisi on alhainen")
    elif nhemo > 195 :
        print("hemoglobiinisi on liian korkea")
    else:
        print("olet normaali")