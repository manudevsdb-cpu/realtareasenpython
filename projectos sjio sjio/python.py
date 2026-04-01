import random

numero = random.randint(1, 10)

num = int(input("Adivina el número 1-10 solo esos  "))

while num != numero:
    print("Otro intento")
    num = int(input("Adivina el número: "))

print("¡Adivinaste!")
