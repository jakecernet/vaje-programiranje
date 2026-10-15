# Izpiši povprečno temperaturo.

temperature_file = open("datoteke/temperature.txt", "r")

vsota = 0
stevec = 0

for vrstica in temperature_file:
    celzij = int(vrstica)
    vsota += celzij
    stevec += 1

povprecje = vsota / stevec
print("Povprečna temperatura:", povprecje)