# Aufgabe 1 – Die Gauß-Aufgabe

# Berechne die Summe aller Zahlen zwischen 1 und 100, 
# wobei sowohl 1 als auch 100 mitgezählt werden sollen.

sum = 0

for num in range(1,101):
    sum += num
    
print(sum)