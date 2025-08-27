"""_summary_

    Returns:
        _type_: _description_
    """

# from dataclasses import dataclass


# @dataclass
# class DataCoche:
#     """_summary_
#     """
#     marca: str
#     modelo: str
#     color: str
#     velocidad: int
#     caballos: int
#     plazas: int


# constructor #
class Coche:
    """_summary_

    Returns:
        _type_: _description_
    """
    # Atributos o propiedades (variables)
    # Caracteristicas del coche
    
    # def __init__(self, coche: DataCoche) -> None:
    def __init__(self, marca: str, modelo: str,
                 color: str, velocidad: int,
                 caballos: int, plazas: int) -> None:
        """_summary_

        Args:
            marca (str): _description_
            modelo (str): _description_
            color (str): _description_
            velocidad (int): _description_
            caballos (int): _description_
            plazas (int): _description_
        """
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad = velocidad
        self.caballos = caballos
        self.plazas = plazas

    # Métodos, son acciones que hace el objeto (funciones)

    def setcolor(self, color: str) -> None:
        """_summary_

        Args:
            color (str): Modifica el color del coche
        """
        self.color = color

    # def setmodelo(self, modelo: str) -> None:
    #     """_summary_

    #     Args:
    #         modelo (str): Modifica el modelo del coche
    #     """
    #     self.modelo = modelo

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

    # Ejemplo Getters

    def getmarca(self) -> str:
        """_summary_

        Returns:
            str: Retorna la marca del coche
        """
        return self.marca

    def getmodelo(self) -> str:
        """_summary_

        Returns:
            str: Retorna el modelo del coche
        """
        return self.modelo

    def getcolor(self) -> str:
        """_summary_

        Returns:
            str: Retorna el color del coche
        """
        return self.color

    def getvelocidad(self) -> int:
        """_summary_
        Returns:
            int: Retorna la velocidad
        """
        return self.velocidad

    def getcaballos(self) -> int:
        """_summary_

        Returns:
            int: Retorna el caballaje
        """
        return self.caballos

    def getplazas(self) -> int:
        """_summary_

        Returns:
            int: Retorna las plazas
        """
        return self.plazas

    def getinfo(self) -> str:
        """_summary_

        Returns:
            str: Retorna todos los getters
            * Marca
            * Modelo
            * Color
            * Velocidad
            * Caballos
            * Plazas
        """
        info = "------------ Información del Coche ------------"
        # txtmarca_modelo: str = f"-Marca = {self.getmarca()}\n-Modelo = {self.getmodelo()}\n"
        # txtcolor_velocidad: str = f"-Color = {self.getcolor()}\n-Velocidad = {self.getvelocidad()}\n"
        # txtcaballos_plazas: str = f"-Caballos = {self.getcaballos()}\n-Plazas = {self.getplazas()}"
        info += "\n- Marca = "+self.getmarca()
        info += "\n- Modelo = "+self.getmodelo()
        info += "\n- Color = "+self.getcolor()
        info += "\n- Velocidad = "+str(self.getvelocidad())
        info += "\n- Caballos = "+str(self.getcaballos())
        info += "\n- Plazas = "+str(self.getplazas())
        return info
