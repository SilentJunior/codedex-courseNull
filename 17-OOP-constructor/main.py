""" 
Main.py - OOP_Constructor
"""
from coche import Coche

fcoche: Coche = Coche("Renault", "RR2012", "Azul", 150, 50, 2)
acoche: Coche = Coche("Toyota", "Toyotaro", "Verde", 300, 150, 7)
ccoche: Coche = Coche("Chevrolet", "Chevrolete", "Amarillo", 285, 100, 5)
bcoche: Coche = Coche("BMW", "Quelujoso", "Lila", 400, 150, 9)
print(fcoche.getinfo())
print(acoche.getinfo())
print(ccoche.getinfo())
print(bcoche.getinfo())
print(bcoche.modelo)
nocoche: str = "Soy un coche :P"
# # Dectetar el tipado
# # if type(acoche) == Coche: # -> funciona igual
# if isinstance(nocoche, Coche):  # -> funciona igual
#     print("Es un objeto")
# else:
#     print("No es un objeto")
