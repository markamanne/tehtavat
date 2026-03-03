import math

# Kysytään säde ja muutetaan se heti tekstistä luvuksi (float)
sade_str = input("Anna ympyrän säde: ")
sade = float(sade_str)

# Lasketaan pinta-ala: pii * säde toiseen potenssiin
pinta_ala = math.pi * (sade ** 2)

# Tulostetaan vastaus
print("Ympyrän pinta-ala on: "
      + str(pinta_ala))