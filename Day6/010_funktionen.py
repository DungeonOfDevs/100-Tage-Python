# Funktionen

# Eine Funktion ist in ihrer einfachsten Form nur ein Sammelname für einen Codeblock.
# Du gibst ihr einen Namen, und wenn du die Funktion mit diesem Namen aufrufst, 
# wird der gesamte Code innerhalb der Funktion ausgeführt.

# Funktionen helfen uns, Zeit zu sparen und wiederholten Code zu vermeiden.

# Eine neue Funktion definieren
# def <funktionsname>():
#     print("Hallo")
#     # Mache etwas anderes
#     # Mache noch etwas anderes ...

# Eine Funktion aufrufen

# Eine Funktion aufzurufen bedeutet einfach, sie auszulösen.
# Wir können eine Funktion an jeder Stelle unseres Python-Codes aufrufen.

# <funktionsname>()

# Alles zusammengefügt – Beispiel
# Erstellen der Funktion
def get_user_name():
    name = input("Wie heißt du? ")
    print("Hallo, " + name)
    # Innerhalb der Funktion

# Außerhalb der Funktion
print("Hallo")
get_user_name()  # Aufruf der Funktion


# Dieser Code führt zu folgender Ausgabereihenfolge:
# Hallo
# Wie heißt du?  # Ich tippe Angela
# Hallo
# Angela

##############################################################################

def my_function():
    name = input("Wie heißt du?\n")
    alter = int(input("Wie alte bist du?\n"))
    print(f"Dein Name ist {name} und du bist {str(alter)} Jahre alt.")

my_function()