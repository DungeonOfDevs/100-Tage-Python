# Variablen

# Beschreibung

# Lerne, wie man Werte in Behältern für die spätere Verwendung speichert.
# Variablen sind ein Konzept in der Programmierung, das es uns erlaubt, einem Datenstück einen Namen (Label) zu geben, 
# sodass wir mithilfe des gewählten Variablennamens auf diese Daten verweisen können.

# In dieser Lektion sehen wir, wie man Variablen erstellt und wie man sie verwendet, um auf den gespeicherten Wert zuzugreifen.

#################################################################################################################################

# input("Wie ist dein Name?") -> speichert Namen nicht

# Name speichern durch Variable
name = "Jack"
print(name)

# name = Variablenname
# "Jack" = Zugeordneter Wert

# Name wird in Variable gespeichert und ist Benutzerabhängig
name = input("Wie heißt du?")
print("Hallo " + name)

##################################################################################################################################

# Variablen können sich ändern
zahl = 1
print(zahl)

zahl = 5            # Überschreibt zahl = 1
print(zahl)

zahl = 7            # Überschreibt zahl = 5
print(zahl + 9)     # Aktueller Wert der Variablen zahl = 7 wird genommen

##################################################################################################################################


