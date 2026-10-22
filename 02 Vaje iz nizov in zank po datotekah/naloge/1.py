# Kateri sta najvišja in najnižja temperatura, izmerjeni kadarkoli v Sloveniji?
# Odgovor: najvišja: 40, najnižja: -32

datoteka = open("vremenske-postaje.txt", "r", encoding="utf-8")

vrednosti = []

for vrstica in datoteka:
    podatki = vrstica.split(",")
    ime = podatki[0]
    datum = podatki[1]
    temperatura_max = int(podatki[2])
    temperatura_min = int(podatki[3])

    vrednosti.append(temperatura_max)
    vrednosti.append(temperatura_min)

najvisja = max(vrednosti)
najnizja = min(vrednosti)

print("Najvišja temperatura:", najvisja)
print("Najnižja temperatura:", najnizja)