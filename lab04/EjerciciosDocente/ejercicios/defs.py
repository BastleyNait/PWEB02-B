# def colorFavorito(color1, color2, color3="rosado"):
#     print(f"""tus colores favoritos son
# {color1}
# {color2}
# {color3}""")


# colorFavorito("rojo", "verde")


def multiplicacion(*numeros):
    producto = 1
    for numero in numeros:
        producto *= numero
    print(producto)    


multiplicacion(2,10,10,10)