# Zahlenmanipulation
# Beschreibung

# 1. Abrunden einer Zahl (Flooring)

# Du kannst eine Zahl abrunden bzw. alle Dezimalstellen entfernen, indem du die Funktion int() verwendest.
# Diese wandelt eine Fließkommazahl (mit Dezimalstellen) in eine Ganzzahl um.

int(3.738492)   # wird zu 3

bmi = 84 / 1.65 ** 2

print(bmi)              # 30.85399449035813


# 2. Runden einer Zahl

# Wenn du eine Dezimalzahl nach den klassischen mathematischen Regeln runden möchtest
# (alles über .5 wird aufgerundet, alles darunter abgerundet), kannst du die Python-Funktion round() verwenden.

round(3.738492)     # wird zu 4
round(3.14159)      # wird zu 3
round(3.14159, 2)   # wird zu 3.14

print(int(bmi))         # 30

print(round(bmi))       # 31

print(round(bmi, 2))    # 30.85
