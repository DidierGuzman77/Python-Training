
curso_python = {
    "nombre_curso": "Python Básico",
    "duracion_horas": 40,
    "estudiantes": ["Didier", "Luka", "Jesus"],
    "activo": True
}


print("Claves:", curso_python.keys())

print("Valores:", curso_python.values())

print("\nPares clave-valor:")
for clave, valor in curso_python.items():
    print(clave, ":", valor)


nivel = curso_python.get("nivel", "principiante")
print("\nNivel del curso:", nivel)

