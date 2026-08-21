# Programa: Cuenta.py
# Objetivo: Programa que va a permitir definir la superclase
#           para controlar Cuentas
# Autor: -Carolina Flores Zarraga
#-Ivana Martinez Hernandez
#-David Enrique Ortiz Gonzalez
#-Marcos Pérez Almazán

from datetime import datetime # Validación de la fecha
from validate_email import validate_email # Validación del email
from abc import ABC, abstractmethod
class Cuenta(ABC):
    def __init__(self, n_cliente: str, num_cliente: int, fecha_apertura: str, num_sucursal: int, estado: str, correo: str, telefono: str):
        """
        Método constructor de la Cuenta.
        :param n_cliente: El nombre del cliente de la Cuenta
        :param num_cliente: El número del cliente de la Cuenta
        :param fecha_apertura:  La fecha de apertura de la Cuenta  en str con formato dd-mm-yyyy.
        :param num_sucursal: El número de la sucursal.
        :param estado: El estado de la sucursal.
        :param correo: El correo electrónico del cliente de la Cuenta.
        :param telefono: El teléfono del cliente de la Cuenta.
        """
        self.__n_cliente = n_cliente
        self.__num_cliente = num_cliente if num_cliente >0 else abs(num_cliente)
        try:
            self.__fecha_apertura = datetime.strptime(fecha_apertura, "%d-%m-%Y").date()
        except ValueError:
            raise ValueError("La fecha {} no corresponde con el formato "
                  "dd-mm-yyyy.".format(fecha_apertura))
        self.__fecha_apertura = self.__fecha_apertura.strftime("%d-%m-%Y")
        self.__num_sucursal = num_sucursal
        self.__estado = estado
        self.__correo = correo #if re.fullmatch(correo) else "correo@dominio.com"
        self.__telefono = telefono

    #Agregamos los setters y getters correspondientes.
    #Agregamos los getters
    @property
    def n_cliente(self) -> str:
        """
        Método que se encarga de obtener el nombre de cliente de la Cuenta
        :return: El nombre del Cliente
        :rtype: str
        """
        return self.__n_cliente

    @property
    def num_cliente(self) -> int:
        """
        Método que se encarga y permite obtener el número de Cliente de la Cuenta
        :return: El número de Cliente
        :rtype: int
        """
        return self.__num_cliente
    @property
    def fecha_apertura(self) -> str:
        """
        Método que se encarga de obtener la fecha de apertura de la Cuenta
        :return:Fecha de apertura de la Cuenta
        :rtype: str
        """
        return self.__fecha_apertura

    @property
    def num_sucursal(self) -> int:
        """
        Método que se encarga de obtener el número de sucursal de la Cuenta del cliente.
        :return:El número de sucursal de la Cuenta
        :rtype: int
        """
        return self.__num_sucursal
    @property
    def estado(self) -> str:
        """
        Método para obtener el estado donde se ubica la sucursal.
        :return: El estado donde se ubica la sucursal.
        :rtype: str
        """
        return self.__estado
    @property
    def correo(self) -> str:
        """
        Método para obtener el correo electrónico del la cuenta del cliente.
        :return: El correo electrónico del cliente
        :rtype: str
        """
        return self.__correo
    @property
    def telefono(self) -> str:
        """
        Método que se encarga para obtener el número de teléfono del Cliente de la Cuenta.
        :return: El teléfono del Cliente de la Cuenta
        :rtype: int
        """
        return self.__telefono

    #Agregar los setters
    @n_cliente.setter
    def n_cliente(self, n_cliente: str):
        """
        Método para establecer el nombre del cliente de la Cuenta.
        :param n_cliente: El nombre del cliente de la Cuenta
        """
        if not isinstance(n_cliente, str) or not n_cliente.strip():
            raise ValueError("El nombre del cliente de la cuenta no puede estar vacío")
        self.__n_cliente = n_cliente

    @num_cliente.setter
    def num_cliente(self, num_cliente: int):
        """
        Método para establecer el número del cliente de la cuenta del cliente.
        :param num_cliente: El número de cliente de la Cuenta
        """
        self.__num_cliente = num_cliente if num_cliente > 0 else abs(num_cliente)

    @fecha_apertura.setter
    def fecha_apertura(self, fecha_apertura: str):
        """
        Método para establecer la fecha de apertura de la cuenta del Cliente.
        :param fecha_apertura: La fecha de apertura de la Cuenta
        """
        try:
            self.__fecha_apertura = datetime.strptime(fecha_apertura, "%d-%m-%Y").date()
        except ValueError:
            raise ValueError("La fecha {} no corresponde con el formato "
                  "dd-mm-yyyy.".format(fecha_apertura))
        self.__fecha_apertura = fecha_apertura

    @num_sucursal.setter
    def num_sucursal(self, num_sucursal: int):
        """
        Método para establecer el número de sucursal de la Cuenta del Cliente.
        :param num_sucursal: El número de sucursal de la Cuenta
        """
        if not (1 <= num_sucursal <=6) :
            raise ValueError("Esta sucursal no existe.")
        self.__num_sucursal = num_sucursal

    @estado.setter
    def estado(self, estado: str): #Definimos una lista con todos los estados de México para verificar que el usuario escoga un estado real.
        """
        Método para establecer el estado donde se ubica la sucursal.
        :param estado: Estado donde se ubica la sucursal.
        """
        estados_validos = [
            "Guerrero",
            "Hidalgo",
            "Jalisco",
            "Morelos",
            "Puebla",
            "Tlaxcala",]
        if estado not in estados_validos:
            raise ValueError(f"{estado} no es un estado de la república mexicana.")
        self.__estado = estado

    @correo.setter
    def correo(self, correo: str):
        """
        Método para establecer el correo electrónico del cliente de la cuenta.
        :param correo: El corre electrónico del cliente.
        """
        if validate_email(correo):  # Si devuelve True el correo es ok
            self.__correo = correo
        else:  # El correo no es válido, se define un correo genérico
            print("El correo no es válido!"
                  "Se definió el correo: correo@dominio.com")
            self.__correo = "correo@dominio.com"

    @telefono.setter
    def telefono(self, telefono: str):
        if not isinstance(telefono, (str)) or len(telefono) != 10:
            raise ValueError("El número de teléfono debe ser de 10 dígitos.")
        self.__telefono = telefono

    @abstractmethod
    def retirar(self, monto: float):
        """Método abstracto para retirar dinero. Debe ser implementado por las subclases concretas."""
        pass

    def __str__(self):
        """
        Método que nos permite imprimir la  Cuenta en formato cadena.
        :return: La Cuenta en formato cadena
        :rtype: str
        """
        return "Cuenta:: Cliente: {} | # de cliente: {} | Fecha de apertura: {} | " \
        "Sucursal: {} | Estado: {} | Email: {} " "| Teléfono: {} ".format(self.n_cliente,
                                                                          self.num_cliente, self.fecha_apertura, self.num_sucursal, 
                                                                          self.estado, self.correo, self.telefono)

    def __iter__(self):
        """
        Método que devuelve una representación iterable de un objeto
        :return: La representación iterable de un objeto Cuenta
        :rtype: iterable
        """
        return iter(["C", self.n_cliente, self.num_cliente, self.fecha_apertura, self.num_sucursal,self.estado, self.correo, self.telefono])

    def __llave(self) -> tuple:
        """
        Método privado que nos permite obtener la llave de un objeto Cuenta.
        :return: Una tuple con los atributos de la Cuenta
        :rtype: tuple
        """
        return self.__n_cliente, self.__num_cliente, self.__fecha_apertura, self.__num_sucursal, self.__estado, self.__correo, self.__telefono

    def __hash__(self) -> int:
        """
        Método que llama internamente a la función hash() para obtener el valor hash del objeto Cuenta.
        :return: Un valor entero que corresponde al hash del objeto Cuenta
        :rtype: int
        """
        return hash(self.__llave())

    def __eq__(self, otro) -> bool:
        """
        Método que permite comparar dos Cuentas para saber si son iguales.
        :param otro: La otra Cuenta para comparar.
        :return: bool
        """
        respuesta =False
        if isinstance(otro, Cuenta):
            respuesta = self.__llave() == otro.__llave()
        return respuesta
    
    def a_dict(self):
        return {
            "tipo": self.__class__.__name__,
            "n_cliente": self.__n_cliente,
            "num_cliente": self.__num_cliente,
            "fecha_apertura": self.fecha_apertura,
            "num_sucursal": self.__num_sucursal,
            "estado": self.__estado,
            "correo": self.__correo,
            "telefono": self.__telefono
        }
