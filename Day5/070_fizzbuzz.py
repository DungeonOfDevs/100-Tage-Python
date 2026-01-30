# FizzBuzz

# Du wirst ein Programm schreiben, das automatisch die Lösung des FizzBuzz-Spiels ausgibt.
# Das sind die Regeln des FizzBuzz-Spiels:

# 1. Dein Programm soll jede Zahl von 1 bis 100 nacheinander ausgeben — einschließlich der 100.
# 2. Wenn die Zahl durch 3 teilbar ist, soll statt der Zahl „Fizz“ ausgegeben werden.
# 3. Wenn die Zahl durch 5 teilbar ist, soll statt der Zahl „Buzz“ ausgegeben werden.
# 4. Wenn die Zahl durch 3 und 5 teilbar ist (z. B. 15), soll statt der Zahl „FizzBuzz“ ausgegeben werden.

# Beispielausgabe:
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
# ...

for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)