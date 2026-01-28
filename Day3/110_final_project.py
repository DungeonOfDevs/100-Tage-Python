# Treasure Island Projekt

# (Schatzinsel-Projekt)

# Dein Ziel heute ist es, ein „Wähle-dein-eigenes-Abenteuer-Spiel“ zu bauen.
# Mit dem, was du heute in den Lektionen gelernt hast, 
# wirst du eine sehr einfache Version dieses textbasierten Spiels erstellen.

# Verwende das hier verlinkte Flussdiagramm, um die Spiellogik zu entwickeln.
# Sobald du das Projekt abgeschlossen hast, kannst du das Spiel jederzeit erweitern und interessanter gestalten!

# Treasure Hunt: Monster-Insel (Textadventure)
# Tipp: Eingaben sind nicht case-sensitive (wir nutzen .lower().strip()).

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************''')

print("🏝️ TREASURE HUNT: Monster-Insel")
print("Finde den Schatz! Aber überlebe 5 Etappen...\n")

# ETAPPE 1
choice1 = input("Etappe 1: Wohin gehst du? (dschungel/strand/ruinen) ").lower()
if choice1 == "dschungel":
    print("Du hörst Dino-Schritte... 😬")
elif choice1 == "strand":
    print("Das Meer gluckert... etwas ist da drin... 🌊")
elif choice1 == "ruinen":
    print("Die Ruinen flüstern... 🏛️")
else:
    print("Falsche Eingabe -> Du verlierst dich. GAME OVER.")
    quit()

# ETAPPE 2
choice2 = input("\nEtappe 2: Ein Monster taucht auf! Was tust du? (rennen/verstecken/kaempfen) ").lower()
if choice2 == "rennen":
    print("Du entkommst knapp!")
elif choice2 == "verstecken":
    print("Puh... es zieht vorbei.")
elif choice2 == "kaempfen":
    print("Du gewinnst... aber nur mit Glück.")
else:
    print("Falsche Eingabe. GAME OVER.")
    quit()

# ETAPPE 3
choice3 = input("\nEtappe 3: Ein Fluss mit Seemonster! (bruecke/schwimmen/floß) ").lower()
if choice3 == "bruecke":
    print("Die Brücke wackelt, hält aber!")
elif choice3 == "floß":
    print("Das Floß schwimmt! Das Monster schnappt daneben.")
elif choice3 == "schwimmen":
    print("Das Seemonster zieht dich runter. GAME OVER.")
    quit()
else:
    print("Falsche Eingabe. GAME OVER.")
    quit()

# ETAPPE 4
choice4 = input("\nEtappe 4: Ein Drache blockiert den Weg! (leise/vorsicht/angreifen) ").lower()
if choice4 == "leise":
    print("Du schleichst vorbei. Der Drache schnarcht.")
elif choice4 == "vorsicht":
    print("Du wirfst ein glänzendes Ding. Der Drache ist abgelenkt.")
elif choice4 == "angreifen":
    print("Der Drache ist beleidigt. GAME OVER.")
    quit()
else:
    print("Falsche Eingabe. GAME OVER.")
    quit()

# ETAPPE 5
print("\nEtappe 5: Drei Truhen stehen vor dir: gold, stein, koralle")
choice5 = input("Welche öffnest du? (gold/stein/koralle) ").lower()

if choice5 == "stein":
    print("\n🏆 GEWONNEN! In der Steintruhe liegt der Schatz! 💎")
elif choice5 == "gold":
    print("\n💀 Falle! Feuerstrahl. GAME OVER.")
elif choice5 == "koralle":
    print("\n💀 Falle! Seemonster-Sprungfalle. GAME OVER.")
else:
    print("\nFalsche Eingabe. GAME OVER.")
