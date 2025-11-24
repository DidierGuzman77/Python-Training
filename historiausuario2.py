
inventario = []


def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    
 
    while True:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            cantidad = int(input("Ingrese la cantidad del producto: "))
            break
        except ValueError:
            print(" Error: Ingrese valores numéricos válidos para precio y cantidad.")

    producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    
 
    inventario.append(producto)
    print(f"Producto '{nombre}' agregado exitosamente.\n")

def mostrar_inventario():
    if len(inventario) == 0:
        print(" El inventario está vacío.\n")
    else:
        print("INVENTARIO ACTUAL")
        for producto in inventario:
            print(f"Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")
        print("--------------------------\n")

def calcular_estadisticas():
    if len(inventario) == 0:
        print("No hay productos para calcular estadísticas.\n")
    else:
        valor_total = sum(p["precio"] * p["cantidad"] for p in inventario)
        cantidad_total = sum(p["cantidad"] for p in inventario)
        
        print("ESTADÍSTICAS DEL INVENTARIO ")
        print(f"Valor total del inventario: ${valor_total:,.2f}")
        print(f"Cantidad total de productos: {cantidad_total}")
        print("------------------------------------")

def menu():
    while True:
        print("===== MENÚ PRINCIPAL =====")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Calcular estadísticas")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ")
        print()  

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            calcular_estadisticas()
        elif opcion == "4":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.\n")

menu()


