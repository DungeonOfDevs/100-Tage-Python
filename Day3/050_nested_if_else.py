# Nesting und Elif

# Du kannst if/else-Anweisungen innerhalb anderer if/else-Anweisungen verwenden. Das nennt man Nesting (Verschachtelung). Zum Beispiel:

# if maths_score >= 90:
#     if english_score >= 90:
#         print("Du bist in allem gut")
#     else:
#         print("Du bist gut in Mathe")

# if english_score >= 90:
#     print("Du bist gut in Englisch")


# In diesem Fall bekommt ein Schüler nur dann die Ausgabe
# „Du bist in allem gut“, wenn er über 90 Punkte in Mathe und Englisch hat.

# Hinweis:
# Du kannst auch if-Anweisungen verwenden, die kein zugehöriges else haben.

# Nested
print("Willkommen in der Achterbahn!")
height = int(input("Wie groß bist du in cm? "))

if height >= 120:
    print("Du darfst Achterbahn fahren")
    age = int(input("Wie alt bist du? "))
    if age <= 18:
        print("Das sind bitte 7€.")
    else:
        print("Das sind bitte 12€.")
else:
    print("Tut mir leid, du musst noch etwas wachsen, bevor du mitfahren darfst.")


# Elif
print("Willkommen in der Achterbahn!")
height = int(input("Wie groß bist du in cm? "))

if height >= 120:
    print("Du darfst Achterbahn fahren")
    age = int(input("Wie alt bist du? "))
    if age < 12:
        print("Das sind bitte 5€.")
    elif age <= 18: 
        print("Das sind bitte 7€.")
    else:
        print("Das sind bitte 12€.")
else:
    print("Tut mir leid, du musst noch etwas wachsen, bevor du mitfahren darfst.")