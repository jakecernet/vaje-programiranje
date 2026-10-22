# Za tole velja enak komentar kot za prejšnjo nalogo. Kaj pa povprečne (najvišje) temperature po mesecih? 
# Odgovor: Januar 2.4, Februar 5.5, Marec 10.8, April 15.7, Maj 20.7, ...

datoteka = open("vremenske-postaje.txt", "r", encoding="utf-8")

povprecja = {}

for vrstica in datoteka:
    podatki = vrstica.split(",")
    ime = podatki[0]
    datum = podatki[1]
    temperatura_max = int(podatki[2])

    leto, mesec, dan = datum.split("-")

    if mesec not in povprecja:
        povprecja[mesec] = {"vsota": temperatura_max, "stevilo_meritev": 1}
    else:
        povprecja[mesec]["vsota"] += temperatura_max
        povprecja[mesec]["stevilo_meritev"] += 1

for mesec, podatki in povprecja.items():
    povprecje = podatki["vsota"] / podatki["stevilo_meritev"]
    povprecje_zaokrozena = round(povprecje, 1)
    print(f"Mesec: {mesec}, Povprečna najvišja temperatura: {povprecje_zaokrozena}")