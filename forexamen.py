estudiantes = {}

while True:
    nombre = input("Nombre del estudiante (o 'salir'): ")
    if nombre.lower() == "salir":
        break

    nota = float(input("Nota: "))

    estado = "Aprobado" if nota >= 3 else "Reprobado"

    estudiantes[nombre] = {
        "nota": nota,
        "estado": estado
    }

print("\nRegistro final:")
print(estudiantes)
