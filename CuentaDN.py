# Programa: CuentaDN.py
# Objetivo: Programa que va a permitir definir la subclase Cuentas de Nomina
# Autor: -Carolina Flores Zarraga
#-Ivana Martinez Hernandez
#-David Enrique Ortiz Gonzalez
#-Marcos Pérez Almazán

from Cuenta import Cuenta
from locale import currency, setlocale, LC_MONETARY
class CuentaDN(Cuenta):
    def __init__(self, n_cliente: str, num_cliente: int, num_cuenta: int, saldo: float, fecha_apertura: str, num_sucursal: int, estado: str, correo: str, telefono: str):
        """
        Método constructor para una Cuenta con Débito y Nomina.
        :param n_cliente: El nombre del cliente de la Cuenta
        :param num_cliente: El número del cliente de la Cuenta
        :param fecha_apertura:  La fecha de apertura de la Cuenta  en str con formato dd-mm-yyyy.
        :param num_sucursal:El número de sucursal de la Cuenta
        :param estado: El estado de la Cuenta.
        :param correo: El correo electrónico del cliente de la Cuenta.
        :param telefono: El teléfono del cliente de la Cuenta.
        :param num_cuenta: El numero de Cuenta.
        :param saldo:  El saldo de la Cuenta.
        """
        super().__init__(n_cliente, num_cliente, fecha_apertura, num_sucursal, estado, correo, telefono)
        self.__num_cuenta = num_cuenta if num_cuenta > 0 else abs(num_cuenta)
        if not isinstance(saldo, (int, float)) or saldo < 0:
            raise ValueError("El saldo debe de ser un numero positivo o cero.")
        self.__saldo = saldo

    # Definimos los metodos getters y setters para número de cuenta y saldo.
    #Definimos los métodos Get.
    @property
    def num_cuenta(self):
        """
        Método que permite obtener el número de Cuenta del cliente.
        :return: El número de Cuenta del cliente.
        :rtype: int
        """
        return self.__num_cuenta

    @property
    def saldo(self) -> float:
        """
        Método que se encarga de obtener el total del Saldo que dispone el cliente en su Cuenta
        :return: El saldo de la Cuenta.
        :rtype: float
        """
        return self.__saldo

    #Definimos los métodos Setters.
    @num_cuenta.setter
    def num_cuenta(self, num_cuenta: int):
        """
        Método que permite establecer el número de cuenta de un cliente
        :param num_cuenta: El numero de cuenta del cliente.
        """
        self.__num_cuenta = num_cuenta if num_cuenta > 0 else abs(num_cuenta)

    @saldo.setter
    def saldo(self, saldo: float):
        """
        Método que permite establecer el saldo de la Cuenta de un cliente.
        :param saldo: Saldo de la Cuenta.
        """
        if not isinstance(saldo, (int, float)) or saldo < 0:
            raise ValueError("Saldo debe de ser un numero positivo o cero.")
        self.__saldo = float(saldo)

    def depositar(self, monto:float):
        """
        Mètodo que permite depositar un monto a la cuenta, incrementando el saldo.
        Este es un método general o estándar que usara la cuenta de Débito
        :param monto: La cantidad a depositar, laa cual debe ser positiva.
        """
        if monto <= 0:
            raise ValueError("El monto a depositar debe ser positivo")
        self.__saldo += monto
        print(f"Depósito exitoso. Nuevo saldo: ${self.saldo:.2f}")

    def retirar(self, monto: float):
        """Método que permite retirar un monto de la cuneta, así decreciendo el saldo de la cuenta.
         Solo si existen los fondos suficientes
         :param monto: La cantidad a retirar
         """
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser positivo")
        if self.__saldo >= monto:
            self.__saldo -= monto
            print(f"Retiro fue exitoso: ${self.saldo:.2f}")
        else:
            raise ValueError("Fondos insuficientes para realizar esta operación")


    def __str__(self):


        """
        Método para imprimir una CuentaDN en formato cadena.
        :return: Una CuentaDN en formato cadena.
        :rtype: str
        """
        setlocale(LC_MONETARY, "en_US")
        return super().__str__() + \
            " | Numero de Cuenta: {} | Saldo: {}".format(self.num_cuenta, currency(self.saldo, grouping=True))

    def __iter__(self):
        """
        Método que devuelve una representación iterable del objeto.
        :return: Una representacion iterable de la CuentaDN.
        :rtype: iterable
        """
        return iter("DN", super().n_cliente, super().num_cliente, self.num_cuenta, self.saldo, super().fecha_apertura, super().num_sucursal, super().estado, super().correo,super().telefono)

    def __llave(self) -> tuple:
        """
        Método privado que nos permite obtener la llave de un objeto CuentaDN.
        :return: Una tuple con los atributos de la CuentaDN.
        :rtype: tuple
        """
        return super().n_cliente, super().num_cliente, self.__num_cuenta, self.__saldo, super().fecha_apertura, super().num_sucursal, super().estado, super().correo,super().telefono

    def __hash__(self) -> int:
        """
        Método que llama internamente a la función hash() para obtener el valor hash del objeto CuentaDN.
        :return: Un valor entero que corresponde al hash del objeto CuentaDN
        :rtype: int
        """
        return hash(self.__llave())

    def __eq__(self, otra) -> bool:
        """
        Método que permite comparar dos Cuentas para saber si son iguales.
        :param otra: La otra CuentaDN para comparar.
        :return: bool
        """
        respuesta =False
        if isinstance(otra, CuentaDN):
            respuesta = self.__llave() == otra.__llave()
        return respuesta
    
    def a_dict(self):
        return {
            "tipo": self.__class__.__name__,
            "n_cliente": super().n_cliente,
            "num_cliente": super().num_cliente,
            "num_cuenta": self.__num_cuenta,
            "saldo": self.__saldo,
            "fecha_apertura": super().fecha_apertura,
            "num_sucursal": super().num_sucursal,
            "estado": super().estado,
            "correo": super().correo,
            "telefono": super().telefono
        }
