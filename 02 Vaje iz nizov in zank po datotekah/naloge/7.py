# Poleg tega za vsako postajo izpiši najvišje temperature, izmerjene na njej. 
# Odgovor: Murska Sobota 40, Črnomelj 40, Maribor 40, Brnik 38, Lisca 35, ... 
# Upoštevaj, da je datoteka sestavljena tako, da si vse meritve na neki postaji sledijo -- ko gremo iz

datoteka = open("vremenske-postaje.txt", "r", encoding="utf-8")

postaje = {}

for vrstica in datoteka:
    podatki = vrstica.split(",")
    ime = podatki[0]
    datum = podatki[1]
    temperatura_max = int(podatki[2])

    leto, mesec, dan = datum.split("-")

    if mesec.startswith("0"):
        mesec = mesec[1]
    if dan.startswith("0"):
        dan = dan[1]

    datum_izpis = "" + dan + ". " + mesec + ". " + leto

    if ime not in postaje:
        postaje[ime] = {"prva": datum_izpis, "zadnja": datum_izpis, "max_temp": temperatura_max}
    else:
        postaje[ime]["zadnja"] = datum_izpis

    if temperatura_max > postaje[ime]["max_temp"]:
        postaje[ime]["max_temp"] = temperatura_max

for ime, datumi in postaje.items():
    print(f"Postaja: {ime}, Prva meritev: {datumi['prva']}, Zadnja meritev: {datumi['zadnja']}, Najvišja temperatura: {datumi['max_temp']}")