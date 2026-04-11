estudiantes = [
    {"nombre": "Ana", "nota": 4.5},
    {"nombre": "Luis", "nota": 2.8},
    {"nombre": "María", "nota": 3.9},
    {"nombre": "Juan", "nota": 1.7},
    {"nombre": "Sofía", "nota": 4.1}
]

mejor = estudiantes[0]
peor = estudiantes[0]

for e in estudiantes:
    if e["nota"] > mejor["nota"]:
        mejor = e
    if e["nota"] < peor["nota"]:
        peor = e

print("Nota más alta:", mejor["nombre"], mejor["nota"])
print("Nota más baja:", peor["nombre"], peor["nota"])