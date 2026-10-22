# Še malo težja: na kateri dan se je začelo to zaporedje?

file = open("datoteke/yuan.txt", "r")

dan = 0
dan_max = 0
dan_zacetek = 0
dnevi = 0

for vrstica in file:
    vrednost = float(vrstica)
    dnevi += 1
    if vrednost < 8:
        dan += 1
        if dan > dan_max:
            dan_max = dan
            dan_zacetek = dnevi - dan + 1
    else:
        dan = 0

print("Najdaljše zaporedje dni, ko je bil evro vreden manj kot 8 yuanov:", dan_max, "dni.")
print("To zaporedje se je začelo na", dan_zacetek, "dan.")
