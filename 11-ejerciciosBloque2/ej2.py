""" 
Ejercicio 2. Escribir un programa que añada valores a una lista
mientras que su longitud sea menor a 120 y luego mostrar la lista
Plus: Usar while y for
"""


def main():  # -> no return
    """ Thank you pylint """
    numeros = []
    # for i in range(120):
    #     numeros.append(f"Elemento-{i}")
    #     print(f"Elemento agregado: {numeros[i]}")

    # # print(numeros)

    contador = 0
    while len(numeros) < 120:
        numeros.append(f"Elemento-{contador}")
        print(f"Elemento agregado: {numeros[contador]}")
        contador += 1


if __name__ == "__main__":
    main()
