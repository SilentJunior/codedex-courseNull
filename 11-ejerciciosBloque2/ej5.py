""" 
Ejercicio 5. 
Crear una lista con el contenido de esta tabla:
ACCION  AVENTURA    DEPORTES
GTA     ASSINS      FIFA 21
COD     CRASH       PRO 21 
PUGB    PRINCE OF PERSIA    MOTO GP 21

Mostrar esta informacion ordenada
"""


def main():
    """ Thank you Pylint """
    listajuegos = [
        {
            'genero': 'ACCION',
            'titulos': ['GTA', 'COD', 'PUGB']
        },
        {
            'genero': 'AVENTURA',
            'titulos': ['ASSASINS', 'CRASH', 'PERSIA']
        },
        {
            'genero': 'DEPORTES',
            'titulos': ['FIFA 21', 'PRO 21', 'MOTO GP 21']
        }
    ]

    for genero in listajuegos:  # Cambié a -> genero para mejor coherencia
        print("------------------------")
        print(f"Genero: {genero['genero']}")
        print("------------------------")
        print("Juegos:")
        for titulos in genero['titulos']:  # Cambié b -> titulos // // //
            print(titulos)
        print("------------------------")
        print("\n")


if __name__ == "__main__":
    main()
