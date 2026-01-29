# Alternative: uniform()

# Eine weitere Möglichkeit für Zufallszahlen mit Nachkommastellen ist:

import random
random_float = random.uniform(1, 10)


# Dies erzeugt eine zufällige Fließkommazahl zwischen 1 und 10.

# Je nach Rundung kann oder kann nicht die obere Grenze enthalten sein.
# Formal gilt:

# a <= random.uniform(a, b) <= b


# Deshalb gilt:
# random.random() → obere Grenze nie enthalten
# random.uniform() → obere Grenze möglicherweise enthalten

print(random_float)