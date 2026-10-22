# Ponovi točke 1-3 samo za leto 2023. :) (Spomni se, da imajo nizi metodo startswith.)

datoteka = open("vremenske-postaje.txt", "r", encoding="utf-8")

max_temp = float('-inf')
min_temp = float('inf')
max_temp_ime = ""
min_temp_ime = ""
max_razlika = float('-inf')
max_razlika_ime = ""
max_razlika_datum = ""

for vrstica in datoteka:
    podatki = vrstica.split(",")
    ime = podatki[0]
    datum = podatki[1]
    temperatura_max = int(podatki[2])
    temperatura_min = int(podatki[3])
    if datum.startswith("2023"):
        if temperatura_max > max_temp:
            max_temp = temperatura_max
            max_temp_ime = ime
        if temperatura_min < min_temp:
            min_temp = temperatura_min
            min_temp_ime = ime

        razlika = temperatura_max - temperatura_min

        if razlika > max_razlika:
            max_razlika = razlika
            max_razlika_ime = ime
            max_razlika_datum = datum
    else:
        continue

print("Najvišja temperatura v letu 2023:", max_temp, "na postaji:", max_temp_ime)
print("Najnižja temperatura v letu 2023:", min_temp, "na postaji:", min_temp_ime)
print("Največja dnevna razlika v letu 2023 je bila", max_razlika, "v kraju", max_razlika_ime, "na datum:", max_razlika_datum)