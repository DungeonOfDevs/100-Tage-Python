# Mehrere if-Anweisungen


# Du kannst so viele if-Anweisungen schreiben, wie du brauchst, um verschiedene 
# Bedingungen zu überprüfen, die nichts miteinander zu tun haben. Vergleiche die folgenden Codeblöcke:


# if / elif / else
# if <Bedingung 1 ist wahr>:
#     <mache A>
# elif <Bedingung 2 ist wahr>:
#     <mache B>
# else:
#     <mache C>


# Verschachtelte if-Anweisungen (nested if)
# if <Bedingung 1 ist wahr>:
#     <mache A>
#     if <Bedingung 2 ist wahr>:
#         <mache B>
#         if <Bedingung 3 ist wahr>:
#             <mache C>


# Mehrere einzelne if-Anweisungen
# if <Bedingung 1 ist wahr>:
#     <mache A>

# if <Bedingung 2 ist wahr>:
#     <mache B>

# if <Bedingung 3 ist wahr>:
#     <mache C>


# Erklärung:

# Beim if / elif / else-Block kann nur eines von A, B oder C ausgeführt werden,
# da sich diese Bedingungen gegenseitig ausschließen.
# Bedingung 2 wird nur geprüft, wenn Bedingung 1 falsch ist.
# Und die else-Anweisung wird nur erreicht, wenn alle vorherigen Bedingungen falsch sind.

# Bei den verschachtelten if-Anweisungen können A, B und C alle ausgeführt werden,
# aber nur, wenn Bedingung 1, 2 und 3 alle wahr sind.
# Bedingung 2 wird nur geprüft, wenn Bedingung 1 wahr ist.

# Bei mehreren einzelnen if-Anweisungen können A, B und C alle ausgeführt werden,
# unabhängig voneinander.
# C kann auch passieren, selbst wenn A und B nicht ausgeführt wurden.
# Jede Bedingung wird geprüft, egal wie die anderen ausgegangen sind.


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
    else:
        bill += 12
        print("Erwachsene Tickets kosten 12€.")
        
    wants_photo = input("Möchtest du ein Foto? J oder N? ")
    if wants_photo == "J":
        bill += 3
        
    print(f"Deine Rechnung ist {bill}€.")
else:
    print("Tut mir leid, du musst noch etwas wachsen, bevor du mitfahren darfst.")