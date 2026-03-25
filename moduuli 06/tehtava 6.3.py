def gallona_litroiksi(gallonat):
    return gallonat * 3.785
def main ():
    while True:
        syöte=float(input("bensiinin määrä gallonoina (ei negatiivinen)"))

        if syöte < 0:
            print ("ohjelma loppuu")
            break
        litrat = gallona_litroiksi(syöte)
        print(f"{syöte} gallona on {litrat:,.3f} litraa.")
if __name__=="__main__":
    main()

