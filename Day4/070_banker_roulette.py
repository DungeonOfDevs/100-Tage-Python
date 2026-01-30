# Banker Roulette

# Finde heraus, wie man zufällig einen Namen aus der Liste friends auswählt.
import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# Option 1
zufall = random.randint(0,4)
print(friends[zufall])

# Option 2
print(random.choice(friends))