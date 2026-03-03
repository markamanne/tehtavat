import random


eka_koodi = f"{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}"


toka_koodi = f"{random.randint(1,6)}{random.randint(1,6)}{random.randint(1,6)}{random.randint(1,6)}"

print(f"Kolmenumeroinen lukko: {eka_koodi}")
print(f"Nelinumeroinen lukko: {toka_koodi}")