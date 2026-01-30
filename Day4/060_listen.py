# Listen

# Du kannst eine einfache Sammlung geordneter Elemente mit einer Python-Liste erstellen, z. B.:

fruits = ["Cherry", "Apple", "Pear"]
print(fruits)

# oder

states_of_america = [
    "Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut",
    "Massachusetts", "Maryland", "South Carolina", "New Hampshire",
    "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont",
    "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi",
    "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan",
    "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota",
    "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
    "North Dakota", "South Dakota", "Montana", "Washington", "Idaho",
    "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska",
    "Hawaii"
]

# Auf Elemente in Listen zugreifen

# Du kannst zuerst den Namen der Liste angeben und dann in eckigen Klammern den Index des gewünschten Elements, z. B.:

print(states_of_america[0])

# Das gibt "Delaware" zurück.

# Denke daran: In der Programmierung beginnt das Zählen immer bei 0
# und nicht bei 1.
# Also: 0, 1, 2, 3 statt 1, 2, 3, 4.

# Negative Indizes

# Du kannst auf Elemente einer Liste auch vom Ende her zugreifen, indem du negative ganze Zahlen verwendest, z. B.:

fruits = ["Cherry", "Apple", "Pear"]
print(fruits[-1])   # das wird "Pear" sein

states_of_america = [
    "Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut",
    "Massachusetts", "Maryland", "South Carolina", "New Hampshire",
    "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont",
    "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi",
    "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan",
    "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota",
    "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
    "North Dakota", "South Dakota", "Montana", "Washington", "Idaho",
    "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska",
    "Hawaii"
]
print(states_of_america[-1])
print(states_of_america[-7])

# Elemente verändern

# Du kannst dieselbe Schreibweise verwenden, um Elemente in einer Liste zu verändern, z. B.:

fruits = ["Cherry", "Apple", "Pear"]
fruits[0] = "Orange"
print(fruits)
# fruits wird nun ["Orange", "Apple", "Pear"]




# Elemente hinzufügen

# Du kannst Elemente am Ende einer Liste mit der Funktion append() hinzufügen, z. B.:

fruits = ["Cherry", "Apple", "Pear"]
fruits.append("Orange")
print(fruits)

# fruits wird nun ["Cherry", "Apple", "Pear", "Orange"]

states_of_america = [
    "Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut",
    "Massachusetts", "Maryland", "South Carolina", "New Hampshire",
    "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont",
    "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi",
    "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan",
    "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota",
    "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
    "North Dakota", "South Dakota", "Montana", "Washington", "Idaho",
    "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska",
    "Hawaii"
]
states_of_america.extend(["Angalaland", "Nerdcountry"])
print(states_of_america)


# Listen-Dokumentation

# Die Dokumentation zu Python-Listen und weiteren listenbezogenen Funktionen findest du hier:
# https://docs.python.org/3/tutorial/datastructures.html

#################################################################################################

# Unterschied extend() und append()

# Mit .extend() Listen zusammenführen:

# Auf der anderen Seite haben wir die Methode .extend(), die dazu dient, eine Iterable 
# (wie eine Liste, ein Set oder ein Tupel) zu nehmen und jedes ihrer Elemente an das 
# Ende der Liste anzuhängen. Der Hauptunterschied besteht darin, dass .extend() die 
# Iterable entpackt und ihre Komponenten als einzelne Elemente hinzufügt, wodurch die 
# Liste erweitert wird, ohne verschachtelte Strukturen zu erzeugen.

# Beispiel
# Betrachten wir die gleiche Ausgangsliste x = [1, 2, 3]. 
# Diesmal wollen wir die Elemente einer anderen Liste [4, 5] in x aufnehmen und dabei 
# eine flache Struktur beibehalten. Hier ist, wie .extend() das erreicht:

# Python Code
x = [1, 2, 3]
x.extend([4, 5])
print(x)

# # Das Ergebnis ist eine nahtlos erweiterte Liste:
# [1, 2, 3, 4, 5]


# Die Methode .append(): Einzelnes Hinzufügen von Elementen

# Die Methode .append() hat einen ganz einfachen Zweck: Sie fügt ein einzelnes Objekt 
# an das Ende einer Liste an, unabhängig vom Typ des Objekts. Damit ist diese Methode 
# vor allem dann interessant, wenn wir ein Objekt an eine Liste anhängen wollen, wobei 
# die Objektintegrität erhalten bleiben soll. Das bedeutet, dass, wenn das Objekt 
# selbst eine Liste ist, .append() diese verschachtelte Liste als ein einzelnes, 
# eindeutiges Element am Ende der Liste anfügt.

# Beispiel
# Betrachten wir ein Szenario, in dem wir eine ursprüngliche Liste x = [1, 2, 3] 
# haben und eine weitere Liste [4] hinzufügen möchten. Mit .append() 
# erreichen wir das Folgende:

# Python Code
x = [1, 2, 3]
x.append(4)
print(x)

# Die Ausgabe dieser Operation wäre:
# [1, 2, 3, 4]

# Zusammenfassung -> append() ein Element | extend() ganze Listen
