""" 
OOP Oriented Objects Programming

La Programación Orientada a Objetos (OOP) en Python es un paradigma
que organiza el código en objetos, que son instancias de clases.
Cada objeto combina datos (atributos) y funciones (métodos) que 
operan sobre esos datos. Las clases actúan como planos para crear 
objetos con propiedades y comportamientos específicos, facilitando 
la organización, reutilización y mantenimiento del código.

Python implementa OOP de forma flexible y todos los tipos básicos son 
objetos, lo que permite modelar conceptos del mundo real como entidades 
con características y acciones, mejorando la claridad y modularidad del 
código.

# Definición de una clase
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo
        self.edad = edad      # Atributo

    def saludar(self):        # Método
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

# Crear un objeto (instancia) de Persona
persona1 = Persona("Ana", 30)

# Usar el método saludar del objeto
persona1.saludar()

En este ejemplo:

*Persona es la clase, la plantilla para crear objetos.

*El método __init__ es el constructor que inicializa el objeto con nombre y edad.

*saludar es un método que define el comportamiento del objeto.

*persona1 es una instancia (objeto) de la clase Persona con valores específicos.

*Usamos persona1.saludar() para que el objeto ejecute su acción

1. Encapsulamiento (Ocultación)
Concepto
Agrupa datos (atributos) y funciones (métodos) dentro de un objeto, y restringe 
el acceso directo a los datos internos para protegerlos y controlar cómo se accede 
o modifica la información.

Beneficios
Protege los datos de modificaciones accidentales.

Facilita el mantenimiento al ocultar detalles internos.

Define interfaces claras para interactuar con el objeto.

2. Abstracción
Concepto
Oculta la complejidad interna y solo expone al usuario los detalles necesarios 
para usar el objeto, simplificando el diseño y uso del software.

Beneficios
Reduce la complejidad al enfocar solo en lo esencial.

Facilita la reutilización y comprensión del código.

Modela objetos del mundo real mostrando solo características importantes.

3. Herencia
Concepto
Permite crear nuevas clases (subclases) que heredan atributos y métodos de 
otras clases existentes (superclases), promoviendo la reutilización de código 
y la creación de jerarquías.

Beneficios
Evita duplicación de código.

Facilita extensión y personalización de clases.

Establece relaciones jerárquicas entre objetos.

4. Polimorfismo (Modularidad)

Concepto
Permite que diferentes clases puedan ser tratadas de manera uniforme a través 
de una misma interfaz, aunque cada clase implemente esa interfaz con un comportamiento específico.

Beneficios
Incrementa la flexibilidad y extensibilidad del código.

Permite usar objetos de diferentes clases intercambiablemente.

Facilita la implementación de código genérico y modular.

Estos pilares juntos permiten diseñar programas organizados, claros y robustos, 
reflejando mejor las entidades y relaciones del mundo real.

1. Encapsulamiento (Ocultación)
Oculta los detalles internos de un objeto y permite acceder o modificar sus datos 
solo mediante métodos públicos.

python
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Atributo privado
        self.__edad = edad      # Atributo privado

    def get_nombre(self):       # Getter público
        return self.__nombre

    def set_edad(self, nueva_edad):  # Setter controlado
        if nueva_edad > 0:
            self.__edad = nueva_edad
        else:
            print("Edad inválida")

persona = Persona("Ana", 30)
print(persona.get_nombre())  # Ana
persona.set_edad(35)
Aquí, los atributos con doble guion bajo __ son privados y no accesibles directamente desde fuera.

2. Abstracción
Oculta complejidades internas y expone solo funcionalidad necesaria para el usuario.

python
class CuentaBancaria:
    def __init__(self, saldo=0):
        self.__saldo = saldo

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto

    def retirar(self, monto):
        if 0 < monto <= self.__saldo:
            self.__saldo -= monto

    def mostrar_saldo(self):
        return self.__saldo

cuenta = CuentaBancaria(100)
cuenta.depositar(50)
cuenta.retirar(30)
print(cuenta.mostrar_saldo())  # 120
El usuario solo interactúa con métodos de alto nivel, no con detalles internos.

3. Herencia
Permite que una clase derive de otra y herede sus atributos y métodos.

python
class Animal:
    def hablar(self):
        print("El animal hace un sonido")

class Perro(Animal):  # Perro hereda de Animal
    def hablar(self):
        print("Guau guau")

perro = Perro()
perro.hablar()  # Guau guau
Perro extiende Animal y redefine su comportamiento.

4. Polimorfismo (Modularidad)
Objetos de diferentes clases pueden ser usados a través de la misma interfaz.

python
class Gato(Animal):
    def hablar(self):
        print("Miau")

def hacer_hablar(animal):
    animal.hablar()

hacer_hablar(Perro())  # Guau guau
hacer_hablar(Gato())   # Miau

La función hacer_hablar funciona con cualquier objeto que tenga el método hablar.
"""
