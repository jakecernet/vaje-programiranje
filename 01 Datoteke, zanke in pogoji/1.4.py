# Izpiši vse temperature višje od 17 stopinj.

temperature_file = open("datoteke/temperature.txt", "r")

for vrstica in temperature_file:
    celzij = int(vrstica)
    if celzij > 17:
        print(celzij)