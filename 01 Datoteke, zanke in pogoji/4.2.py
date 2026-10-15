# Napiši program, ki izpiše, s katerim kolesom se je peljal največkrat.

cube = 0
canyon = 0
nakamura = 0
stevens = 0

file = open("datoteke/kolesa.txt", "r")

for vrstica in file:
    if vrstica.strip() == "Cube":
        cube += 1
    elif vrstica.strip() == "Canyon":
        canyon += 1
    elif vrstica.strip() == "Nakamura":
        nakamura += 1
    elif vrstica.strip() == "Stevens":
        stevens += 1

if cube > canyon and cube > nakamura and cube > stevens:
    print("Največkrat se je peljal s kolesom Cube.")
elif canyon > cube and canyon > nakamura and canyon > stevens:
    print("Največkrat se je peljal s kolesom Canyon.")
elif nakamura > cube and nakamura > canyon and nakamura > stevens:
    print("Največkrat se je peljal s kolesom Nakamura.")
elif stevens > cube and stevens > canyon and stevens > nakamura:
    print("Največkrat se je peljal s kolesom Stevens.")
    