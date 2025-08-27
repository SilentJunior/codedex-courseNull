"""
Ejercicio 6.  Mostrar todas las tablas de multiplicar del 1 al 10.
Mostrando el titulo de la tabla y luego las multiplicaciones del 1 al 10
"""

print("TABLAS DE MULTIPLICAR\n")
for i in range(1, 11):
    print("Tabla de "+str(i)+"\n")
    for j in range(1, 11):
        # Aqui van las multis
        print(f"{i} * {j} = {i*j}")
    print("\n")