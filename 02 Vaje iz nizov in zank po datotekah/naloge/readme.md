Za vaje potrebuješ datoteko `vremenske-postaje.txt`. Poberi in odzipaj. Vsaka vrstica ima štiri podatke: ime vremenske postaje, datum meritve ter najvišjo in najnižjo izmerjeno temperaturo v tem dnevu.

- Kateri sta najvišja in najnižja temperatura, izmerjeni kadarkoli v Sloveniji?
  <br>Odgovor: najvišja: 40, najnižja: -32

- Poleg tega izpiši, na katerih postajah sta bili tidve temperaturi izmerjeni.

- Poišči največjo zabeleženo razliko med najnižjo in najvišjo temperaturo v istem dnevu. (V enem izmed krajev se je v enem dnevu temperatura vzpela z -13 na 26). Izpiši še kraj in datum s to najvišjo dnevno razliko.

- Ponovi točke 1-3 samo za leto 2023. :) (Spomni se, da imajo nizi metodo startswith.)

- Izpiši imena vseh postaj. Vsako samo enkrat. Upoštevaj, da si meritve z iste postaje sledijo -- ko gremo iz Murske Sobote na Črnomelj, se nikoli ne vračamo v Črnomelj.

- Poleg tega izpiši pri vsaki postaji tudi datum prve in zadnje meritve. Za Mursko Soboto mora izpisati 1. 1. 1961 (in ne 1961-01-01 ali kaj podobnega). Predpostavi, da so meritve v datoteki urejene po datumih, od najstarejšega do najnovejšega.

- Poleg tega za vsako postajo izpiši najvišje temperature, izmerjene na njej. <br>Odgovor: Murska Sobota 40, Črnomelj 40, Maribor 40, Brnik 38, Lisca 35, ... Upoštevaj, da je datoteka sestavljena tako, da si vse meritve na neki postaji sledijo -- ko gremo iz

- Za vsako postajo zapiši največjo zabeleženo razliko med najnižjo in najvišjo temperaturo v istem dnevu. (Obstaja, na primer, kraj, v katerem se je v enem dnevu temperatura vzpela z -26 na 6. Mogoče te zanima tudi, kateri in kdaj?) <br>Odgovor: Murska Sobota 29, Črnomelj 28, Maribor 24, Brnik 28, Lisca 17, ...

- Za vse vremenske postaje izpiši povprečja najvišjih dnevnih temperatur. (Opomba: klic round(x, 1) zaokroži podano število x na eno decimalko.) Pazi: različni kraji imajo različno število meritev! <br>Odgovor: Murska Sobota 15.5, Črnomelj 17.1, Maribor 15.6, Brnik 14.9, Lisca 11.6, ...

- Tole bo zelo zoprno -- lahko rešuješ tudi le toliko časa, da vidiš, kako zoprno je. :) Kakšne so najvišje izmerjene temperature v Ljubljani za posamične mesece v letu? Se pravi, kakšna je bila najvišja temperatura januarja, februarja itn? (Izbereš lahko tudi drug kraj, recimo Kredarico.) (Nasvet: datum razbij na leto, mesec in dan. Potem predalčkaš po mesecih.) <br>Odgovor: Januar 16, Februar 22, Marec 25, April 29, Maj 33, ...

- Za tole velja enak komentar kot za prejšnjo nalogo. Kaj pa povprečne (najvišje) temperature po mesecih?
  <br>Odgovor: Januar 2.4, Februar 5.5, Marec 10.8, April 15.7, Maj 20.7, ...
