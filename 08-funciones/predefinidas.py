""" 
FUNCIONES PREDEFINIDAS

conocidas:
print()
type() -> dentro de print() bcs return
isinstance()
"""

print(type("Hello"))  # -> print() funcion predefinida

# Detectar el (tipado) -> type
comprobar = isinstance("hello", str)
if comprobar != False:
    print("'Hello' es tipo str")
else:
    print("'Hello' no es tipo str")

if not isinstance("hello", float):
    print("No es un numero con decimales")

# Eliminar el espacio
frase = "    muchos espacios :c       "
print("Sin strip:", frase)
print("Con strip:", frase.strip())

# Eliminar variables
year = 2025
print("Antes del borrado: ", year)
del year
# print("jeje ", year)

# Comprobar variable vacia
texto = "  ff "

if len(texto) <= 0:
    print("Variable vacia")
else:
    print("Variable con contenido")

# Buscar
frase = "El destino es lo mejor"
print(frase.find("mejor"))

# Reemplazar
print(frase.replace("El destino", "La bendición"))
