# 3. Zuweisungsoperatoren

# Zuweisungsoperatoren wie der Additions-Zuweisungsoperator +=
# addieren die Zahl rechts zum ursprünglichen Wert der Variablen links
# und speichern das neue Ergebnis wieder in der Variable.

# +=
# -=
# *=
# /=

score = 0

# User macht einen Punkt
score += 1
print(score)


# 4. f-Strings

# In Python können wir f-Strings verwenden, um eine Variable oder einen Ausdruck in eine Zeichenkette einzufügen.

# age = 12
# print(f"I am {age} years old")

# Ausgabe:
# I am 12 years old

print(f"Dein Punktestand ist: {score}!")

#####################################################################

score = 0
height = 1.8
is_winning = True

print(f"Score: {score}, Height: {height}, Winning: {is_winning}")
