# Vergleichsoperatoren (Comparator Operators)

# Diese Operatoren werden für Bedingungen benutzt:

# > größer als
# < kleiner als
# >= größer als oder gleich
# <= kleiner als oder gleich
# == gleich
# != ungleich / nicht gleich

# Wichtig:

# = → weist einen Wert zu
# == → vergleicht zwei Werte

# Das ist ein sehr häufiger Anfängerfehler.

#######################################################################

print("Willkommen bei der Achterbahn!")
height = int(input("Wie groß bist du in cm? "))

if height >= 120:
    print("Du darfst Achterbahn fahren!")
else:
    print("Du bist leider zu klein!")

#######################################################################

age = 20
height = 120
lives = 0
password = "katze123"
answer = "ja"

# > größer als
if age > 18:
    print("age > 18 → Du bist älter als 18.")

# < kleiner als
if age < 30:
    print("age < 30 → Du bist jünger als 30.")

# >= größer oder gleich
if height >= 120:
    print("height >= 120 → Du darfst Achterbahn fahren.")

# <= kleiner oder gleich
if lives <= 0:
    print("lives <= 0 → Game Over.")

# == gleich
if password == "katze123":
    print("password == katze123 → Passwort korrekt.")

# != nicht gleich
if answer != "nein":
    print("answer != nein → Wir machen weiter.")
