# Programa: Ejecutivo.py
# Objetivo: Programa que va a permitir definir la superclase
#           para controlar los Ejecutivos de Cuentas
# Autor: Marcos Pérez Almazán

from datetime import datetime # Validación de la fecha
import random

class Ejecutivo:
    def __init__(self, num_empleado: int, rfc: str, n_empleado: str, fecha_nac: str, direccion: str, telefono: str, sueldo_m: float):
        """
            Método constructor del Ejecutivo.
        :param num_empleado: El número de empleado.
        :param rfc: El Registro Federal de Contribuyentes del empleado.
        :param n_empleado: El nombre del empleado.
        :param fecha_nac: La fecha de nacimiento del empleado.
        :param direccion: La dirección del empleado.
        :param telefono: El número telefónico del empleado.
        :param sueldo_m: El sueldo mensual del empleado.
        """
        self.__num_empleado = num_empleado if num_empleado > 0 else abs(num_empleado)
        self.__rfc = rfc
        self.__n_empleado = n_empleado
        try:
            self.__fecha_nac = datetime.strptime(fecha_nac, "%d-%m-%Y").date()
        except ValueError:
            raise ValueError("La fecha {} no corresponde con el formato "
                  "dd-mm-yyyy.".format(fecha_nac))
        self.__fecha_nac = self.__fecha_nac.strftime("%d-%m-%Y")
        self.__direccion = direccion
        self.__telefono = telefono if len(str(telefono)) == 10 else str(telefono)[:-(len(str(telefono))-10)]
        self.__sueldo_m = sueldo_m

    #Agregamos los setters y getters correspondientes.
    #Agregamos los getters
    @property
    def num_empleado(self) -> int:
        """
        Método que se encarga de obtener el número de empleado.
        :return: El número de empleado.
        :rtype: int
        """
        return self.__num_empleado

    @property
    def rfc(self) -> str:
        """
        Método que se encarga de obtener el rfc del empleado.
        :return: El RFC del empleado.
        :rtype: str
        """
        return self.__rfc

    @property
    def n_empleado(self) -> str:
        """
        Método que se encarga de obtener el nombre del empleado.
        :return: El nombre del empleado.
        :rtype: str
        """
        return self.__n_empleado

    @property
    def fecha_nac(self) -> str:
        """
        Método que se encarga de obtener la fecha de nacimiento del empleado.
        :return: La fecha de nacimiento del empleado.
        :rtype: str
        """
        return self.__fecha_nac
    @property
    def direccion(self) -> str:
        """
        Método que se encarga de obtener la dirección del empleado.
        :return: La dirección del empleado.
        :rtype: str
        """
        return self.__direccion
    @property
    def telefono(self) -> str:
        """
        Método que se encarga de obtener el número de teléfono del empleado.
        :return: El número telefónico del empleado.
        :rtype: str
        """
        return self.__telefono

    @property
    def sueldo_m(self) -> float:
        """
        Método que se encarga de obtener el sueldo mensual del empleado.
        :return: El sueldo mensual del empleado.
        :rtype: float
        """
        return self.__sueldo_m

    #Agregar los setters
    @num_empleado.setter
    def num_empleado(self, num_empleado: int):
        """
        Método para establecer el número de empleado.
        :param num_empleado: El número de empleado.
        """
        self.__num_empleado = num_empleado if num_empleado > 0 else abs(num_empleado)

    @rfc.setter
    def rfc(self, rfc: str):
        if not isinstance(rfc, str) or not rfc.strip():
            raise ValueError("El RFC no puede estar vacío.")
        self.__rfc = rfc

    @n_empleado.setter
    def n_empleado(self, n_empleado: str):
        if not isinstance(n_empleado, str) or not n_empleado.strip():
            raise ValueError("El nombre del ejecutivo(a) no puede estar vacío.")
        self.__n_empleado = n_empleado

    @fecha_nac.setter
    def fecha_nac(self, fecha_nac: str):
        """
        Método para establecer la fecha de nacimiento del empleado.
        :param fecha_nac: La fecha de nacimiento del empleado.
        """
        try:
            self.__fecha_nac = datetime.strptime(fecha_nac, "%d-%m-%Y").date()
        except ValueError:
            raise ValueError ("La fecha {} no corresponde con el formato "
                  "dd-mm-yyyy.".format(fecha_nac))
        self.__fecha_nac = fecha_nac

    @direccion.setter
    def direccion(self, direccion: str):
        if not isinstance(direccion, str) or not direccion.strip():
            raise ValueError("La dirección no puede estar vacío")
        self.__direccion = direccion

    @telefono.setter
    def telefono(self, telefono: str):
        if not isinstance(telefono, (str)) or len(telefono) != 10:
            raise ValueError("El número de teléfono debe ser de 10 dígitos.")
        self.__telefono = telefono

    @sueldo_m.setter
    def sueldo_m(self, sueldo_m: float):
        if not isinstance(sueldo_m, (int, float)) or sueldo_m < 0:
            raise ValueError("El saldo mensual debe ser un número positivo.")
        self.__sueldo_m = sueldo_m

    def __str__(self):
        """
        Método que nos permite imprimir la información del Ejecutivo en formato cadena.
        :return: El Ejecutivo en formato cadena
        :rtype: str
        """
        return "Ejecutivo:: # de Ejecutivo: {} | RFC: {} | Nombre del Ejecutivo: {} | " \
                "Fecha de Nacimiento: {} | Dirección: {} | Teléfono: {} | Sueldo Mensual: ${} ".format(self.__num_empleado,
                                                                                             self.__rfc,
                                                                                             self.__n_empleado,
                                                                                             self.__fecha_nac,
                                                                                             self.__direccion,
                                                                                             self.__telefono,
                                                                                             self.__sueldo_m)
    def __iter__(self):
        """
        Método que devuelve una representación iterable de un objeto Ejecutivo.
        :return: La representación iterable de un objeto Ejecutivo
        :rtype: iterable
        """
        return iter([self.num_empleado, self.rfc, self.n_empleado, self.fecha_nac,self.direccion, self.telefono, self.sueldo_m])

    def __llave(self) -> tuple:
        """
        Método privado que nos permite obtener la llave de un objeto Ejecutivo.
        :return: Una tuple con los atributos del Ejecutivo.
        :rtype: tuple
        """
        return self.__num_empleado, self.__rfc, self.__n_empleado, self.__fecha_nac, self.__direccion, self.__telefono, self.__sueldo_m

    def __hash__(self) -> int:
        """
        Método que llama internamente a la función hash() para obtener el valor hash del objeto Ejecutivo.
        :return: Un valor entero que corresponde al hash del objeto Ejecutivo.
        :rtype: int
        """
        return hash(self.__llave())

    def __eq__(self, otro) -> bool:
        """
        Método que permite comparar dos Ejecutivos para saber si son iguales.
        :param otro: El otro Ejecutivo para comparar.
        :return: bool
        """
        respuesta = False
        if isinstance(otro, Ejecutivo):
            respuesta = self.__llave() == otro.__llave()
        return respuesta
    
    def a_dict(self):
        return {
            "num_empleado": self.__num_empleado,
            "rfc": self.__rfc,
            "n_empleado": self.__n_empleado,
            "fecha_nac": self.__fecha_nac,
            "direccion": self.__direccion,
            "telefono": self.__telefono,
            "sueldo_m": self.__sueldo_m
        }
