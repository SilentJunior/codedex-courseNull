""" 
Funciones y métodos predefinidos
"""


def mostrarstr(non=None):
    """ almacena str """
    if non is None:
        non = []
    lenlista = len(non)
    concat = ""
    for i in non:
        if non.index(i) != (lenlista - 1):
            concat += f"{i}, "
        else:
            concat += f"{i}"
    return concat


cantantes = ['Franco de Vita', 'Gianluca', 'Gualberto']

numeros = [1, 5, 2, 6, 3, 7, 4]
print("\nNumeros antes de sort " + mostrarstr(numeros))
# Ordenar
numeros.sort()
print("\nNumeros despues de sort " + mostrarstr(numeros))

# Añadir
print("\nCantantes: ", mostrarstr(cantantes))
cantantes.append('Matt Belamy')
cantantes.insert(2, 'Aurora')
print("\nCantantes: ", mostrarstr(cantantes))

# Eliminar
cantantes.pop(1)
cantantes.remove('Aurora')
print("\nCantantes: ", mostrarstr(cantantes))

# Dar la Vuelta
numeros.reverse()
print("\nNumeros volteados: ", mostrarstr(numeros))

# Condicional (buscar dentro de una lista)
print(7 in numeros)

# Contar elementos
len(numeros)

# Cuantas veces aparece un elemento
numeros.count(6)

# Conseguir el indice de un elemento
cantantes.index('Franco de Vita')

# # Unir listas
# cantantes.extend(numeros)
