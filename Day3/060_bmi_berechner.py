# BMI-Rechner mit Interpretation

# Füge dem BMI-Rechner einige if/elif/else-Anweisungen hinzu, damit er die berechneten BMI-Werte interpretiert.

# 1. Wenn der BMI unter 18,5 liegt (nicht eingeschlossen), gib „Untergewicht“ aus.

# 2. Wenn der BMI zwischen 18,5 (einschließlich) und 25 (nicht eingeschlossen) liegt, gib „Normalgewicht“ aus.

# 3. Wenn der BMI 25 (einschließlich) oder höher ist, gib „Übergewicht“ aus.

weight = 85
height = 1.85

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("Untergewicht")
elif bmi < 25:
    print("Normalgewicht")
else:
    print("Übergewicht")
