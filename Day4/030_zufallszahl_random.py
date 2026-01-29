# Zufällige Fließkommazahlen (Floats)

# Du kannst eine zufällige Zahl zwischen 0.0 (inklusive) und 1.0 (exklusive) erzeugen:

import random
rand_num_0_to_1 = random.random()

# Das lässt sich auch so ausdrücken:

# 0.0 <= random.random() < 1.0

print(rand_num_0_to_1)


# Bereich erweitern

# Durch Multiplikation kannst du den Zahlenbereich vergrößern:

zahl = random.random() * 5     # Ergebnis: # → Zufällige Zahl zwischen 0 und 5
print(zahl)