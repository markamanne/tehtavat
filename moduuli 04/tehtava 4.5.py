yritykset=0
tunnus = ""
salasana = ""

while (tunnus!= "python" or salasana != "rules") and yritykset <5:
    tunnus = input("Käyttäjätunnus:")
    salasana = input("Salasana:")
    yritykset +=1

    if tunnus== "python" and salasana == "rules":
        print("tervetuloa")
    else:
        print("Pääsy evätty")

    