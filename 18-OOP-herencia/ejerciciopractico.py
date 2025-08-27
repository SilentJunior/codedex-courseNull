""" 
Crea una clase base Empleado con atributos nombre y salario.
Añade un método mostrar_detalles() que imprima el nombre y salario.

Luego crea dos clases derivadas:

EmpleadoTiempoCompleto que además tenga un atributo beneficios.

EmpleadoTiempoParcial que además tenga un atributo horas_trabajadas.

Sobrescribe el método mostrar_detalles() en ambas clases para
incluir sus datos específicos.

Finalmente, crea objetos de ambas y llama al método 
mostrar_detalles().
"""


class Empleado:
    """_summary_
    """
    __nombre: str
    __salario: int

    def __init__(self, nombre, salario) -> None:
        """_summary_

        Args:
            nombre (_type_): _description_
            salario (_type_): _description_
        """
        self.__nombre = nombre
        self.__salario = salario

    def mostrar_detalles(self) -> None:
        """_summary_
        """
        print(f"Nombre: {self.__nombre}\nSalario: {self.__salario}$")


class EmpleadoTiempoCompleto(Empleado):
    """_summary_

    Args:
        Empleado (_type_): _description_
    """
    # Atributos heredados:
    # nombre: str
    # salarios: int
    # Extra:
    # beneficios #
    __beneficios: bool

    def __init__(self, nombre: str, salario: int, beneficios: bool = True) -> None:
        super().__init__(nombre, salario)
        self.__beneficios = beneficios

    def mostrar_detalles(self) -> None:
        if self.__beneficios:
            super().mostrar_detalles()
            print("Cuenta con beneficios 👍🏻")


class EmpleadoTiempoParcial(Empleado):
    """_summary_

    Args:
        Empleado (_type_): _description_
    """
    # Atributos heredados:
    # nombre
    # salarios
    # Extra:
    # horas_trabajadas #
    __horas_trabajadas: int

    def __init__(self, nombre: str, salario: int, horas_trabajadas: int) -> None:
        super().__init__(nombre, salario)
        self.__horas_trabajadas = horas_trabajadas

    def mostrar_detalles(self) -> None:
        super().mostrar_detalles()
        print(f"Horas Trabajadas= {self.__horas_trabajadas}")
