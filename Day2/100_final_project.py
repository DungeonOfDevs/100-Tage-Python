# Trinkgeldrechner-Projekt
# Beschreibung

# Wir werden einen Trinkgeldrechner bauen.

# Wenn die Rechnung 150,00 $ beträgt, auf 5 Personen aufgeteilt wird und 12 % Trinkgeld gegeben werden:

# Jede Person sollte zahlen:    (150.00 / 5) * 1.12 = 33.6

# Nach dem Formatieren auf 2 Dezimalstellen = 33.60

# Demo
# https://appbrewery.github.io/python-day2-demo/

# Sehr optionale Lektüre: Fließkommaarithmetik
# https://docs.python.org/3/tutorial/floatingpoint.html


print("Willkommen beim Trinkgeldrechner!")
bill = float(input("Wie hoch war die Gesamtrechnung? €"))
tip = int(input("Wie viel Prozent Trinkgeld möchtest du geben? 10 12 15 "))
people = int(input("Auf wie viele Personen soll die Rechnung aufgeteilt werden? "))

tip_prozent = tip / 100
total_with_tip = bill * (1 + tip_prozent)
final_bill = total_with_tip / people

final_bill = round(final_bill, 2)

print(
    f"Bei einer Rechnung von {bill}€, die durch {people} Personen geteilt wird, "
    f"muss jede Person {final_bill}€ bezahlen, wenn {tip}% Trinkgeld gegeben wird."
)