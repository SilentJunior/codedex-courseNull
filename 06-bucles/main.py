""" BUCLES O CICLOS
 
# FOR

for variable in elemento_iterable:
    bloque de código

# WHILE

while condición:
    bloque de código
    actualización de la condición
    
"""

# # # Bucle For
# # for i in range(11):
# #     if i == 1:
# #         print(f"Muestro el mensaje {i} vez")
# #     else:
# #         print(f"Muestro el mensaje {i} veces")

# # otro ejemplo bucle for
# print("\n\tTABLA DE MULTIPLICAR")
# print("#######################################")
# num_ususario = int(
#     input("Indique el número a mostrar de tabla de multiplicar: "))
# print("#######################################\n")

# for num_tabla in range(1, 11):
#     print(f"{num_ususario} x {num_tabla} = {num_ususario * num_tabla}")
# print("\n#######################################\n")

# # Bucle While
# contador = 1
# concatenado = str(0)
# while contador <= 100:
#     # print("Muestro " + str(contador))
#     concatenado = concatenado + ", " + str(contador)
#     contador += 1
# print(concatenado)

# ejemplo bucle while
print("\n\tTABLA DE MULTIPLICAR")
print("#######################################")
num_ususario = int(
    input("Indique el número a mostrar de tabla de multiplicar: "))
print("#######################################\n")
num_contador = 1
while num_contador <= 10:
    print(f"{num_ususario} x {num_contador} = {num_ususario * num_contador}")
    num_contador += 1
print("\n#######################################\n")
