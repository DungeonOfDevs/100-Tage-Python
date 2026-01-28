# Python Pizza

# Herzlichen Glückwunsch, du hast einen Job bei Python Pizza bekommen!
# Deine erste Aufgabe ist es, ein automatisches Pizza-Bestellprogramm zu erstellen.

# Basierend auf der Bestellung eines Nutzers sollst du die Endrechnung berechnen.
# Verwende die Funktion input(), um die Wünsche des Nutzers abzufragen, 
# ddiere anschließend die Gesamtkosten und teile ihm mit, wie viel er bezahlen muss.

# Preise
# Kleine Pizza (S): 15 $
# Mittlere Pizza (M): 20 $
# Große Pizza (L): 25 $

# Extras
# Peperoni für kleine Pizza (Y oder N): +2 $
# Peperoni für mittlere oder große Pizza (Y oder N): +3 $
# Extra Käse für jede Pizzagröße (Y oder N): +1 $

# Beispiel-Interaktion
# Willkommen bei Python Pizza Lieferservice!

# Welche Pizzagröße möchtest du? S, M oder L: L
# Möchtest du Peperoni auf deiner Pizza? Y oder N: Y
# Möchtest du extra Käse? Y oder N: N
# Deine Endrechnung beträgt 28 $.

########################################################################################

print("Willkommen bei Python Pizza Lieferservice!")
size = input("Welche Pizzagröße möchtest du? S, M oder L: ")
pepperoni = input("Möchtest du Peperoni auf deiner Pizza? Y oder N: ")
extra_cheese = input("Möchtest du extra Käse? Y oder N: ")
bill = 0


if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if pepperoni == "Y":
    if pepperoni =="S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Deine Rechnung Beträgt {bill}€.")