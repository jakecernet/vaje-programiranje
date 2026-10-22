def najvisja_cena():
    datoteka = open("zapisnik.txt", "r", encoding="utf-8")
    najvisja = 0
    for vrstica in datoteka:
        cena = int(vrstica.split(",")[2])
        if cena > najvisja:
            najvisja = cena
    return najvisja

def najdrazji_predmet():
    datoteka = open("zapisnik.txt", "r", encoding="utf-8")
    najdrazji = ""
    najvisja = 0
    for vrstica in datoteka:
        cena = int(vrstica.split(",")[2])
        if cena > najvisja:
            najvisja = cena
            najdrazji = vrstica.split(",")[0]
    return najdrazji

def izpisi_seznam():
    datoteka = open("zapisnik.txt", "r", encoding="utf-8")
    predmeti = []
    for vrstica in datoteka:
        predmet = "- " + vrstica.split(",")[0]
        if predmet not in predmeti:
            predmeti.append(predmet)
    return predmeti

def prestej_imena():
    datoteka = open("zapisnik.txt", "r", encoding="utf-8")
    imena = {}
    for vrstica in datoteka:
        ime = vrstica.split(",")[1]
        if ime in imena:
            imena[ime] += 1
        else:
            imena[ime] = 1
    return imena

print("Najvišja cena je:", najvisja_cena())
print("Najdražji predmet je:", najdrazji_predmet())
print("Seznam vseh predmetov:\n", "\n".join(izpisi_seznam()), "\n", "Skupaj", len(izpisi_seznam()), "predmetov.")
print("Število posameznih imen:")
for ime, stevilo in prestej_imena().items():
    print(ime, ":", stevilo)