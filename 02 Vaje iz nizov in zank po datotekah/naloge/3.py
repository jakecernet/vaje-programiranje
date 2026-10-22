# Poišči največjo zabeleženo razliko med najnižjo in najvišjo temperaturo v istem dnevu. 
# (V enem izmed krajev se je v enem dnevu temperatura vzpela z -13 na 26). Izpiši še kraj in datum s to najvišjo dnevno razliko.

datoteka = open("vremenske-postaje.txt", "r", encoding="utf-8")

max_razlika = float('-inf')
max_razlika_ime = ""
max_razlika_datum = ""

for vrstica in datoteka:
    podatki = vrstica.split(",")
    ime = podatki[0]
    datum = podatki[1]
    temperatura_max = int(podatki[2])
    temperatura_min = int(podatki[3])

    razlika = temperatura_max - temperatura_min

    if razlika > max_razlika:
        max_razlika = razlika
        max_razlika_ime = ime
        max_razlika_datum = datum

print("Največja dnevna razlika je bila", max_razlika, "v kraju:", max_razlika_ime, "na datum:", max_razlika_datum)