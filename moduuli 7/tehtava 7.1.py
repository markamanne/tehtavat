vuodenajat = ("talvi", "talvi", "kevät", "kevät", "kevät", "kesä", "kesä", "kesä", "syksy", "syksy", "syksy", "talvi")

kuukausi = int(input("Anna kuukauden numero (1-12): "))
print(f"{kuukausi}. kuukausi kuuluu vuodenaikaan: {vuodenajat[kuukausi-1]}")