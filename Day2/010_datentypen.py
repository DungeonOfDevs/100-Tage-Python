# Primitive Datentypen

# ... in Programmiersprache eingebaute Datentypen!

# In der Programmierung ist der Datentyp ein wichtiges Konzept.
# Variablen können Daten unterschiedlicher Typen speichern, 
# und verschiedene Typen können unterschiedliche Dinge tun.
# Python besitzt standardmäßig die folgenden eingebauten Datentypen, 
# eingeteilt in diese Kategorien:

# Texttyp:                  str

# Numerische Typen:         int, float, complex

# Sequenztypen:             list, tuple, range

# Zuordnungstyp (Mapping):  dict

# Mengen-Typen:             set, frozenset

# Boolescher Typ:           bool

# Binäre Typen:             bytes, bytearray, memoryview

# None-Typ:                 NoneType


# 1. Indizierung
gruess = "Hallo"[0]
print(gruess)

print("Victor"[1])

# 2. String (str)
print("123" + "456")
print("Hallo mein Name ist Vic.")

# 3. Integer (int) = ganze Zahlen ohne Dezimalstellen
print(123 + 456)

# 4. Große Integer
print(123_456_789)  # _ wird Ignoriert beim auslesen

# 5. Float (float) = Kommazahl
print(3141.59)      # statt Komma schreibt man einen Punkt -> so wie im eng.

# 6. Boolean (bool) = Wahrheitswert (Wahr oder Falsch)
print(True)
print(False)