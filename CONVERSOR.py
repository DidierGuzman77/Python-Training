try:
 celsius = int(input("Ingrese la temperatura: "))
except ValueError:
    print("ingresa una temperatura valida")
farenheit = (celsius * 9/5) + 32

print (f"{celsius} grados celsius a farenheit son: {farenheit} farenheit")
