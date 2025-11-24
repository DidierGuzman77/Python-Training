
tareas = []

def agregar_tarea(titulo):
    tarea = {
        "titulo": titulo,
        "completada": False
    }
    tareas.append(tarea)
    print("Tarea agregada correctamente.")

def completar_tarea(indice):
    if 0 <= indice < len(tareas):
        tareas[indice]["completada"] = True
        print("Tarea marcada como completada.")
    else:
        print("Índice inválido.")

def mostrar_tareas():
    if not tareas:
        print("No hay tareas aún.")
        return
    
    print("\n--- LISTA DE TAREAS ---")
    for i, tarea in enumerate(tareas):
        estado = "✔ Completada" if tarea["completada"] else "✘ Pendiente"
        print(f"{i}. {tarea['titulo']} — {estado}")
    print("------------------------\n")


# ---- MENÚ PRINCIPAL ----
while True:
    print("1. Agregar tarea")
    print("2. Marcar tarea como completada")
    print("3. Mostrar todas las tareas")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        titulo = input("Escribe el título de la tarea: ")
        agregar_tarea(titulo)

    elif opcion == "2":
        try:
            indice = int(input("Índice de la tarea a completar: "))
            completar_tarea(indice)
        except ValueError:
            print("Debes ingresar un número.")

    elif opcion == "3":
        mostrar_tareas()

    elif opcion == "4":
        print("¡Programa finalizado!")
        break

    else:
        print("Opción inválida, intenta de nuevo.")
