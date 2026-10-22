# Na kateri dan (zaporedna številka dneva) je evro prvič padel pod osem yuanov? 
# (Opazka: na razmerje med yuanom in evrom najbrž vpliva predvsem ravnanje kitajske in ne toliko evropske banke. 
# Ko je vrednost yuana nizka, je to lahko dobro za kitajski izvoz, čeprav stvari seveda niso tako preproste.)

file = open("datoteke/yuan.txt", "r")

dan = 0

for vrstica in file:
    dan += 1
    vrednost = float(vrstica)
    if vrednost < 8:
        print("Evro je prvič padel pod osem yuanov", dan, "dan.")
        break