# Aufgabe 1 – Kopf oder Zahl

# Erstelle ein Münzwurf-Programm mit dem Wissen über Zufälligkeit in Python.

# Das Programm soll bei jedem Start zufällig „Heads“ oder „Tails“ ausgeben.

import random

coin = random.randint(0,1)
print(coin)

if coin == 1:
    print("Kopf")
else: 
    print("Zahl")