"""tipos"""

nada = None
cadena = "Me gusta python"
entero = 50
flotante = 50.0
booleano = True or False
lista = [10, 11, 14, 15]
tuplaNoCambia = ("dee", 25, True)
diccionario = {"id": 0,
               "name": "JJ"}
rango = range(9)
dato_byte = b"text"

# imprimir
print(entero)
# mostrar tipo de dato
print(type(entero))

# py variables-tipos/tipos.py

# # convertir de un tipo a otro
# print(float(entero))
# print(type(float(entero)))

# print(cadena + " " + entero) # -> error
# can only concatenate str (not "int") to str

# solución
print(cadena + " " + str(entero))
