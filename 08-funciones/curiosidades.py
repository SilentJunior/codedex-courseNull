""" 
CURIOSIDADES

"""

# Las funciones se escriben antes que todos
# para mantener cierto orden en el código
# siempre deben tener un return y parametros


def mi_ejemplo(nom):
    return "Ejemplo 1 " + nom


def mi_ejemplo2(ape):
    return "Ejemplo 2 " + ape


nombre = "Mau"
apellido = "Lau"

print("hello world")
print(nombre, " ", apellido)
print(mi_ejemplo(nombre))
print(mi_ejemplo2(apellido))
