""" 
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
"""


class Persona:
    """class Persona

    Returns:
        Padre: Clase Padre
    """
    __nombre: str
    __apellidos: str
    __altura: int
    __edad: int

    def __init__(self, nombre: str, apellidos: str, altura: int, edad: int) -> None:
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__altura = altura
        self.__edad = edad

    # GETTERS #
    def getnombre(self) -> str:
        """From class -> Persona

        Returns:
            str: Retorna nombre
        """
        return self.__nombre

    def getapellidos(self) -> str:
        """From class -> Persona

        Returns:
            str: Retorna apellidos
        """
        return self.__apellidos

    def getaltura(self) -> int:
        """From class -> Persona

        Returns:
            int: Retorna altura
        """
        return self.__altura

    def getedad(self) -> int:
        """From class -> Persona

        Returns:
            int: Retorna altura
        """
        return self.__edad

    # SETTERS #
    def setnombre(self, nombre: str) -> None:
        """From class -> Persona

        Args:
            nombre (str): Almacena el nombre proporcionado por el usuario
        """
        self.__nombre = nombre

    def setapellidos(self, apellidos: str) -> None:
        """From class -> Persona

        Args:
            apellidos (str): Almacena el/los apellidos proporcionado por el usuario
        """
        self.__apellidos = apellidos

    def setaltura(self, altura: int) -> None:
        """From class -> Persona

        Args:
            altura (int): Almacena la altura proporcionado por el usuario
        """
        self.__altura = altura

    def setedad(self, edad: int) -> None:
        """From class -> Persona

        Args:
            edad (int): Almacena la edad proporcionado por el usuario
        """
        self.__edad = edad

    # FUNCIONES GENERICAS QUE HEREDARAN (Ejemplos)
    def hablar(self) -> str:
        """from class -> Persona
        Returns:
            str: Talk
        """
        return "Estoy hablando"

    def caminar(self) -> str:
        """from class -> Persona
        Returns:
            str: Walk
        """
        return "Estoy caminando"

    def dormir(self) -> str:
        """from class -> Persona
        Returns:
            str: Sleep
        """
        return "Estoy durmiendo"


class Informatico(Persona):
    """Class Informatico

    Args:
        Persona (_type_): _description_

    Returns:
        _type_: _description_
    """
    __lenguajes: str
    __experienciayrs: int

    def __init__(self, nombre: str, apellidos: str, altura: int, edad: int,
                 lenguajes: str, experienciayrs: int) -> None:
        super().__init__(nombre, apellidos, altura, edad)
        self.__lenguajes = lenguajes
        self.__experienciayrs = experienciayrs

    def getlenguajes(self) -> str:
        """from class -> Informatico

        Returns:
            str: Retorna los lenguajes aprendidos
        """
        return self.__lenguajes

    def getexperiencia(self) -> int:
        """from class -> Informatico

        Returns:
            int: Retorna los años de experiencia
        """
        return self.__experienciayrs

    def setlenguajes(self, lenguajes: str) -> None:
        """
        Args:
            lenguajes (str): Almacena los lenguajes nuevos aprendidos
        """
        self.__lenguajes += "\nLenguajes nuevos aprendidos = " + lenguajes

    def setexperiencia(self, experiencia: int) -> None:
        """
        Args:
            experiencia (int): Almacena la experiencia calculando la actual con el resto a - b
        """
        self.__experienciayrs += (self.getexperiencia() - experiencia)

    def programar(self) -> str:
        """_summary_

        Returns:
            str: Programming
        """
        return "Estoy programando"

    def repararpc(self) -> str:
        """_summary_

        Returns:
            str: Repairing
        """
        return "Ordenador reparado"
