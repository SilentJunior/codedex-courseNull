""" 
Ficheros Python:

"""

# from io import open
# import pathlib
# import shutil
# import os.path


def main():
    """ doc """

    # ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"  # -> original
    # print(ruta)

    # # Abrir archivo
    # with open(ruta, "a+", encoding="UTF-8") as archivo:
    #     # Escribir archivo
    #     archivo.write("HOLA MUNDO ME ESCRIBIERONNNN\n")
    #     # Cerrar
    #     archivo.close()
    #     if archivo.closed:
    #         print("archivo cerrado")

    # # Abrir archivo para lectura
    # with open(ruta, "r", encoding="UTF-8") as archivo_lectura:
    #     # Leer contenido
    #     # contenido = archivo_lectura.read() # -> solamente se puede leer una vez
    #     # print(contenido)

    #     # Leer contenido y guardarlo en lista
    #     listastr: list[str] = archivo_lectura.readlines()
    #     # print(listastr)
    #     archivo_lectura.close()
    #     # Leyendo la lista
    #     for frase in listastr:
    #         print("- "+frase.capitalize())

    # # Copiar
    # ruta_copia = str(pathlib.Path().absolute()) + \
    #     "/fichero_copiado.txt"  # -> copia
    # # ruta_alternate = "../13-paquetes/lacopiadelacopia.txt"

    # shutil.copyfile(ruta, ruta_copia)

    # # Mover
    # ruta_copia = str(pathlib.Path().absolute()) + \
    #     "/fichero_copiado.txt"  # -> copia
    # ruta_mover = str(pathlib.Path().absolute()) + \
    #     "/../12-modulos/fichero_copiado_movido.txt"  # -> copia movida
    # shutil.move(ruta_copia, ruta_mover)

    # # Eliminar
    # ruta_eliminar = str(pathlib.Path().absolute()) + \
    #     "/../12-modulos/fichero_copiado_movido.txt"  # -> eliminar
    # os.remove(ruta_eliminar)

    # # Comprobar
    # ruta_comprobar = str(pathlib.Path().absolute()) + \
    #     "/../12-modulos/fichero_copiado_movido.txt"  # -> comprobar
    # print(os.path.exists(ruta_comprobar))

    # # Crear carpeta
    # if not os.path.isdir("./mi_carpeta"):
    #     os.mkdir("./mi_carpeta")
    #     print("Directorio creado.")
    #     print("si vuelves a ejecutar el script, lo eliminarás.".capitalize())
    # else:
    #     # Eliminar carpeta
    #     os.rmdir("./mi_carpeta")
    #     print("directorio eliminado")

    # # Copiar carpeta
    # ruta_og = "./mi_carpeta"
    # ruta_copia = "./mi_carpeta-COPIADA"
    # shutil.copytree(ruta_og, ruta_copia)

    # # Revisar el contenido
    # # # Crear
    # archivouno = str(pathlib.Path().absolute()) + "/mi_carpeta/archivo1.txt"
    # holamundo = os.path.abspath("./mi_carpeta/holamundo.txt")
    # open(holamundo, "+a", encoding="UTF-8")
    # open(archivouno, "+a", encoding="UTF-8")
    # contenido = os.listdir("./mi_carpeta")
    # print("Contenido: ")
    # for ficheros in contenido:
    #     print(f"Fichero: {ficheros}")


if __name__ == "__main__":
    main()
