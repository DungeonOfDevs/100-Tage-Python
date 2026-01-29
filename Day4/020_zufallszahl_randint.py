# Zufällige ganze Zahlen in einem Bereich

import random
import my_module    # selbst erstelltes Module

rand_num = random.randint(1, 10)

# Dies erzeugt eine zufällige ganze Zahl zwischen 1 und 10 (einschließlich).

print(rand_num)

zahl = random.randint(1, 100)
print(zahl)

# Module in Python

# Python erlaubt es, Code auf verschiedene Dateien aufzuteilen und diesen bei Bedarf zu importieren.
# Dadurch können Programme besser organisiert und modular aufgebaut werden.

# Du kannst ein eigenes Modul erstellen, indem du einfach eine neue .py-Datei anlegst.
# Anschließend kannst du Variablen oder Funktionen daraus mit dem import-Schlüsselwort einbinden.

print(my_module.my_favourite_number)    # my_module = Datei auf die ich zugreife + my_favourite_number = Variable die ich in my_module erstellt habe