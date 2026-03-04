import math
while True:
    luku= float(input("anna luku:"))
    if(luku>0):
        print(math.sqrt(luku))
        break
    else:
        print("Virheellinen luku")
