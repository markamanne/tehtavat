kaupungit= []
for i in range (5):
    nimi= input (f"anna {i+1}).kaupungin nimi: ")
    kaupungit.append(nimi)
print("\nSyöttämäsi kaupungit ovat:")

for kaupunki in kaupungit:
    print(kaupunki)


