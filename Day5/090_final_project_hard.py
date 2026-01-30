# Schwierige Version (Hard Version)

# Wenn du die einfache Version geschafft hast, bist du bereit für die schwere Version.
# In der erweiterten Version folgt das Passwort keinem festen Muster mehr.
# Das Beispiel oben könnte dann z. B. so aussehen:

# x$d24g*f9


# Jedes Mal, wenn ein Passwort generiert wird, sind die Positionen von: - Buchstaben
#                                                                       - Zahlen
#                                                                       - Symbolen unterschiedlich.

# Dadurch wird das Passwort deutlich schwerer zu knacken.

# 🧠 Wichtige Lernbotschaft

# Eine der wichtigsten Fähigkeiten eines guten Programmierers ist es, Google zu benutzen, um Lösungen zu finden.

# Dein Gehirn ist zum Denken da – nicht zum Auswendiglernen von Funktionen.

# Für die schwere Version wirst du Googeln müssen.
# Wenn du feststeckst, schaue dir den Hinweis unten an.

# 💡 Hinweis 2

# Versuche zu googeln:

# „How to shuffle items in a list in Python“

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
password_liste = []

# Schritt 3 - Buchstaben random in Liste einfügen
for letter in range(1, nr_letters + 1):
    password_liste.append(random.choice(letters))


# Schritt 4 - Zahlen random
for num in range(1, nr_numbers + 1):
    password_liste.append(random.choice(numbers))

# Schritt 5 - Symbole random
for symbol in range(1, nr_symbols + 1):
    password_liste.append(random.choice(symbols))

# Schritt 6 - Mixe die Zeichen
print(password_liste)                               # Liste vor dem Mix
neues_password = random.shuffle(password_liste)     # Passwort Liste shuffeln
print(password_liste)                               # neue Passwort Liste

# Schritt 6 - Passwort Liste wieder zu String
passwort = " "

for char in password_liste:
    passwort += char

# Schritt 7 - Passwort ausgeben
print(passwort)