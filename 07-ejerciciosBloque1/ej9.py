""" 
Ejercicio 9. Hacer un programa que pida numeros al usuario
            indefinidamente hasta meter el numero 111
"""

numero = int(input("Ingrese un numero: "))

while numero != 111:
    print(f"Numero: {numero}\n")
    numero = int(input("Ingrese otro numero: "))
print("Adios")
