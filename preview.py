coders = []
print(coders)

amaount = int(input("cuantos users va a agregar: "))

while amaount !=0:
    name= input("ingrese su nombre: ")
    lastname = input("ingrese su apellido: ")
    age= input("ingrese su edad: ")
    email = input("ingrese su email:")

    coder = {
        "nombre": name,
        "apellido": lastname,
        "edad": age,
        "email": email
    }

    coders.append(coder)
    amaount -= 1
print(coders)