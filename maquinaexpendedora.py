print("=== MÁQUINA EXPENDEDORA ===")
print("Código 049 - Agua  - $5")
print("Código 047 - Jugo  - $5")
print("Código 045 - Café  - $5")

# Precios (todos valen 5)
precios = {
    49: 5,
    47: 5,
    45: 5
}

# Pedir código del producto
opcion = int(input("Ingrese el código del producto (049, 047, 045): "))

if opcion not in precios:
    print("Código inválido. Intente nuevamente.")
else:
    precio = precios[opcion]
    print(f"El producto cuesta: ${precio}")

    # Pedir dinero
    pago = float(input("Ingrese el dinero: $"))

    if pago < precio:
        print("Dinero insuficiente. No se puede completar la compra.")
    else:
        cambio = pago - precio
        print("¡Compra exitosa!")

        if cambio > 0:
            print(f"Su cambio es: ${cambio}")

        print("Gracias por su compra.")
