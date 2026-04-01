import random

opciones = ["piedra", "papel", "tijera"]

usuario = input("escoje  piedra, papel o tijera: ")
a = random.choice(opciones)
# un juegito q no savia ke aser lo hice con trandom jajajajajjaajajajaj
print("La computadora eligió:", a)
if a == "piedra" and usuario == "papel":
    print("¡Me has ganado! Tenía piedra")
elif a == "papel" and usuario == "piedra":
    print("Te gané, tenía papel")
elif a == "tijera" and usuario == "papel":
    print("Te gané, tenía tijera")
elif a == "papel" and usuario == "tijera":
    print("me ganaste tenia papel")
elif a == "piedra" and usuario == "tijera":
    print("te gane tenia piedra ")
elif a == "tijera" and usuario == "piedra":
    print("me ganaste tenia tijera ")

        