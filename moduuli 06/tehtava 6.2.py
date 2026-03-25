import random

def heitto(tahkot):
    return random.randint(1,tahkot)
def main():
    maksimi=int(input("montako tahkoa?"))
    silmäluku=0
    while silmäluku !=maksimi:
        silmäluku=heitto(maksimi)
        print(f"heiton tulos:{silmäluku}")
if __name__=="__main__":
    main()
    