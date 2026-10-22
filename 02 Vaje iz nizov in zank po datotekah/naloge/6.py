# Poleg tega izpiši pri vsaki postaji tudi datum prve in zadnje meritve. 
# Za Mursko Soboto mora izpisati 1. 1. 1961 (in ne 1961-01-01 ali kaj podobnega). 
# Predpostavi, da so meritve v datoteki urejene po datumih, od najstarejšega do najnovejšega.

datoteka = open("vremenske-postaje.txt", "r", encoding="utf-8")

postaje = {}

for vrstica in datoteka:
    podatki = vrstica.split(",")
    ime = podatki[0]
    datum = podatki[1]

    leto, mesec, dan = datum.split("-")

    if mesec.startswith("0"):
        mesec = mesec[1]
    if dan.startswith("0"):
        dan = dan[1]

    datum_izpis = "" + dan + ". " + mesec + ". " + leto

    if ime not in postaje:
        postaje[ime] = {"prva": datum_izpis, "zadnja": datum_izpis}
    else:
        postaje[ime]["zadnja"] = datum_izpis

for ime, datumi in postaje.items():
    print(f"Postaja: {ime}, Prva meritev: {datumi['prva']}, Zadnja meritev: {datumi['zadnja']}")