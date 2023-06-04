nada = None
cadena = "Hola soy Richart Escobedo WEB"
entero = 99
flotante = 4.2
booleano = False
lista = [10, 20, 30, 100, 200]
listaString = [44, "treinta", 30, "cuarenta"]
tuplaNoCambia = ("master", "en", "python")
diccionario = {
    "nombre": "Victor",
    "apellido": "Robles",
    "curso": "Master en Python"
}
rango = range(9)
dato_byte = b"Probando"

# imprimir variable
#print(dato_byte)

#Mostrar tipo de dato
#print(type(dato_byte))

texto="Hola soy un texto"
numerito=str(776)
print("tipo dato tupla")
print(type(tuplaNoCambia))
print("tipo dato de lista string")
print(type(listaString))
print("tipo de dato de numerito")
print(type(numerito))
print("concatenando texto con numerito")
print(texto + " " + numerito)
numerito = int(numerito)
print("numerito casteado")
print(type(numerito))
numerito = float(numerito)
print("tipo de dato de numerito despues del casteo")
print(type(numerito))
numerito = int(numerito)
print("\nimprimiendo rango")
print(rango)
print(type(rango))