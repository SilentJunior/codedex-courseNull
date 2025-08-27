""" 
Ejercicio 8. ¿Cuanto es el X por ciento de X numero?
                20% de 150
"""

numero = int(input("Ingrese un numero: "))
porcentaje = int(input("Ingrese un porcentaje: "))

resultado = numero * (porcentaje/100)
print(f"El {porcentaje}% de {numero} es = {resultado}")
