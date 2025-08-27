""" 
clases 
"""


class Coche:
    """_summary_
    """
    # Atributos o propiedades (variables)
    # Caracteristicas del coche
    carcolor: str = "Rojo"
    marca: str = "Ferrari"
    modelo: str = "Adavantor"
    velocidad: int = 300
    caballos: int = 750
    plazas: int = 4
    # def __init__(self) -> None:
    #     pass
    # Métodos, son acciones que hace el objeto (funciones)

    def setColor(self, color: str) -> None:
        """_summary_

        Args:
            color (str): Modifica el color del coche
        """
        self.carcolor = color

    def getColor(self) -> str:
        """_summary_

        Returns:
            str: Retorna el color del coche
        """
        return self.carcolor

    def setModelo(self, modelo: str) -> None:
        """_summary_

        Args:
            modelo (str): Modifica el modelo del coche
        """
        self.modelo = modelo

    def getModelo(self) -> str:
        """_summary_

        Returns:
            str: Retorna el modelo del coche
        """
        return self.modelo

    def acelerar(self) -> None:  # Ejemplo Setters
        """_summary_
        """
        self.velocidad += 1
        print("Acelerando! ", self.velocidad)

    def frenar(self) -> None:  # Ejemplo Setters
        """_summary_
        """
        self.velocidad -= 1
        print("Frenando! ", self.velocidad)

    def getVelocidad(self) -> int:  # Ejemplo Getters
        """_summary_
        Returns:
            int: Retorna la velocidad
        """
        return self.velocidad
# fin definición clase


# Crear Objetos / Instanciar la clase
coche: Coche = Coche()
print("COCHE 1: ")
coche.setColor("Azul")
coche.setModelo("Gallardo")
print(coche.marca, coche.getModelo(), coche.getColor())
# print("Velocidad actual: ", coche.getVelocidad())
# coche.acelerar()
# coche.acelerar()
# coche.acelerar()
# coche.acelerar()
# print("Velocidad actual: ", coche.getVelocidad())
# coche.frenar()
# coche.frenar()
# coche.frenar()
# coche.frenar()
# print("Velocidad actual: ", coche.getVelocidad())

print("--------------------------------")
# Multiples objetos
coche2: Coche = Coche()
print("COCHE 2: ")
coche2.setColor("Verde")
coche2.setModelo("Murcielago")
print(coche2.marca, coche2.getModelo(), coche2.getColor())
