# contador = 1
# num = int (input("de que numero desea la tabla?: "))
# for contador in range(1,11):
#     print (f"{num} * {contador} = {num*contador}")

class Perro:
    color = ""
    raza = ""

    def __init__(self, raza, color):
        self.raza=raza
        self.color=color

        

rex = Perro("shitzu", "negro")
print(type(rex))
print(rex.color)

diccionario = {"clave1": "valor1", "clave2": "valor2", "clave3": "valor3"}

claves = diccionario.keys()
print(claves)
