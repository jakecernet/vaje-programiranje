# Za vsako postajo zapiši največjo zabeleženo razliko med najnižjo in najvišjo temperaturo v istem dnevu. 
# (Obstaja, na primer, kraj, v katerem se je v enem dnevu temperatura vzpela z -26 na 6. Mogoče te zanima tudi, kateri in kdaj?) 
# Odgovor: Murska Sobota 29, Črnomelj 28, Maribor 24, Brnik 28, Lisca 17, ...

datoteka = open("vremenske-postaje.txt", "r", encoding="utf-8")

postaje = {}

for vrstica in datoteka:
    podatki = vrstica.split(",")
    ime = podatki[0]
    datum = podatki[1]
    temperatura_max = int(podatki[2])
    temperatura_min = int(podatki[3])

    razlika = temperatura_max - temperatura_min

    leto, mesec, dan = datum.split("-")

    if mesec.startswith("0"):
        mesec = mesec[1]
    if dan.startswith("0"):
        dan = dan[1]

    datum_izpis = "" + dan + ". " + mesec + ". " + leto

    if ime not in postaje:
        postaje[ime] = {"prva": datum_izpis, "zadnja": datum_izpis, "max_temp": temperatura_max, "max_razlika": razlika, "max_razlika_datum": datum_izpis}
    else:
        postaje[ime]["zadnja"] = datum_izpis

    if temperatura_max > postaje[ime]["max_temp"]:
        postaje[ime]["max_temp"] = temperatura_max

    if razlika > postaje[ime]["max_razlika"]:
        postaje[ime]["max_razlika"] = razlika
        postaje[ime]["max_razlika_datum"] = datum_izpis

for ime, datumi in postaje.items():
    print(f"Postaja: {ime}, Prva meritev: {datumi['prva']}, Zadnja meritev: {datumi['zadnja']}, Najvišja temperatura: {datumi['max_temp']}, Največja dnevna razlika: {datumi['max_razlika']} na datum: {datumi['max_razlika_datum']}")