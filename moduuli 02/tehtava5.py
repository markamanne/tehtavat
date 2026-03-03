leiviskä=float(input("anna leiviskät: "))
naula=float(input("anna naulat"))
luoti=(float(input("anna luodit")))

leiviskäluoti=leiviskä*20*32
naulaluoti=naula*32
yhteensäluoti=leiviskäluoti+naulaluoti+luoti

yhteensä_gramma= yhteensäluoti*13.3
kilogramma= (int(yhteensä_gramma/1000))

gramma= yhteensä_gramma -(kilogramma*1000)
print("massa nykymittojen mukaan: ")
print(f"{kilogramma} kilogrammaa ja {gramma:.2f} grammaa")

