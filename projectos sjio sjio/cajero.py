saldo = 1000000
opcion = ""

while opcion != "4":
    print("1. Ver saldo")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Salir")

    opcion = input("Elige: ")

    if opcion == "1":
        print("Saldo:", saldo)

    elif opcion == "2":
        cantidad = float(input("Depositar: "))
        saldo = saldo + cantidad

    elif opcion == "3":
        cantidad = float(input("Retirar: "))

        saldo = saldo - cantidad
        if cantidad > saldo:
         print("no tienes todo ese dinero")    