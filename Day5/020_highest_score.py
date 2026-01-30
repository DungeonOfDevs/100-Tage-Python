# Höchste Punktzahl (Highest Score)
# Beschreibung
# Summe

# Python besitzt viele eingebaute Funktionen, die uns beim Arbeiten mit Zahlen helfen.
# Eine davon berechnet die Summe (Gesamtwert), zum Beispiel:

student_scores = [180, 124, 165, 173, 189, 169, 146]
total_score = sum(student_scores)

# Wie funktioniert sum() im Hintergrund?

# Der Code wurde von den Entwicklern von Python geschrieben und könnte ungefähr so aussehen:

student_scores = [180, 124, 165]

sum = 0
for score in student_scores:
    sum += score

print(sum)
