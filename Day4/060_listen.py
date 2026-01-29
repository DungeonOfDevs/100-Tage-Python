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

# Listen-Dokumentation

# Die Dokumentation zu Python-Listen und weiteren listenbezogenen Funktionen findest du hier:
# https://docs.python.org/3/tutorial/datastructures.html