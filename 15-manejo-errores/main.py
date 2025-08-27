""" 
Manejo de Errores

# Capturar excepciones y manejar errores en código
# susceptible a fallos/errores
"""


def main():
    """_summary_
    """
    # # mejor forma
    # try:
    #     nombre: str = input("Cual es tu nombre: ")
    #     nombre_usuario: str = ""

    #     # HECHO EN PYTHON 3.8 SIN PYLINT CREO
    #     # if len(nombre) > 1:
    #     #     nombre_usuario: str = "El nombre es " + nombre

    #     # print(nombre_usuario)

    #     # HECHO EN PYTHON 3.13 CON PYLINT
    #     if len(nombre) > 1:
    #         nombre_usuario = "El nombre es " + nombre
    #     elif nombre.isnumeric():
    #         raise TypeError
    #     else:
    #         raise ValueError
    # # Multiples excepciones
    # except ValueError:
    #     print("Capturado error: No puede colocar nombres vacios")
    # except TypeError:
    #     print("Capturado error TypeError: El nombre son caracteres, no numeros")
    # else:
    #     print(nombre_usuario)
    # finally:
    #     print("Finalizado :D")
    # # NOTA, CON LAS ACTUALIZACIONES, LOS ERRORES FUERON CORRIGIENDO
    # # Y BUSCANDO MEJORES PRACTICAS

    # # Otro ejemplo
    # try:
    #     numero: int = int(input("Numero para elevarlo al cuadrado: "))
    #     print("El cuadrado es: " + str(numero * numero))

    # except ValueError:
    #     print("Error: No es un numero entero")

    # Otro ejemplo con excepcion personalizada

    # INICIALIZAMOS PORQUE DENTRO DEL TRY
    # NO PERMITE CAPTURA SIN VERIFICAR
    # PERO SI CAMBIOS Y VERIFICAR #
    nombre: str = input("Ingrese un nombre: ")
    edad_str: str = input("Ingrese una edad: ")
    # edad_str: str = ""
    edad: int = 0

    try:
        # SI COLOCAN LOS TIPOS CORRESPONDIENTES
        # A CADA QUIEN (NOMBRE -> STR, EDAD -> INT)
        # NO LES SALTARÁ EL TYPEERROR#
        if nombre.isalnum() or edad_str.isalpha():
            raise TypeError
        # LUEGO DE VERIFICAR, ALMACENAMOS EL STR
        # EN EL INT PARA OTRAS VERIFICACIONES
        # (SI ESTÁ VACIO O ENTRA EN EL RANGO
        # VALIDO DE EDAD) #
        edad = int(edad_str)
        # VERIFICAMOS QUE NO HAYAN DEJADO EL
        # CAMPO NOMBRE VACIO#
        if len(nombre) <= 0:
            raise ValueError
        # VERIFICAMOS QUE NO HAYAN COLOCADO
        # UNA EDAD NO VALIDA#
        if edad < 1 or edad > 100:
            raise ValueError
        # FINALMENTE, IMPRIMIMOS LOS VALORES CORRECTOS #
        print("\nNombre: " + nombre)
        print("Edad: " + str(edad))

    except TypeError:

        # EXCEPCION PARA CUANDO COLOCAN UN TIPO DE DATO
        # NO CORRESPONDIENTE #
        print("\nError: Incorrecto tipo de dato en el campo")
        print("Error: Numerico en nombre o letras en edad")

    except ValueError:
        # EXCEPCION: MENSAJE PARA AMBOS CAMPOS VACIOS#
        if nombre.strip() == "" and edad_str.strip() == "":
            print("\nLos campos no pueden estar vacios")
        # EXCEPCION: MENSAJE PARA CAMPO EDAD VACIO#
        elif edad_str == "":
            print("\nLa edad no puede estar vacia")
        # EXCEPCION: MENSAJE DE RANGO NO VALIDO DE EDAD#
        elif edad < 1 or edad > 100:
            print("\nLa edad no es valida, rango valido de edad: 1 - 100")
        # EXCEPCION: MENSAJE PARA CAMPO DE NOMBRE VACIO#
        elif len(nombre) <= 0:
            print("\nEl nombre no puede estar vacio")

    finally:
        print("\nFinalizado")


if __name__ == "__main__":
    main()
