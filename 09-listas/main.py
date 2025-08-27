""" 
LISTAS (arrays) PYTHON

Concepto?

Son colecciones o conjuntos de datos/valores, bajo un único
nombre.
Para acceder a esos valores podemos usar un indice númerico.

-> [1 - 10] se interpreta [0 - 9] <-

Es igual que una tupla, pero las tuplas no se pueden modificar

"""

# pelicula = "Batman"  # -> Variable
# definir lista
peliculas = ["Batman", "Superman", "Iron Man"]  # -> Lista forma

instrumentos = list(('Cello', 'Violoncelloxd', 'Violin',
                    'Viola'))  # -> Lista forma Tupla

instrumentosLs = [ls for ls in instrumentos]  # -> Comprension

# print(pelicula)
# print("Lista completa:", peliculas)
# print(instrumentos)

# # Indices
# print(peliculas[0])  # -> Indice 1
# print(instrumentosLs[1:3])  # -> desde el Indice 2 hasta indice 3
# print(peliculas[1:]) # -> a partir el Indice 2

# # Añadir elemento a Lista
# # instrumentosLs # -> actualmente ['Cello', 'Violoncelloxd', 'Violin', 'Viola']
# instrumentosLs.append("Contrabajo")
# # Ahora es ['Cello', 'Violoncelloxd', 'Violin', 'Viola', 'Contrabajo']
# print(instrumentosLs)

# # Recorrer
# print("**** LISTADO PELICULAS ****")
# for i in peliculas:
#     index = peliculas.index(i)
#     contador = index + 1
#     print(f"Index {index} ({contador}): {i}")

# Listas multidimensionales
print("\n********* Listado de contactos *********")
contactos = [
    [
        'Rigoberto',
        'rigo@worker.com'
    ],
    [
        'Jose',
        'jose@worker.com'
    ],
    [
        'Joaquin',
        'joaquin@worker.com'
    ],
    [
        'Navarro',
        'navarro@worker.com'
    ]
]

# for i, j in contactos:
#     print("\n")
#     print(f"Nombre: {i}\nEmail: {j}")

# for contacto in contactos:  # contacto -> Lista, contactos -> Lista multi
#     for elemento in contacto:  # recorre lista -> contacto
#         if contacto.index(elemento) == 0:
#             print("\nNombre: " + elemento)
#         else:
#             print("Correo: " + elemento)

# print(contactos[1][1])
