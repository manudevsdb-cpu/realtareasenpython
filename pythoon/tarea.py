while True:
    nombre = input("¿Cuál es tu nombre? ")

    if nombre == "":
        print("No puedes dejar vacío tu nombre")
    else:
        print("Tu nombre es", nombre, "¿verdad?")
        break
while True:
    edad_texto = input("¿Cuál es tu edad? ")

    if edad_texto == "":
        print("No puedes dejar vacía tu edad")
    elif not edad_texto.isdigit():
        print("La edad debe ser un número")
else:
        edad = int(edad_texto)
        print("Tu nombre es", nombre, "y tu edad es", edad)
        break
while True:
    num1_texto = input("Digita el 1er número: ")

    if num1_texto == "":
        print("No dejes vacío el número")
    else:
        try:
            num1 = float(num1_texto)
            break
        except:
            print("Debes escribir un número válido")
while True:
    num2_texto = input("Digita el 2do número: ")

    if num2_texto == "":
        print("No dejes vacío el número")
    else:
        try:
            num2 = float(num2_texto)
            break
        except:
            print("Debes escribir un número válido")
if num2 == 0:
    print("No se puede dividir entre 0")
else:
    suma = num1 + num2
    multi = num1 * num2
    res = num1 - num2
    div = num1 / num2

    print("\nLos resultados son:")
    print("Suma =", suma)
    print("División =", div)
    print("Resta =", res)
    print("Multiplicación =", multi)