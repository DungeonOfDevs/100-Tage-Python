# If Else (Wenn–Sonst)

# Bedingungsprüfung (Condition Check)

# Lerne, wie man Bedingungen in Python verwendet, um eine Bedingung zu 
# überprüfen und dem Computer zu sagen, was er in jedem Fall tun soll, z. B.:

# if <diese Bedingung ist wahr>:
#     <dann führe diese Codezeile aus>

# Was passiert, wenn die Bedingung falsch ist?

# Das Schlüsselwort else wird verwendet, um einen Codeblock zu definieren, 
# der ausgeführt wird, wenn die im if-Statement geprüfte Bedingung falsch ist.

# Beispiel:
# if pigs can fly:
#     <Code, der niemals ausgeführt wird>
# else:
#     print("Das ist das echte Leben")


# Python-Einrückung (Indentation)

# Verstehe die Wichtigkeit der Einrückung in Python, denn sie bestimmt, welche Codezeilen zu anderen Codezeilen gehören.

# Beispiel:

if 5 > 2:   # Dies ist die übergeordnete (parent) Codezeile
    print("yes")   # Dies ist eine untergeordnete (child) Codezeile

# Die eingerückte Zeile gehört zum if-Block und wird nur ausgeführt, wenn die Bedingung wahr ist.


# Alltagsbeispiel für if/else Anweisung
wasserstand = int(input("Wie hoch ist das Wasser in der Badewanne (in cm)?\n"))

if wasserstand > 80:
    print("Wasser bitte ablassen!")
else: 
    print("Wanne weiter mit Wasser füllen.")