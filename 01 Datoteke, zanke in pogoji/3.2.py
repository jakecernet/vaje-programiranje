# Koliko dni je bil evro vreden več ali enako 10 yuanov?

file = open("datoteke/yuan.txt", "r")

dnevi = 0

for vrstica in file:
    vrednost = float(vrstica)
    if vrednost >= 10:
        dnevi += 1

print("Evro je bil vreden več ali enako 10 yuanov", dnevi, "dni.")