# Naloga za vaje

Datoteke, ki jih potrebujete za reševanje teh nalog, najdete na https://ucilnica.fri.uni-lj.si/mod/resource/view.php?id=53254.

## Primeri s predavanj

Nič ne bo škodilo, če to narediš znova - s čim manj škiljenja v zapiske. :)

- Izpiši vse temperature v datoteki temperature.txt.

- Izpiši vse temperature, vendar pretvorjene v Fahrenheite.

- Izpiši povprečno temperaturo.

- Izpiši vse temperature višje od 17 stopinj.

- Izpiši število dni, ko je temperatura višja od 17 stopinj.

- Izpiši najnižjo in najvišjo napovedano temperaturo. Poskusi oboje izračunati v okviru ene same zanke.

- Izpiši zaporedno številko dneva z najnižjo temperaturo.

## Še malo vremena

- Znaš izračunati poprečno temperaturo tako, kot to delajo pri smučarskih skokih, kjer ne upoštevajo tistega ocenjevalca, ki je dal najmanjšo in ocenjevalca, ki je dal največjo oceno? Če je najmanjšo (ali največjo) oceno dalo več ocenjevalcev, seveda odstranijo le enega. (Nasvet: računaj vsoto, minimum in maksimum. Po zanki odšteješ minimum in maksimum od vsote ter izračunaš povprečje.)

- Nariši (no, izpiši) graf temperatur:
      <pre>
          24 ************************
          18 ******************
          15 ***************
          16 ****************
          18 ******************
      </pre>

## Kitajci

V datoteki `yuan.txt` je tečaj evra proti kitajske valute yuan (ki se menda izgovori tako, kot bi Nemci izgovorili üen) v času od 1. aprila 2005 do 9. oktobra 2023, brez sobot in nedelj.

- Izpiši najvišjo in najnižjo vrednost - točneje, koliko največ in koliko najmanj yuanov je bil vreden evro.

- Koliko dni je bil evro vreden več ali enako 10 yuanov?

- Kolikšen delež dni (v odstotki) je bil evro vreden več ali enako 10 yuanov?

- Na kateri dan (zaporedna številka dneva) je evro prvič padel pod osem yuanov? (Opazka: na razmerje med yuanom in evrom najbrž vpliva predvsem ravnanje kitajske in ne toliko evropske banke. Ko je vrednost yuana nizka, je to lahko dobro za kitajski izvoz, čeprav stvari seveda niso tako preproste.)

- Malo težja: kako dolgo je najdaljše zaporedje dni, ko je bil evro vreden manj kot 8 yuanov?

- Še malo težja: na kateri dan se je začelo to zaporedje?

## Kolesa

Lastnik štirih koles različnih znamk (Cube, Canyon, Stevens, Nakamura) si v datoteko "kolesa.txt" beleži, kolikokrat se pelje s katerim.

- Napiši program, ki to prešteje in izpiše.

- Napiši program, ki izpiše, s katerim kolesom se je peljal največkrat.

Problem: iz razlogov, ki jih bomo spoznali zdaj zdaj, je na koncu vrstice, prebrane iz datoteke, še nekaj šare. Namesto niza "Cube" bo Python prebral "Cube\n". Če se želiš tega znebiti, dodaj vrstico vrstica = vrstica.strip() (ob predpostavki, da se prebrana vrstica nahaja v spremenljivki vrstica.)
