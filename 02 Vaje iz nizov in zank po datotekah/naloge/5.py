# Izpiši imena vseh postaj. Vsako samo enkrat. Upoštevaj, da si meritve z iste postaje sledijo -- ko gremo iz Murske Sobote na Črnomelj, se nikoli ne vračamo v Črnomelj.

datoteka = open("vremenske-postaje.txt", "r", encoding="utf-8")

imena_postaj = []

for vrstica in datoteka:
    podatki = vrstica.split(",")
    ime = podatki[0]

    if ime in imena_postaj:
        continue
    else:
        imena_postaj.append(ime)

for ime in imena_postaj:
    print(ime)