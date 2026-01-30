# Stein Papier Schere

# Du wirst ein Stein-Papier-Schere-Spiel programmieren.
# Dafür musst du anwenden, was du bisher über Randomisierung und Listen gelernt hast.

# Demo: https://appbrewery.github.io/python-day4-demo/

import random

rock = '''
    _______
---'   ____)
        (_____)
        (_____)
        (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
            ______)
            _______)
            _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
            ______)
        __________)
        (____)
---.__(___)
'''

game_image = [scissors, rock, paper]

spieler_name = input("Wie heißt du?\n")
print (f"Willkommen {spieler_name} bei Schere, Stein Papier.")
spieler1 = int(input("Bitte wähle 0 für Schere, 1 für Stein und 2 für Papier!\n"))
if spieler1 >= 0 and spieler1 <=2:
    print(game_image[spieler1])
    
computer = random.randint(0,2)
print("Der Computer wählte: ")
print(game_image[computer])

spieler_ausgabe = " "
computer_ausgabe = " "

if spieler1 == 0:
    spieler_ausgabe = "Schere"
elif spieler1 == 1:
    spieler_ausgabe = "Steine"
else:
    spieler_ausgabe = "Papier"

if computer == 0:
    computer_ausgabe = "Schere"
elif computer == 1:
    computer_ausgabe = "Stein"
else:
    computer_ausgabe = "Papier"


if (computer == 0 and spieler1 == 0) or (computer == 1 and spieler1 == 1) or (computer == 2 and spieler1 == 2):
    print(f"Der Computer hat {computer_ausgabe} gewählt und du hast {spieler_ausgabe} gewählt. Das heißt unentschieden.")
elif (computer == 0 and spieler1 == 1) or (computer == 1 and spieler1 == 2) or (computer == 2 and spieler1 == 0):
    print(f"Der Computer hat {computer_ausgabe} gewählt und du hast {spieler_ausgabe} gewählt. Das heißt du hast gewonnen, da {spieler_ausgabe} gewinnt gegen {computer_ausgabe}.")
elif (computer == 0 and spieler1 == 2) or (computer == 1 and spieler1 == 0) or (computer == 2 and spieler1 == 1):
    print(f"Der Computer hat {computer_ausgabe} gewählt und du hast {spieler_ausgabe} gewählt. Das heißt der Computer hat gewonnen, da {computer_ausgabe} gewinnt gegen {spieler_ausgabe}.")
else:
    print("Da ist etwas schief gelaufen. Versuche es nocheinmal.")