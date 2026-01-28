# Praxisbeispiel: Achterbahn im Freizeitpark

# Regel:    Nur Personen ab 120 cm dürfen fahren

# Ablauf:
# 1. Nutzer gibt seine Körpergröße ein
# 2. Programm prüft die Größe
# 3. Je nach Ergebnis wird eine andere Nachricht ausgegeben

print("Willkommen bei der Achterbahn!")
height = int(input("Wie groß bist du in cm? "))

if height > 120:                            # 120cm ist auch zu klein
    print("Du darfst Achterbahn fahren!")
else:
    print("Du bist leider zu klein!")


# Verbesserter Code
if height >= 120:
    print("Du darfst Achterbahn fahren!")
else:
    print("Du bist leider zu klein!")