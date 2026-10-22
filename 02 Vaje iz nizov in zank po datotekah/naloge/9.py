# Za vse vremenske postaje izpiši povprečja najvišjih dnevnih temperatur. 
# (Opomba: klic round(x, 1) zaokroži podano število x na eno decimalko.) 
# Pazi: različni kraji imajo različno število meritev! 
# Odgovor: Murska Sobota 15.5, Črnomelj 17.1, Maribor 15.6, Brnik 14.9, Lisca 11.6, ...

datoteka = open("vremenske-postaje.txt", "r", encoding="utf-8")

povprecja = {}

for vrstica in datoteka:
    podatki = vrstica.split(",")
    ime = podatki[0]
    temperatura_max = int(podatki[2])

    if ime not in povprecja:
        povprecja[ime] = {"vsota": temperatura_max, "stevilo_meritev": 1}
    else:
        povprecja[ime]["vsota"] += temperatura_max
        povprecja[ime]["stevilo_meritev"] += 1

for ime, podatki in povprecja.items():
    povprecje = podatki["vsota"] / podatki["stevilo_meritev"]
    povprecje_zaokrozena = round(povprecje, 1)
    print(f"Postaja: {ime}, Povprečna najvišja temperatura: {povprecje_zaokrozena}")