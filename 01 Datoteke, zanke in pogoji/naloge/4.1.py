# Napiši program, ki to prešteje in izpiše.

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

print("Cube:", cube)
print("Canyon:", canyon)
print("Nakamura:", nakamura)
print("Stevens:", stevens)
    