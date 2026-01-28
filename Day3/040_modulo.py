# Modulo

# Der Modulo-Operator gibt dir den Rest einer Division zurück.

print(6 % 2)   # ergibt 0
print(6 % 5)   # ergibt 1
print(6 % 4)  # ergibt 2

########################################################################################

# Aufgabe 1 – Was ist 10 % 3?

# Was glaubst du, wird ausgegeben?

print(10 % 3)

########################################################################################

# Aufgabe 2 – Gerade oder ungerade prüfen

# Schreibe etwas Code mit dem, was du über den Modulo-Operator und bedingte Anweisungen 
# (if / else) in Python gelernt hast, um zu überprüfen, 
# ob die Zahl im Eingabefeld gerade oder ungerade ist.

# Wenn sie ungerade ist → gib „Odd“ aus

# Andernfalls → gib „Even“ aus

num = int(input("Wähle eine Zahl zwischen 0 - 100 aus!\n"))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")