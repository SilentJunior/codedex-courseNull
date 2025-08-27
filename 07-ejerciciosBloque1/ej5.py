""" 
Ejercicio 5. Hacer un programa que muestre todos los numeros entre
dos numeros que diga el usuario.
"""

num1 = int(input("Inserte primer numero: "))
num2 = int(input("Inserte segundo numero: "))

if num1 < num2:
    print(f"Rango del {num1} al {num2}\n")
    for i in range(num1, (num2 + 1)):
        print(i)
else:
    print("\nEl número 1 debe ser menor al número 2.\n")
