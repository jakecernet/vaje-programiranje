datoteka = open("datoteke/drazba-dolga.txt")
# datoteka = open("datoteke/drazba.txt")

prodanih = 0
najvisja_cena = 0
skup_cena = 0
ana_predmeti = 0
ana_pare = 0
berta_predmeti = 0
berta_pare = 0


ponudbe = []

for vrstica in datoteka:
	cena = int(vrstica)
	if cena == -1:
		koncna_cena = ponudbe[-1]
		prodanih += 1
		najvisja_cena = max(najvisja_cena, koncna_cena)
		skup_cena += koncna_cena

		if len(ponudbe) % 2 == 1:
			ana_predmeti += 1
			ana_pare += koncna_cena
		else:
			berta_predmeti += 1
			berta_pare += koncna_cena

		ponudbe = []
	else:
		ponudbe.append(cena)

print("Prodanih predmetov: ", prodanih)
print("Najvišja cena:", najvisja_cena)
print("Skupna cena:", skup_cena)
print("Ana:", ana_predmeti, "predmetov za", ana_pare)
print("Berta:", berta_predmeti,"predmetov za", berta_pare)
