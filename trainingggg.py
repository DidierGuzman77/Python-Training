def contar_vocales(texto):
    vocales = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    texto = texto.lower()

    for char in texto:
        if char in vocales:
            vocales[char] += 1

    return vocales

texto_usuario = input("Escribe un texto: ")


resultado = contar_vocales(texto_usuario)
print(resultado)
