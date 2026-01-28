# Schaltjahr

# Schreibe ein Programm, das herausfindet, ob ein gegebenes Jahr ein normales Jahr oder ein Schaltjahr ist.
# Ein normales Jahr hat 365 Tage, Schaltjahre haben 366, mit einem zusätzlichen Tag im Februar.

# Der Grund, warum wir Schaltjahre haben, ist wirklich faszinierend – dieses Video erklärt es noch besser.

# So findest du heraus, ob ein bestimmtes Jahr ein Schaltjahr ist:

# - in jedem Jahr, das ohne Rest durch 4 teilbar ist

# - außer in jedem Jahr, das ohne Rest durch 100 teilbar ist

# - es sei denn, das Jahr ist auch ohne Rest durch 400 teilbar.

year = int(input("Welches Jahr möchtest du überprüfen? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Das ist ein Schaltjahr")
        else:
            print("Das ist kein Schaltjahr")
    else:
        print("Das ist ein Schaltjahr")
else:
    print("Das ist kein Schaltjahr")