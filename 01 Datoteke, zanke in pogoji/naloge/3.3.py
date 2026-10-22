# Kolikšen delež dni (v odstotki) je bil evro vreden več ali enako 10 yuanov?

file = open("datoteke/yuan.txt", "r")

dnevi = 0
dnevi_skupaj = 0

for vrstica in file:
    vrednost = float(vrstica)
    dnevi_skupaj += 1
    if vrednost >= 10:
        dnevi += 1

delež = (dnevi / dnevi_skupaj) * 100
print("Evro je bil vreden več ali enako 10 yuanov", delež, "% dni.")