# Variablen Benennen

#1. Variablen sollten lesbar sein:

#   - Kurze Namen wie n oder l funktionieren technisch,
#   - sind aber schlecht verständlich.

# Verwende aussagekräftige Namen wie:

username = "Wintersturm"
name_length = 12

##############################################################################

# 2. Mehrere Wörter → Unterstrich verwenden

# ❌ Nicht erlaubt: user name

# ✅ Richtig:

user_name = "Storm"     # Variablennamen müssen eine Einheit sein.

##############################################################################

# 3. Zahlen sind erlaubt – aber nicht am Anfang

# ✅ Erlaubt:

length1 = 15
user2 = "Huehnerhose"

# ❌ Nicht erlaubt:  1length    |   3name

##############################################################################

# 4. Keine reservierten Wörter benutzen

#   - Funktionsnamen wie print oder input nicht als Variablen verwenden
#   - Das ist schlechte Praxis und sehr verwirrend

##############################################################################

# 5. Python achtet streng auf die Schreibweise

# name ≠ Name ≠ nama

#   - Ein Tippfehler führt zu einem NameError

# Beispiel: print(nama)
# → Fehler, weil nama nicht definiert wurde.

# Variablennamen sind groß- und kleinschreibungssensitiv
# (age, Age und AGE sind drei verschiedene Variablen)

##############################################################################

# 6. Python prüft keine Rechtschreibung

#   - Python interessiert sich nicht, ob ein Wort „richtig“ geschrieben ist

# Wichtig ist nur:
# --> Der Name muss überall exakt gleich geschrieben sein

##############################################################################

# 7. Muss mit Buchstaben oder Unterstrich (_) beginnen

test = " Das ist ein Test"
_hund = "Das ist die Variable Hund"
