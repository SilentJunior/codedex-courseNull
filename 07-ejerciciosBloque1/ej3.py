""" 

Ejercicio 3. Escribir un programa que muestre los cuadrados
(un número multiplicado por si mismo) de los 60 primero números
naturales. Resolverlo con for y con while

"""
contador = 0
print("********CUADRADOS********\n")
print("Numero \t= \tCuadrado")
# For
for i in range(61):
    print(f"{i} \t= \t{i*i}")

# # While
# while contador <= 60:
#     cuadrado = contador * contador
#     print(f"{contador} \t= \t{cuadrado}")
#     contador += 1
