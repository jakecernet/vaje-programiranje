# Izpiši število dni, ko je temperatura višja od 17 stopinj.

temperature_file = open("datoteke/temperature.txt", "r")

stevec = 0

for vrstica in temperature_file:
    celzij = int(vrstica)
    if celzij > 17:
        stevec += 1

print("Število dni, ko je temperatura višja od 17 stopinj:", stevec)