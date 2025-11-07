name = input("cual es el nombre del producto: ")
while True:
    price = input ("Cual es el precio de este producto: ")
    quantity = input ("cual es la cantidad de productos: ")
    try:
        price = float(price)
        quantity = int(quantity)
        break
    except:
        print("error, ingrese valores validos")
total_cost = (price * quantity)
print(f"product: {name} price: {price} quantity: {quantity}total: {total_cost} ")