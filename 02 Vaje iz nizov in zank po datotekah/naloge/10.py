# Tole bo zelo zoprno -- lahko rešuješ tudi le toliko časa, da vidiš, kako zoprno je. :) 
# Kakšne so najvišje izmerjene temperature v Ljubljani za posamične mesece v letu? 
# Se pravi, kakšna je bila najvišja temperatura januarja, februarja itn? (Izbereš lahko tudi drug kraj, recimo Kredarico.) 
# (Nasvet: datum razbij na leto, mesec in dan. Potem predalčkaš po mesecih.) 
# Odgovor: Januar 16, Februar 22, Marec 25, April 29, Maj 33, ...

datoteka = open("vremenske-postaje.txt", "r", encoding="utf-8")

maksimumi = {}

for vrstica in datoteka:
    podatki = vrstica.split(",")
    ime = podatki[0]
    datum = podatki[1]
    temperatura_max = int(podatki[2])

    leto, mesec, dan = datum.split("-")

    if ime == "Ljubljana":
        if mesec not in maksimumi:
            maksimumi[mesec] = temperatura_max
        else:
            if temperatura_max > maksimumi[mesec]:
                maksimumi[mesec] = temperatura_max

for mesec, temperatura in maksimumi.items():
    print(f"Mesec: {mesec}, Najvišja temperatura: {temperatura}")