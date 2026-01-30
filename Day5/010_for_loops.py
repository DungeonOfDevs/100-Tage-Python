# For-Loops

# (For-Schleifen)

# Beschreibung

# Schleifen ermöglichen es uns, dem Computer zu sagen, dass er Aktionen wiederholen soll, ohne dass wir denselben Code immer wieder neu schreiben müssen.

# Wenn wir zum Beispiel möchten, dass der Computer die Zahlen von 1 bis 100 ausgibt, wäre es sehr mühsam, für jede Zahl eine eigene print-Anweisung zu schreiben – oder sogar alle Zahlen einzeln einzugeben.

# Schleifen erlauben es uns, eine Regel festzulegen, der der Computer folgt, um eine Aktion mehrfach auszuführen.

# Syntax
# for <Variablenname für jedes Element> in <einer Liste>:
#     <etwas tun>
#     <noch etwas tun>

fruits = ["Apple", "Peach", "Pear", "Cherry", "Pineapple", "Coconut"]

for fruit in fruits:
    print(fruit)
    print(fruit + " pie")



# Aufgabe 1 – Sei ein Computer:

# Überlege, was durch folgenden Code ausgegeben wird:

# fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)
    print(fruit + " pie")


# Einrückung (Indentation)

# Einrückung ist in Python sehr wichtig.

# Jedes Mal, wenn du das Symbol : siehst, musst du darauf achten, wie der Code danach eingerückt ist.
# Zum Beispiel verhält sich dieser Code sehr anders:

fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)
    print("Hello")

# im Vergleich zu diesem Code:

fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)    # ein Item der Liste
    print(fruits)   # alle Inhalte

print("Hello")