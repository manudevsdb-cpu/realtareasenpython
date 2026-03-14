import random

numero = random.randint(1, 10)

while True:
    intento = int(input("Adivina el número (1-10): "))
    
    if intento == numero:
        print("¡Correcto!")
        break
    else:
        print("Intenta otra vez")