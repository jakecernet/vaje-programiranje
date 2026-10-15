# Izpiši vse temperature v datoteki temperature.txt.

temperature_file = open("datoteke/temperature.txt", "r")

for vrstica in temperature_file:
    print(vrstica)