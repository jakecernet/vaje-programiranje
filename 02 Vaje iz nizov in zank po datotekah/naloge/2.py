# Poleg tega izpiši, na katerih postajah sta bili tidve temperaturi izmerjeni.

datoteka = open("vremenske-postaje.txt", "r", encoding="utf-8")

max_temp = float('-inf')
min_temp = float('inf')
max_temp_ime = ""
min_temp_ime = ""

for vrstica in datoteka:
    podatki = vrstica.split(",")
    ime = podatki[0]
    datum = podatki[1]
    temperatura_max = int(podatki[2])
    temperatura_min = int(podatki[3])

    if temperatura_max > max_temp:
        max_temp = temperatura_max
        max_temp_ime = ime
    if temperatura_min < min_temp:
        min_temp = temperatura_min
        min_temp_ime = ime

print("Najvišja temperatura:", max_temp, "na postaji:", max_temp_ime)
print("Najnižja temperatura:", min_temp, "na postaji:", min_temp_ime)