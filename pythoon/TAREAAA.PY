compra = float(input("Valor de la compra: "))

if compra < 50:
    precio = compra
else:
    if compra <= 100:
        precio = compra * 0.9
    else:
        if compra <= 200:
            precio = compra * 0.8
        else:
            precio = compra * 0.7

print("Total a pagar:", precio)