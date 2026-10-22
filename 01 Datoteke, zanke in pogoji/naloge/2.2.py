# Nariši (no, izpiši) graf temperatur

temperature = open("datoteke/temperature.txt", "r")

for vrstica in temperature:
    temp = int(vrstica)
    print(int(vrstica))
    for i in range(temp):
        print("*", end="")
    print()  # Premik na novo vrstico po vsaki temperaturi