""" 
Ejemplo usando try-except
"""


def main():
    """_summary_
    """
    try:
        listanumeros: list[int] = [2, 4, 1, 3, 7, 6, 9, 5]

        busqueda: int = int(input("Introduce el número: "))
        comprobar = isinstance(busqueda, int)

        while not comprobar:
            print("Escribe un numero, no texto\n")
            busqueda = int(input("Introduce el número: "))

        print(f"Has introducido el {busqueda}")
        print(f"#### Buscar en la lista el número {busqueda} ####")
        search = listanumeros.index(busqueda)
    except ValueError:
        print("El numero no se encuentra en la lista")
    else:
        print(f"Se ha encontrado el número buscado, es el indice {search}")
    finally:
        print("\nFinalizado\n")


if __name__ == "__main__":
    main()
