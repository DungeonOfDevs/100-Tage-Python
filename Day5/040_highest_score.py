# Deine Aufgabe

# Finde heraus, wie Python-Programmierer diese Funktionen mithilfe von Schleifen und Bedingungen gebaut haben könnten.
# ⚠️ Löse diese Aufgabe OHNE max() zu benutzen
# Du bekommst eine Liste mit Prüfungsergebnissen und sollst die höchste Punktzahl aus der Liste ausgeben.
# Dabei sollst du verwenden, was du über:

#  - Listen
#  - For-Schleifen
#  - Bedingungen (if)

# gelernt hast.

# Beispiel

# Wenn die Ergebnisse so lauten:     8 65 89 86 55 91 64 89

# Dann soll dein Programm ausgeben:  91

student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

max_score = 0
for score in student_scores:    # geht jede einzelne Zahl durch
    if score > max_score:       # vergleicht aktuelle Zahl mit der bisher höchsten
        max_score = score       # speichert die neue höchste Zahl

print(max_score)

##########################################################################

# Extra: kleinster score

student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

min_score = student_scores[0]

for score in student_scores:
    if score < min_score:
        min_score = score

print(min_score)
