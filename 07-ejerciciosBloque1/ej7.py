""" 
Ejercicio 7. Hacer un programa que muestre todos los numeros impares
entre dos numeros que decida el usuario.
"""

num1 = int(input("Ingrese el Primer numero: "))
num2 = int(input("Ingrese el Segundo numero: "))

if num1 < num2:
    for i in range(num1, (num2+1)):
        if i % 2 != 0:
            print(i)
elif num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num1 == num2:
    print("Ambos numeros son iguales")
