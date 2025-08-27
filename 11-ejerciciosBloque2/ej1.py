""" 
Ejercicio 1. Hacer un programa que tenga una lista
de 8 numeros enteros y haga lo siguiente:
(hecho) - Recorrer la lista y mostrarla
(hecho) - Hacer funcion que recorra listas de numeros y devuelva un string
(hecho) - Ordenarla y mostrarla
(hecho) - Mostrar su longitud
(hecho de dos formas) - Buscar algun elemento (Que el usuario pida por teclado)
"""

listanumeros = [2, 4, 1, 3, 7, 6, 9, 5]
# listanumeros = []


# 2. Funcion que recorre lista y retorna string
def recorrerls(lista=None):
    """ Recorre una lista y retorna string """
    if lista is None:
        lista = []
    longls = len(lista)
    strcon = ""
    for look in lista:
        if lista.index(look) != (longls-1):
            strcon += f"{look}, "
        else:
            strcon += f"{look}\n"
    return strcon

# FANCY STYLE #


# # 1. Recorrer y mostrarla (fancy style)
# def recorrerlsfancy(lista=None):
#     """ Recorre una lista """
#     if lista is None:
#         lista = []
#     longls = len(lista)
#     strcon = ""
#     for look in lista:
#         if lista.index(look) != (longls-1):
#             strcon += f"{look}, "
#         else:
#             strcon += f"{look}"
#     return f"\nLista Recorrida\n{strcon}"


# # 2. Ordenarla y mostrarla (fancy style)
# def ordenarlsfancy(lista=None):
#     """ Ordenar una lista """
#     if lista is None:
#         lista = []
#     lista.sort()
#     longls = len(lista)
#     strcon = ""
#     for look in lista:
#         if lista.index(look) != (longls-1):
#             strcon += f"{look}, "
#         else:
#             strcon += f"{look}"
#     return f"\nLista Ordenada\n{strcon}"


# # 3. Mostrar su longitud (fancy style)
# def mostrarlongitud(lista=None):
#     """ Mostrar la longitud """
#     if lista is None:
#         lista = []
#         lista.sort()
#     return f"\nLongitud de lista: {len(lista)}"


# # 4. Buscar algun elemento (fancy style)
# def buscarelemento(lista=None):
#     """ Buscar elemento """
#     if lista is None:
#         lista = []
#         lista.sort()
#     busqueda = input("\nIndique un numero a buscar: ")
#     while True:
#         if busqueda.lower() == 'parar':
#             break
#         for ls in lista:
#             if ls == int(busqueda):
#                 print(f"Encontrado el numero {ls}.\n")
#         busqueda = input("Indique un numero a buscar: ")
#     return "\nFinalizado"

# print("Lista: ", listanumeros)
# print(recorrerlsfancy(listanumeros))
# print(ordenarlsfancy(listanumeros))
# print(mostrarlongitud(listanumeros))
# print(buscarelemento(listanumeros))


# FANCY STYLE #

print("################ Recorrer y mostrar ################")
# Recorrer y mostrar
for ls in listanumeros:
    print(ls)

print("\n################ Recorrer y mostrar String ################")
# Recorrer lista e imprimir string
print(recorrerls(listanumeros))

print("\n################ Ordenar y mostrar ################")
# Ordenar y mostrar
listanumeros.sort()
for ls in listanumeros:
    print(ls)

print("\n################ Mostrar su longitud ################")
# Mostrar su longitud
LENLS = len(listanumeros)
print(f"\nLongitud de la lista: {LENLS}")

print("\n################ Busqueda de elemento ################")
# Busqueda de elemento
# while True: # -> Forma normal
#     busqueda = input("\nIndique un numero a buscar: ")
#     if busqueda.lower() == "parar":
#         break
#     if int(busqueda) in listanumeros:
#         print(f"\nEncontrado el numero {busqueda}.")
#     else:
#         print(f"\nNumero {busqueda} no encontrado")

busqueda: int = int(input("Introduce el número: "))
comprobar = isinstance(busqueda, int)

while not comprobar or busqueda <= 0:
    busqueda = int(input("Introduce el número: "))

print(f"Has introducido el {busqueda}")

print(f"#### Buscar en la lista el número {busqueda} ####")

search = listanumeros.index(busqueda)

print(f"Se ha encontrado el número buscado, es el indice {search}")

print("\nFinalizado\n")
