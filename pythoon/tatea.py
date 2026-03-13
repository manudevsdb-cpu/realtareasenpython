
while True:
    nombre = input("¿Cuál es su nombre? ").strip()
    if nombre:
        break
    print("No puedes dejar vacío tu nombre.")

while True:
    try:
        edad = int(input("¿Cuál es tu edad? "))
        if edad > 0:
            break
        else:
            print("La edad debe ser mayor que 0.")
    except ValueError:
        print("Debes escribir un número válido.")

print("Tu nombre es:", nombre)
print("Tu edad es:", edad)