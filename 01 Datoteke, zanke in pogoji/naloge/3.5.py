# Malo težja: kako dolgo je najdaljše zaporedje dni, ko je bil evro vreden manj kot 8 yuanov?

file = open("datoteke/yuan.txt", "r")

dan = 0
dan_max = 0

for vrstica in file:
    vrednost = float(vrstica)
    if vrednost < 8:
        dan += 1
        if dan > dan_max:
            dan_max = dan
    else:
        dan = 0

print("Najdaljše zaporedje dni, ko je bil evro vreden manj kot 8 yuanov:", dan_max, "dni.")