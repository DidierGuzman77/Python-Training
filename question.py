while True:
    try:
        tabla = []
    with open("multiplicar.txt", "w") as f:
    
            numero = int(input("ingrese un numero: "))
    except ValueError:
    print("solo numeros")
    for i in range (1, 11):
        f.write(f"{numero} x {i} = {i*numero} \n")
    with open("multiplicar.txt", "r") as f:
        for linea in f:
            print(linea)