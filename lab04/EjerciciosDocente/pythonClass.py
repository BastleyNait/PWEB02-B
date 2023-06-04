class MiClase:
    def __init__(self):
        self._variable_privada = 42
    
    def _funcion_privada(self):
        print("Esta es una función privada")
    
    def funcion_publica(self):
        print("Esta es una función pública")
        self._funcion_privada()

# Crear un objeto de la clase MiClase
objeto = MiClase()

# Acceder a la variable privada y llamar a la función pública
print(objeto._variable_privada)
objeto.funcion_publica()

# Intentar llamar a la función privada directamente
objeto._funcion_privada()  # No se recomienda hacer esto
