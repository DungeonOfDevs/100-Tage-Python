# Typumwandlung (Type Conversion)

# Du kannst Daten mit speziellen Funktionen in andere Datentypen umwandeln, zum Beispiel:

# float()
# int()
# str()

# Korregiere die Zeile Code das sie ohne Probleme läuft
# print("Number of letters in your name: " + len(input("Enter your name")))

name_benutzer = input("Gib bitte deinen Namen ein \n")
leange_des_namen = len(name_benutzer)

# print(type("Anzahl der Buchstaben in deinem Namen: "))    
# print(type(leange_des_namen))

print("Anzahl der Buchstaben in deinem Namen: " + str(leange_des_namen))
