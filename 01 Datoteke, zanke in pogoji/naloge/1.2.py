# Izpiši vse temperature, vendar pretvorjene v Fahrenheite.

temperature_file = open("datoteke/temperature.txt", "r")

for vrstica in temperature_file:
    celzij = int(vrstica)
    fahrenheit = (celzij * 9/5) + 32
    print("Celzij:", celzij, "-> Fahrenheit:", fahrenheit)