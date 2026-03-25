import random

def heitto():
    return random.randint(1,6)
def main():
    silmäluku=0
    while silmäluku !=6:
        silmäluku=heitto()
        print(f"heiton tulos:{silmäluku}")
if __name__ == "__main__":
        main()

