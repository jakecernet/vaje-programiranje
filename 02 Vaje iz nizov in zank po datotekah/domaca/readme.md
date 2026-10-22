# Dražba brez anonimnosti

Na dražbi seveda nimajo tako nepopolnih zapisnikov, kot je namigovala prejšnja naloga. Ve se, katere predmete prodajajo. Na dražbe tudi ne hodita le Ana in Berta; Ani seveda ni treba vedno začeti izklicevanja.

V resnici so zapisniki videti tako:

<pre>
slika,Berta,31
slika,Ana,33
slika,Berta,35
slika,Ana,40
pozlačen dežnik,Ema,29
Meldrumove vaze,Ana,46
Meldrumove vaze,Berta,61
Meldrumove vaze,Ana,63
Meldrumove vaze,Cilka,67
skodelice,Dani,50
skodelice,Berta,55
skodelice,Dani,60
skodelice,Berta,61
</pre>

Vsaka vrstica vsebuje tri podatke, ločene z vejico. Prvi je prodajani predmet, drugi je ime osebe, ki viša ceno, in tretji je ponujena cena. Pri branju si bomo (lahko) pomagali s tem, da vemo naslednje:

- Na dražbi (vedno) nastopa pet oseb: Ana, Berta, Cilka, Dani in Ema.
- Vsak predmet nastopa le v zaporednih vrsticah: ko je slika prodana (Ani za 40), se v datoteki ne pojavi nikoli več.

Ne smete predpostaviti, da na dražbi prodajajo natančno te predmete, ki se pojavijo v datoteki. Program naj pravilno deluje tudi za drugačne datoteke, vendar seveda v enaki obliki in z istimi udeleženkami.

## Naloge

- Izpišite, kakšna je bila najvišja dosežena cena. Za datoteko priloženo nalogi se izpiše: Najvišja cena: 107.
- Izpišite, kateri predmet je dosegel najvišjo ceno. Za datoteko iz naloge: Najdražji predmet: kip.

- Izpišite seznam predmetov. Vsak naj bo izpisan le enkrat. Pred vsakim elementom seznama bodi "- ". Na koncu naj se izpiše še skupno število predmetov.

    Seznam predmetov:
    - slika
    - pozlačen dežnik
    - Meldrumove vaze
    - skodelice
    - kip
    - čajnik
    - srebrn jedilni servis
    - perzijska preproga

    Skupaj: 8 predmetov

- Izpišite, kolikokrat se v datoteko pojavi posamično ime.
  <pre>
      Ana: 4
      Berta: 18
      Cilka: 12
      Dani: 15
      Ema: 11
  </pre>

Zadnja naloga bo kar nadležna. Namen je prav v tem, da jo bomo prihodnji teden rešili veliko elegantneje.
