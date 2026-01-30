# For-Schleifen mit range
# Beschreibung

# Die Kombination aus der range()-Funktion und der Python-for-Schleife ermöglicht 
# es uns, eine Schleife so oft auszuführen, wie wir möchten.

# Anstatt jedes Element einer Liste zu durchlaufen, 
# können wir auch einen Zahlenbereich durchlaufen.

# Die range-Funktion
# range(1, 10)

# Dieser Code macht für sich allein nichts.
# Wenn man ihn z. B. ausgeben möchte, erhält man keine einzelnen Zahlen.

# Verwendung mit for-Schleifen
# for number in range(1, 10):
#     print(number)


# Dies gibt alle Zahlen von 1 bis 9 aus.

# Wichtiges Prinzip von range()

# Der Zahlenbereich kann auch so beschrieben werden:    a ≤ range(a, b) < b


# Das bedeutet:

# Die untere Grenze ist inklusive
# Die obere Grenze ist exklusiv (zählt nicht mit)

# Beispiel : 
# Wenn du die Zahlen 1 bis 10 ausgeben willst, musst du schreiben:

# range(1, 11)

#range() Funktion
print(range(1,10))

# range() Funktion mit For Loop

for number in range(1,10):      # 1 bis 10, aber ohne 10 auszugeben
    print(number)
    
for num in range(1,11,3):   # 1 = Startwert | 11 = Endwert | 3 = Schrittweite
    print(num)              # Ausgabe= 1, 4, 7, 10