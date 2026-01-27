# TypeError

# Diese Fehler treten auf, wenn du den falschen Datentyp verwendest,
# z. B.:     len(12345)

# Da du der Funktion len() nur Zeichenketten (Strings) übergeben kannst, 
# verweigert sie die Ausführung und gibt einen TypeError zurück, wenn du ihr eine Zahl (Integer) übergibst.

# Aufgabe 1:
# Behebe die len()-Funktion so, dass sie keine Warnungen oder Fehler mehr verursacht.

lenght = len("12345")
print(lenght)

# oder ander Variante

print(len("12345"))