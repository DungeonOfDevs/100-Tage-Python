# Random-Modul

# Pseudozufallszahlengeneratoren:

# Computer sind nicht wirklich zufällig, da sie aus Schaltkreisen und Schaltern bestehen. 
# Dennoch ist Zufälligkeit sehr wichtig beim Entwickeln von Software – besonders bei Spielen. 
# Es wäre extrem langweilig, wenn jede Bewegung in einem Videospiel vorherbestimmt wäre.

# Deshalb haben Informatiker sogenannte Pseudozufallszahlengeneratoren entwickelt, zum Beispiel den Mersenne Twister:
# https://en.wikipedia.org/wiki/Mersenne_Twister

# Wenn du mehr darüber lernen möchtest, empfehle ich dieses Video von Khan Academy:
# https://www.youtube.com/watch?v=GtOt7EBNEwQ&ab_channel=KhanAcademyLabs

# Das Random-Modul in Python

# Die offizielle Dokumentation findest du hier:
# https://docs.python.org/3/library/random.html

# Um das Modul zu verwenden, musst du es zuerst importieren:

import random

zahl = random.random()
print(zahl)