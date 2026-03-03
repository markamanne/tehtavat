vuosi=(int(input("mikä vuosi on")))

jaollinen_neljalla=(vuosi/4==vuosi//4)
jaollinen_sadalla=(vuosi/100==vuosi//100)
jaollinen_neljallasadalla=(vuosi/400==vuosi//400)

if(jaollinen_neljalla and not jaollinen_sadalla) or jaollinen_neljallasadalla:
    print("VOU; se on karkausvuosi")
else:
    print("Tämä ei ole karkausvuosi")



