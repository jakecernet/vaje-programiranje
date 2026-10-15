#Znaš izračunati poprečno temperaturo tako, kot to delajo pri smučarskih skokih, kjer ne upoštevajo tistega 
# ocenjevalca, ki je dal najmanjšo in ocenjevalca, ki je dal največjo oceno? Če je najmanjšo (ali največjo) 
# oceno dalo več ocenjevalcev, seveda odstranijo le enega. 
# (Nasvet: računaj vsoto, minimum in maksimum. Po zanki odšteješ minimum in maksimum od vsote ter 
# izračunaš povprečje.)

temperature_file = open("datoteke/temperature.txt", "r")

max_temp = 0
min_temp = 0
vsota_temp = 0

for line in temperature_file:
    temp = int(line)
    vsota_temp += temp
    if temp > max_temp:
        max_temp = temp
    if temp < min_temp:
        min_temp = temp

vsota_temp -= max_temp
vsota_temp -= min_temp

povprecna_temp = vsota_temp / 3

print("Povprečna temperatura (brez najnižje in najvišje):", povprecna_temp)