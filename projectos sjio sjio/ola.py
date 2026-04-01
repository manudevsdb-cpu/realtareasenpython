import random
a = random.randint(1, 10)
b = int(input("Adivina el número "))
while b != a:
    print("ño es, inténtalo otra vez")
    b = int(input("Adivina el número: "))
print("¡Adivinaste!")