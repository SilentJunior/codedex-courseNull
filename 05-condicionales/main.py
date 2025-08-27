"""condicionales
# Condicional IF

SI its_TRUE_condition:
    Ejecutar bloque de codigos/instrucciones
SI NO:
    Ejecutar otro bloque de codigos/instrucciones

ejemplo:

if true_condition:
    code_blocks
else:
    code_blocks

# Operadores de comparación:

== Igual
!= Distinto
< menor que
> Mayor que
<= menor o igual que
>= Mayor o igual que

"""

# Ejemplo 1
print("############ EJEMPLO 1 ############")

color = "verde"
# color = input("Adivina mi color favorito: ")

if color.lower() == "Azul".lower():
    print("Adivinaste mi color favorito")
else:
    print("Color incorrecto")

# Ejemplo 2
print("\n############ EJEMPLO 2 ############")

year = 2020
year = int(input("¿En que año estamos? "))

if year >= 2021:
    print("Estamos de 2021 en adelante!!")
else:
    print("Es un año anterior a 2021")

# Ejemplo 3
print("\n############ EJEMPLO 3 ############")

edad_min = 18
edad_max = 65
edad_oficial = input("¿Tienes edad para trabajar?\n\nIntroduce tu edad: ")

# primera forma
if edad_oficial >= edad_min and edad_oficial <= edad_max:
    print("Está en edad de trabajar !!\n")
else:
    print("No está en edad de trabajar\n")

# # segunda forma (difiere en los casos)
# if edad_min <= edad_oficial <= edad_max:
#     print("Está en edad de trabajar !!\n")
# else:
#     print("No está en edad de trabajar\n")
