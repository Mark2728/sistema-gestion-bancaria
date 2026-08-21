# Programa: CuentaN.py
# Objetivo: Programa que va a permitir definir la subclase Cuentas de Débito
# Autor: -Carolina Flores Zarraga
#-Ivana Martinez Hernandez
#-David Enrique Ortiz Gonzalez
#-Marcos Pérez Almazán

from CuentaDN import CuentaDN
from datetime import datetime # Valída las fechas

class CuentaN(CuentaDN):
    def __init__(self, n_cliente: str, num_cliente: int, num_cuenta: int, saldo: float, fecha_apertura: str, fecha_dep:str, num_sucursal: int, estado: str, correo: str, telefono: str, rfc_empresa: str, n_empresa: str):
        """
        Método constructor para una cuenta de Nómina.
        :param n_cliente: El nombre del cliente de la Cuenta.
        :param num_cliente: El número del cliente asociado con la Cuenta.
        :param num_cuenta: El número de Cuenta del cliente.
        :param saldo: El saldo de la Cuenta.
        :param fecha_apertura:  La fecha de apertura de la Cuenta  en str con formato dd-mm-yyyy.
        :param num_sucursal:El número de sucursal de la Cuenta.
        :param estado: El estado donde se ubica la sucursal.
        :param correo: El correo electrónico del cliente de la Cuenta.
        :param telefono: El teléfono del cliente de la Cuenta.
        :param rfc_empresa: El RFC de la empresa del cliente.
        :param n_empresa: El nombre de la empresa del cliente.
        :param fecha_dep: La fecha de deposito de la nómina.
        """
        #Llamamos a la superclase (CuentaDN) el cual es el constructor
        super().__init__(n_cliente, num_cliente, num_cuenta, saldo, fecha_apertura, num_sucursal, estado, correo, telefono)
        #Aquí colocamos el nuevo atributo qeu pertenece a la clase de Nómina.
        try:
            self.__fecha_dep = datetime.strptime(fecha_dep, "%d-%m-%Y").date()
        except ValueError:
            raise ValueError(f"La fecha de depósito {fecha_dep} no cumple con el formato solicitado (dd-mm-yyyy)")
        self.__fecha_dep = self.__fecha_dep.strftime("%d-%m-%Y")
        self.__rfc_empresa = rfc_empresa
        self.__n_empresa = n_empresa

    #Métodos GET Y SET.
    #Colocamos el método getter
    @property
    def rfc_empresa(self) -> str:
        """
        Método que permite obtener el RFC de la empresa donde trabaja el cliente.
        :param self: El RFC de la empresa donde trabaja el cliente.
        :type: str
        """
        return self.__rfc_empresa

    @property
    def n_empresa(self) -> str:
        """
        Método que permite obtener el nombre de la empresa donde trabaja el cliente.
        :param self: El nombre de la empresa donde trabaja el cliente.
        :type: str
        """
        return self.__n_empresa

    @property
    def fecha_dep(self) -> str:
        """
        Método que permite obtener la fecha de depósito de la nómina.
        :param self: La fecha de depósito de la nómina.
        :type: str
        """
        return self.__fecha_dep
    #Colocamos el método setter
    @rfc_empresa.setter
    def rfc_empresa(self, rfc_empresa: str):
        """
        Método que permite establecer el RFC de la empresa donde trabaja el cliente.
        :param rfc_empresa: El RFC de la empresa.
        :return: str
        """
        self.__rfc_empresa = rfc_empresa

    @n_empresa.setter
    def n_empresa(self, n_empresa: str):
        """
        Método que permite establecer el nombre de la empresa donde trabaja el cliente.
        :param n_empresa: El nombre de la empresa.
        :return: str
        """
        self.__n_empresa = n_empresa

    @fecha_dep.setter
    def fecha_dep(self, fecha_dep: str):
        """
        Método que permite establecer la fecha de depósito de nómina.
        :param fecha_dep: La fecha de depósito de la nómina.
        :return: str
        """
        try:
            self.__fecha_dep = datetime.strptime(fecha_dep, "%d-%m-%Y").date()
        except ValueError:
            raise ValueError(f"La fecha de depósito {fecha_dep} no cumple con el formato solicitado (dd-mm-yyyy)")
        self.__fecha_dep = fecha_dep

    def depositar(self, monto: float):
        """
        Sobreescribimos este método heredado de CuentaDN. En donde esta operación esta prohibida para cuentas de nómina.
        Por lo que al método a utilizar sera recibir_pago_nómina.
        Entonces hacemos que genere un error y no permita la operación
        """
        raise PermissionError("El depósito directo por un cliente no esta permitido en la Cuenta de Nómina\
                              Para realizar esta opción utilize registrar Pago de Nómina.")

    def recibir_pago_nomina(self, monto: float, rfc_empresa_dep: str):
        """
        Método que se encarga exclusivamente para que la empresa autorizada en este caso la Institución deposite la Nómina
        Valida que el RFC de la empresa que deposita coincida con el de la cuenta.
        :param monto: El monto de la Nómina a depositar
        :param rfc_empresa_dep: El RFC de la empresa.
        """
        if rfc_empresa_dep.upper() != self.rfc_empresa.upper():
            raise ValueError(f"La empresa con RFC {rfc_empresa_dep} no esta autorizado")
        if monto <= 0:
            raise ValueError("El monto de la nómina debe ser positivo")
        self.__saldo += monto
        print(f"El pago de la Nómina de {self.n_empresa} ah sido recibido. /"
              f"Nuevo saldo: ${self.__saldo:,.2f}")

    def __str__(self):
        """
        Método para imprimir una CuentaN (Cuenta de Nómina) en formato cadena.
        :return: Una CuentaN en formato cadena.
        :rtype: str
        """
        return "Cuenta de Nómina: Cliente: {} | # de cliente: {} | # de cuenta: {}" \
        "| Saldo: ${} | Fecha de apertura: {} Fecha de depósito: {} | Sucursal: {} " \
        "| Estado: {} | Email: {} | Teléfono: {} | RFC de la empresa: {} " \
        "| Empresa: {}".format(super().n_cliente, super().num_cliente, super().num_cuenta, 
                               super().saldo, super().fecha_apertura, self.fecha_dep, 
                               super().num_sucursal, super().estado, super().correo, 
                               super().telefono, self.rfc_empresa, self.n_empresa)

    def __iter__(self):
        """
        Método que devuelve una representación iterable del objeto.
        :return: Una representación iterable de la CuentaN (Cuenta de Nómina).
        :rtype: iterable
        """
        return iter("N", super().n_cliente, super().num_cliente, super().num_cuenta, super().saldo, super().fecha_apertura, self.fecha_dep, super().num_sucursal, super().estado, super().correo, super().telefono, self.rfc_empresa, self.n_empresa)

    def __llave(self) -> tuple:
        """
        Método privado que nos permite obtener la llave de un objeto CuentaN.
        :return: Una tuple con los atributos de la CuentaN (Cuenta de Nómina).
        :rtype: tuple
        """
        return super().n_cliente, super().num_cliente, super().num_cuenta, super().saldo, super().fecha_apertura, self.__fecha_dep, super().num_sucursal, super().estado, super().correo,super().telefono, self.__rfc_empresa, self.__n_empresa

    def __hash__(self) -> int:
        """
        Método que llama internamente a la función hash() para obtener el valor hash del objeto CuentaN (Cuenta de Nómina).
        :return: Un valor entero que corresponde al hash del objeto CuentaN (Cuenta de Nómina).
        :rtype: int
        """
        return hash(self.__llave())

    def __eq__(self, otro) -> bool:
        """
        Método que permite comparar dos Cuentas para saber si son iguales.
        :param otro: La otra CuentaN para comparar.
        :return: bool
        """
        respuesta =False
        if isinstance(otro, CuentaN):
            respuesta = self.__llave() == otro.__llave()
        return respuesta
    
    def a_dict(self):
        return {
            "tipo": self.__class__.__name__,
            "n_cliente": super().n_cliente,
            "num_cliente": super().num_cliente,
            "num_cuenta": super().num_cuenta,
            "saldo": super().saldo,
            "fecha_apertura": super().fecha_apertura,
            "fecha_dep": self.fecha_dep,
            "num_sucursal": super().num_sucursal,
            "estado": super().estado,
            "correo": super().correo,
            "telefono": super().telefono,
            "rfc_empresa": self.__rfc_empresa,
            "n_empresa": self.__n_empresa
        }
