# Izpiši najvišjo in najnižjo vrednost - točneje, koliko največ in koliko najmanj yuanov je bil vreden evro.

file = open("datoteke/yuan.txt", "r")

max = 0
min = 0

for vrstica in file:
    vrednost = float(vrstica)
    if vrednost > max:
        max = vrednost
    if min == 0 or vrednost < min:
        min = vrednost

print("Najvišja vrednost: ", max)
print("Najnižja vrednost: ", min)