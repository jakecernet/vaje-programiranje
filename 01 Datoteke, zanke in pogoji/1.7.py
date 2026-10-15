# Izpiši zaporedno številko dneva z najnižjo temperaturo.

temperature_file = open("datoteke/temperature.txt", "r")

min_temp = temperature_file.readline()
min_day = 1

for vrstica in temperature_file:
    if vrstica < min_temp:
        min_temp = vrstica
        min_day += 1
    
print("Dan z najnižjo temperaturo:", min_day)