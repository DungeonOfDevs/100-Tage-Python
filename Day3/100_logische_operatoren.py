# Logische Operatoren
# Beschreibung

# Du kannst verschiedene Bedingungen mithilfe logischer Operatoren kombinieren.

# A and B   → Beide Bedingungen müssen wahr sein
# C or D    → Nur eine der Bedingungen muss wahr sein
# not E     → Die Bedingung muss falsch sein

# Aufgabe 1 – Altersbereich 45 bis 55

# Aktualisiere den Code so, dass Personen im Alter von 45 bis 55 Jahren 
# (beide Altersangaben eingeschlossen) kostenlos fahren dürfen.

# Verwende logische Operatoren, um zu prüfen, dass:
# - das Alter größer oder gleich 45 ist
# - und kleiner oder gleich 55

# Hinweis: 

# Die Warnung zur Vereinfachung ist nur ein Vorschlag.
# Du kannst ihn berücksichtigen und anwenden – oder auch ignorieren.

print("Willkommen in der Achterbahn!")
height = int(input("Wie groß bist du in cm? "))
bill = 0

if height >= 120:
    print("Du darfst Achterbahn fahren")
    age = int(input("Wie alt bist du? "))
    if age < 12:
        bill += 5
        print("Kindertickets kosten 5€.")
    elif age <= 18: 
        bill += 7
        print("Jugendliche Tickets kosten 7€.")
    elif age >= 45 and age <= 55:
        print("Alles okay. Du darfst heute kostenlos mitfahren.")
    else:
        bill += 12
        print("Erwachsene Tickets kosten 12€.")
        
    wants_photo = input("Möchtest du ein Foto? J oder N? ")
    if wants_photo == "J":
        bill += 3
        
    print(f"Deine Rechnung ist {bill}€.")
    
else:
    print("Tut mir leid, du musst noch etwas wachsen, bevor du mitfahren darfst.")