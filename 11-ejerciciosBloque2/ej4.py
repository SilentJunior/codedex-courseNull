""" 
Ejercicio 4. Crear un script que tenga 4 variables -> 1 lista, 1 string,
1 entero y 1 booleano y que imprima un mensaje segun el tipo de dato
de cada variable

Usar funciones
"""


# Extra, traductor de tipos
def traducirtipo(tipo=type):
    """ Traduce de <class type> -> type """
    result = None
    if tipo == list:
        result = "LISTA"
    elif tipo == str:
        result = "CADENA DE TEXTO"
    elif tipo == int:
        result = "ENTERO"
    elif tipo == bool:
        result = "BOOLEANO"
    return result

# # MI SOLUCION
# def whattype(lista, string, entero, booleano):
#     """ Revisamos que tipo es la variable """
#     strtipo = ""
#     strtipo += f"Tipo 1era variable: {traducirtipo(type(lista))}\n"
#     strtipo += f"Tipo 2da variable: {traducirtipo(type(string))}\n"
#     strtipo += f"Tipo 3era variable: {traducirtipo(type(entero))}\n"
#     strtipo += f"Tipo 4ta variable: {traducirtipo(type(booleano))}\n"
#     return strtipo


# SOLUCION CURSO (nota: El enunciado dicta de mostrar el tipo, no comprobar)
def comprobartipado(dato, tipo: type):
    """ comprueba si es el tipo de variable que le queriamos asignar """
    test = isinstance(dato, tipo)

    if test:
        return f"Este dato es del tipo {traducirtipo(tipo)}"

    return "Este dato no es del tipo indicado"


def main():
    """ Thank you Pylint """
    print("hallo")
    listas = [23]
    strings = "Hola mundo"
    enteros = 22
    booleanos = True
    # print(whattype(listas, strings, enteros, booleanos))
    print(comprobartipado(listas, list))
    print(comprobartipado(strings, str))
    print(comprobartipado(enteros, int))
    print(comprobartipado(booleanos, bool))


if __name__ == "__main__":
    main()
