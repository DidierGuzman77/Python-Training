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




inventario = {}

while True:
    producto = input("Nombre del producto (o 'salir'): ")
    if producto.lower() == "salir":
        break

    precio = float(input("Precio: "))

    if precio > 100000:
        categoria = "Costoso"
    else:
        categoria = "Económico"

    inventario[producto] = {
        "precio": precio,
        "categoria": categoria
    }

print("\nInventario final:")
print(inventario)




empleados = {}

while True:
    nombre = input("Nombre del empleado (o 'salir'): ")
    if nombre.lower() == "salir":
        break

    salario = float(input("Salario: "))
    experiencia = int(input("Años de experiencia: "))

    if experiencia >= 5:
        bono = True
    else:
        bono = False

    empleados[nombre] = {
        "salario": salario,
        "experiencia": experiencia,
        "bono": bono
    }

print("\nLista final de empleados:")
print(empleados)




productos = {}

while True:
    nombre = input("Producto (o 'salir'): ")
    if nombre.lower() == "salir":
        break

    precio = float(input("Precio: "))
    tipo = input("Tipo (comida / tecnologia / medicina): ").lower()

    if tipo == "comida":
        iva = 0.05
    elif tipo == "tecnologia":
        iva = 0.19
    elif tipo == "medicina":
        iva = 0
    else:
        print("Tipo inválido")
        continue

    precio_final = precio + (precio * iva)

    productos[nombre] = {
        "precio_base": precio,
        "tipo": tipo,
        "iva": iva,
        "precio_final": precio_final
    }

print("\nProductos registrados:")
print(productos)

