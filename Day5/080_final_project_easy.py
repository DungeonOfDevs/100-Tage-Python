# Passwortgenerator-Projekt
# Beschreibung

# Das Programm wird fragen:
# 1. Wie viele Buchstaben möchtest du in deinem Passwort haben?
# 2. Wie viele Symbole möchtest du haben?
# 3. Wie viele Zahlen möchtest du haben?

# Das Ziel ist es, die Eingaben des Benutzers zu übernehmen und daraus ein zufälliges Passwort zu generieren.
# Nutze dein Wissen über Python-Listen und Schleifen, um diese Aufgabe zu lösen.

# Demo https://appbrewery.github.io/python-day5-demo/

# Einfache Version (Easy Version)

# Erzeuge das Passwort in einer festen Reihenfolge:
# 1. Buchstaben → Symbole → Zahlen
# 2. Wenn der Benutzer z. B. möchte:    - 4 Buchstaben
#                                       - 2 Symbole
#                                       - 3 Zahlen

# dann könnte das Passwort so aussehen: fgdx$*924

# Du siehst, dass:
# 1. alle Buchstaben zusammenstehen,
# 2. alle Symbole zusammenstehen,
# 3. alle Zahlen ebenfalls zusammenstehen.
# 👉 Versuche zuerst diese Version zu lösen.

# 💡 Hinweis 1:
# Denke daran, dass du die Funktion random.choice() verwenden kannst, 
# um ein zufälliges Element aus einer Liste zu wählen.
# Vergiss nicht, vorher das random-Modul zu importieren.

# Schritt 1: import random
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Willkommen beim PyPassword-Generator!")
nr_letters = int(input("Wie viele Buchstaben möchtest du in deinem Passwort haben?\n"))
nr_symbols = int(input("Wie viele Symbole möchtest du haben?\n"))
nr_numbers = int(input("Wie viele Zahlen möchtest du haben?\n"))

# Schritt 2 - leerer Passwort Container
password = " "

# Schritt 3 - Buchstaben random
# kurze Schreibweise
for letter in range(1, nr_letters + 1):
    password += random.choice(letters)
    
# lange Schweibweise
# for letter in range(1, nr_letters + 1):
#     random_char = random.choice(letters)
#     password += random_char

# Schritt 4 - Zahlen random
# kurze Schreibweise
for num in range(1, nr_numbers + 1):
    password += random.choice(numbers)

# lange Schweibweise
# for num in range(1, nr_numbers + 1):
#     random_num = random.choice(numbers)
#     password += random_num

# Schritt 5 - Symbole random
#kurze Schreibweise
for symbol in range(1, nr_symbols + 1):
    password += random.choice(symbols)

# lange Schreibweise
# for symbol in range(1, nr_symbols + 1):
#     random_symbol = random.choice(symbols)
#     password += random_symbol

# Schritt 6 - Ausgabe Passwort
print(password)


