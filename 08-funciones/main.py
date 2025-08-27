"""
FUNCIONES:
Una función es un conjunto de instrucciones agrupadas
bajo un nombre concreto que pueden reutilizarse invocando
a la función tantas veces como sea necesario.

def nombreFuncion(parametros):
    # BLOQUE / CONJUNTO DE INSTRUCCIONES

nombreFuncion(mi_parametro)
nombreFuncion(mi_parametro) -> se puede callear siempre cuando uno quiera

"""

# # Ejemplo 1
# print("####### EJEMPLO 1 #######")


# # Definir Función
# def muestraNombre():
#     """Muestra Nombres"""
#     print("Muestra Nombre")
#     print("Jose")
#     print("\n")


# # Invocar Función
# muestraNombre()

# # Ejemplo 2: parametros
# print("####### EJEMPLO 2 #######")


# def mostrarTuNombre(nombre, edad):
#     print(f"Tu nombre es {nombre}")
#     if edad < 18:
#         print("Eres menor de edad")
#     else:
#         print("Eres mayor de edad")
#     print("\n")


# # mostrarTuNombre("Jose", 19)
# name = input("Ingresa tu nombre: ")
# age = int(input("Ingresa tu edad: "))
# mostrarTuNombre(name, age)
# print("\n")


# # Ejemplo 3: parametros adicionales
# print("####### EJEMPLO 3 #######")


# def tabla(numero):
#     print(f"Tabla de multiplicar: {numero}")
#     for contador in range(11):
#         operacion = numero * contador
#         print(f"{numero} * {contador} = {operacion}")
#     print("\n")


# for i in range(11):
#     tabla(i)

# # Ejemplo 4: parametros opcionales
# print("####### EJEMPLO 4 #######")

# def getEmpleado(name, ci=None):
#     print("EMPLEADO")
#     print(f"Nombre: {name}")
#     if ci != None:
#         print(f"C.I: {ci}")

# getEmpleado("Jose Garcia", 27313891)

# # Ejemplo 5: Return (Ejemplo)
# print("####### EJEMPLO 5 #######")

# # EJEMPLO
# # def saludame(nombre):
# #     return "Hola, saludos " + nombre

# # print(saludame("Jose"))

# # Ejemplo 6: Return (otro ejemplo del uso)
# print("####### EJEMPLO 6 #######")

# def calculadora(num1, num2, basicas=False, todos=False):
#     suma = num1 + num2
#     resta = num1 - num2
#     multi = num1 * num2
#     div = num1 / num2

#     concatCalc = ""

#     if todos != False:
#         concatCalc += "Suma: " + str(suma)
#         concatCalc += "\nResta: " + str(resta)
#         concatCalc += "\nMultiplicacion: " + str(multi)
#         concatCalc += "\nDivision: " + str(div)

#     elif basicas != False:
#         concatCalc += "Suma: " + str(suma)
#         concatCalc += "\nResta: " + str(resta)

#     else:
#         concatCalc += "Multiplicacion: " + str(multi)
#         concatCalc += "\nDivision: " + str(div)

#     return concatCalc


# print(f"Basicas \n{calculadora(5, 5, True)}\n")
# print(f"Avanzadas \n{calculadora(5, 5, False)}\n")
# print(f"Todas \n{calculadora(5, 5, False, True)}")

# # Ejemplo 7: Funciones dentro de otra
# print("####### EJEMPLO 7 #######")


# def getNombre(nombre):
#     texto = f"Tu nombre es {nombre}"
#     return texto


# def getApellidos(apellidos):
#     texto = f"Tus apellidos son {apellidos}"
#     return texto

# # EJEMPLO DE FUNCIONES DENTRO DE UNA FUNCION


# def getNombreApellido(nombre, apellidos):
#     texto = f"{getNombre(nombre)}\n{getApellidos(apellidos)}"
#     return texto


# # print(getNombre("Jose")," "+getApellidos("G N")) # -> ejemplo simple
# print(getNombreApellido("Jose", "Garcia Navarro"))

# # Ejemplo 8: Funciones lambda
# print("####### EJEMPLO 8 #######")

# tell_year = lambda year: f"El año es {year}"

# print(tell_year(2025))

# Ejemplo 9: Variables Globales y Locales
print("####### EJEMPLO 9 #######")


print("\n Finalizado...")
