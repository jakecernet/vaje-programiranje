# Izpiši najnižjo in najvišjo napovedano temperaturo. Poskusi oboje izračunati v okviru ene same zanke.

temperature_file = open("datoteke/temperature.txt", "r")

max = temperature_file.readline()
min = max

for vrstica in temperature_file:
    celzij = vrstica
    if celzij > max:
        max = vrstica
    if celzij < min:
        min = vrstica

print("Najnižja temperatura:", min)
print("Najvišja temperatura:", max)
