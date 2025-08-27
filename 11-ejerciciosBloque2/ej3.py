""" 
Ejercicio 3. Programa que compruebe si una variable está vacia
y si está vacia, rellenarla con texto en minusculas y mostrarlo
en mayusculas.
"""


def main():
    """ Thank you pylint """
    caracter = ""
    if len(caracter.strip()) <= 0:  # usar strip() para asegurarse
        # caracter = input("Ingrese un texto: ") #-> mi version
        caracter = "colibri colibri (se guardó en minusculas)"
        print(caracter.upper())
    else:
        print(f"La variable tiene contenido: {caracter}")


if __name__ == "__main__":
    main()
