# Programa: CuentaD.py
# Objetivo: Programa que va a permitir definir la subclase Cuentas de Débito
# Autor: -Carolina Flores Zarraga
#-Ivana Martinez Hernandez
#-David Enrique Ortiz Gonzalez
#-Marcos Pérez Almazán


from CuentaDN import CuentaDN
from datetime import datetime # Valída las fechas

class CuentaD(CuentaDN):
    def __init__(self, n_cliente: str, num_cliente: int, num_cuenta: int, saldo: float, fecha_apertura: str, fecha_corte: str, num_sucursal: int, estado: str, correo: str, telefono: str):
        """
        Método constructor para una cuenta de Débito.
        :param n_cliente: El nombre del cliente de la Cuenta
        :param num_cliente: El número del cliente de la Cuenta
        :param fecha_apertura:  La fecha de apertura de la Cuenta  en str con formato dd-mm-yyyy.
        :param num_sucursal:El número de sucursal de la Cuenta
        :param estado: El estado de la Cuenta.
        :param correo: El correo electrónico del cliente de la Cuenta.
        :param telefono: El teléfono del cliente de la Cuenta.
        :param num_cuenta: El numero de Cuenta.
        :param saldo:  El saldo de la Cuenta.
        :param fecha_corte: La fecha de corte a la Cuenta.
        """
        #Llamamos a la superclase (CuentaDN) el cual es el constructor
        super().__init__(n_cliente, num_cliente, num_cuenta, saldo, fecha_apertura, num_sucursal, estado, correo, telefono)
        #Aquí colocamos el nuevo atributo qeu pertenece a la clase de Débito
        try:
            self.__fecha_corte = datetime.strptime(fecha_corte, "%d-%m-%Y").date()
        except ValueError:
            raise ValueError(f"La fecha de corte{fecha_corte} no cumple con el formato solicitado (dd-mm-yyyy)")
        self.__fecha_corte = self.__fecha_corte.strftime("%d-%m-%Y")
        #Métodos GET Y SET.
        #Colocamos el método setter
    @property
    def fecha_corte(self) -> str:
        """
        Método que permite obtener la fecha de corte de la cuenta de Débito
        :param self: La fecha de corte de la Cuenta de Debito
        :type: str
        """
        return self.__fecha_corte
    #Colocamos el método getter
    @fecha_corte.setter
    def fecha_corte(self, fecha_corte: str):
        """
        Método que permite establecer la fecha de corte de la Cuenta de Débito.
        :param self: La fecha de corte de la Cuenta de Debito
        :param fecha_corte:
        :return:
        """
        try:
            self.__fecha_corte = datetime.strptime(fecha_corte, "%d-%m-%Y").date()
        except ValueError:
            raise ValueError(f"La fecha de corte{fecha_corte} no cumple con el formato solicitado (dd-mm-yyyy)")
        self.__fecha_corte = fecha_corte

    def __str__(self):
        """
        Método para imprimir una CuentaD (Cuenta de Débito) en formato cadena.
        :return: Una CuentaD en formato cadena.
        :rtype: str
        """
        return "Cuenta de Débito: Cliente: {} | # de cliente: {} | # de cuenta: {}" \
        "| Saldo: ${} | Fecha de apertura: {} Fecha de corte: {} | Sucursal: {} " \
        "| Estado: {} | Email: {} | Teléfono: {}".format(super().n_cliente, super().num_cliente, 
                                                         super().num_cuenta, super().saldo, 
                                                         super().fecha_apertura, self.fecha_corte, 
                                                         super().num_sucursal, super().estado, 
                                                         super().correo,super().telefono)

    def __iter__(self):
        """
        Método que devuelve una representación iterable del objeto.
        :return: Una representación iterable de la CuentaD (Cuenta de Crédito).
        :rtype: iterable
        """
        return iter("D", super().n_cliente, super().num_cliente, super().num_cuenta, super().saldo, super().fecha_apertura, self.__fecha_corte, super().num_sucursal, super().estado, super().correo,super().telefono)

    def __llave(self) -> tuple:
        """
        Método privado que nos permite obtener la llave de un objeto CuentaDN.
        :return: Una tuple con los atributos de la CuentaD(Cuenta de Débito).
        :rtype: tuple
        """
        return super().n_cliente, super().num_cliente, super().fecha_apertura, self.__fecha_corte, super().num_sucursal, super().estado, super().correo,super().telefono, super().num_cuenta, super().saldo

    def __hash__(self) -> int:
        """
        Método que llama internamente a la función hash() para obtener el valor hash del objeto CuentaD(Cuenta de Débito).
        :return: Un valor entero que corresponde al hash del objeto CuentaD (Cuenta de Débito).
        :rtype: int
        """
        return hash(self.__llave())

    def __eq__(self, otro) -> bool:
        """
        Método que permite comparar dos Cuentas para saber si son iguales.
        :param otro: La otra CuentaDN para comparar.
        :return: bool
        """
        respuesta =False
        if isinstance(otro, CuentaD):
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
            "fecha_corte": self.fecha_corte,
            "num_sucursal": super().num_sucursal,
            "estado": super().estado,
            "correo": super().correo,
            "telefono": super().telefono
        }
