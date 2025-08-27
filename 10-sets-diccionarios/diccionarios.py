""" 
Diccionario:
Un tipo de dato que almacena un conjunto de datos.
En formato clave -> valor.
Es parecido a un array asociativo o un objeto json.
"""

# Diccionario

persona = {
    "nombre": "Jose",
    "apellido": "Garcia",
    "ocupacion": "Desarrollador"
}

# print(persona)
# print(persona["ocupacion"])

# Lista con diccionarios

contactos = [
    {
        'nombre': 'JJ',
        'email': 'jj@desarrollador.com'
    },
    {
        'nombre': 'GN',
        'email': 'gn@desarrollador.com'
    },
    {
        'nombre': 'silenjunior',
        'email': 'blcsheep@desarrollador.com'
    }
]

# print(contactos)

print("\nLista de contactos:")
print("-------------------------------")
for i in contactos:
    print(f"Nombre: {i['nombre']}")
    print(f"E-mail: {i['email']}")
    print("-------------------------------")
