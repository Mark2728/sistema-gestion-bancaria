# Programa: CuentaC.py
# Objetivo: Programa que va a permitir definir la subclase Cuentas de Crédito
# Autor: -Carolina Flores Zarraga
#-Ivana Martinez Hernandez
#-David Enrique Ortiz Gonzalez
#-Marcos Pérez Almazán

from Cuenta import Cuenta
from datetime import datetime # Valída las fechas
class CuentaC(Cuenta):
    def __init__(self, n_cliente: str, num_cliente: int, num_tarjeta: str, imp_credito: float, mon_credito: float, fecha_apertura: str, fecha_pago: str, fecha_ven: str, num_sucursal: int, estado: str, correo: str, telefono: str):
        """
        Método constructor para una Cuenta de Credito
        :param n_cliente: El nombre del cliente de la Cuenta
        :param num_cliente: El número del cliente de la Cuenta
        :param num_tarjeta: El numero de tarjeta (4 digitos).
        :param imp_credito: El importe de crédito.
        :param mon_credito: El monto de crédito usado.
        :param fecha_apertura:  La fecha de apertura de la Cuenta  en str con formato dd-mm-yyyy.
        :param fecha_pago: La fecha de pago.
        :param fecha_ven La fecha de vencimiento de la tarjeta.
        :param num_sucursal: El número de sucursal de la Cuenta
        :param estado: El estado de la Cuenta.
        :param correo: El correo electrónico del cliente de la Cuenta.
        :param telefono: El teléfono del cliente de la Cuenta.
        """
        super().__init__(n_cliente, num_cliente, fecha_apertura, num_sucursal, estado, correo, telefono)
        if len(num_tarjeta) != 4:
            raise ValueError("El número de la tarjeta debe ser de 4 dígitos.")
        self.__num_tarjeta = num_tarjeta
        if not isinstance(imp_credito, (int, float)) or imp_credito < 0:
            raise ValueError("El importe de crédito debe de ser un numero positivo o cero.")
        self.__imp_credito = imp_credito
        if not isinstance(mon_credito, (int, float)) or mon_credito < 0:
            raise ValueError("El monto de crédito debe de ser un numero positivo o cero.")
        self.__mon_credito = mon_credito
        try:
            self.__fecha_pago = datetime.strptime(fecha_pago, "%d-%m-%Y").date()
        except ValueError:
            print("La fecha {} no corresponde con el formato "
                  "dd-mm-yyyy.".format(fecha_pago))
        self.__fecha_pago = self.__fecha_pago.strftime("%d-%m-%Y")
        try:
            self.__fecha_ven = datetime.strptime(fecha_ven, "%d-%m-%Y").date()
        except ValueError:
            print("La fecha {} no corresponde con el formato "
                  "dd-mm-yyyy.".format(fecha_ven))
        self.__fecha_ven = self.__fecha_ven.strftime("%d-%m-%Y")

    # Definimos los metodos getters y setters para el número de tarjeta, importe de crédito, monto de crédito usado, fecha de pago y la fecha de vencimiento de la tarjeta.
    #Definimos los métodos Get.
    @property
    def num_tarjeta(self):
        """
        Método que permite obtener el número de la tarjeta del cliente.
        :return: El número de tarjeta del cliente.
        :rtype: str
        """
        return self.__num_tarjeta

    @property
    def imp_credito(self):
        """
        Método que se encarga de obtener el importe de crédito en la tarjeta del cliente.
        :return: El saldo de la tarjeta.
        :rtype: str
        """
        return self.__imp_credito

    @property
    def mon_credito(self)  -> float:
        """
        Método que regresa el monto de crédito utilizado en la tarjeta del cliente.
        :return: El monto de crédito.
        :rtype: str
        """
        return self.__mon_credito

    @property
    def fecha_pago(self):
        """
        Método que regresa la fecha de pago de la tarjeta del cliente.
        :return: La fecha de pago.
        :rtype: str
        """
        return self.__fecha_pago

    @property
    def fecha_ven(self):
        """
        Método que regresa la fecha de vencimiento de la tarjeta.
        :return: La fecha de vencimiento.
        :rtype: str
        """
        return self.__fecha_ven

    #Definimos los métodos Setters.
    @num_tarjeta.setter
    def num_tarjeta(self, num_tarjeta: str):
        """
        Método que permite establecer el número de la tarjeta de un cliente
        :param num_tarjeta: El numero de la tarjeta del cliente.
        """
        if len(num_tarjeta) != 4:
            raise ValueError("El número de la tarjeta debe ser de 4 dígitos.")
        self.__num_tarjeta = num_tarjeta

    @imp_credito.setter
    def imp_credito(self, imp_credito: float):
        """
        Método que permite establecer el crédito de la tarjeta de un cliente.
        :param imp_credito: Crédito de la tarjeta.
        """
        if not isinstance(imp_credito, (int, float)) or imp_credito < 0:
            raise ValueError("El importe de crédito debe de ser un numero positivo o cero.")
        self.__imp_credito = imp_credito

    @mon_credito.setter
    def mon_credito(self, mon_credito: float):
        """
        Método que permite establecer el monto de crédito usado de la tarjeta de un cliente.
        :param mon_credito: Monto de crédito usado de la tarjeta.
        """
        if not isinstance(mon_credito, (int, float)) or mon_credito < 0:
            raise ValueError("El monto de crédito debe de ser un numero positivo o cero.")
        self.__mon_credito = mon_credito

    @fecha_pago.setter
    def fecha_pago(self, fecha_pago: str):
        """
        Método que permite establecer la fecha de pago de la tarjeta de un cliente.
        :param fecha_pago: Fecha de pago de la tarjeta.
        """
        try:
            self.__fecha_pago = datetime.strptime(fecha_pago, "%d-%m-%Y").date()
        except ValueError:
            print("La fecha {} no corresponde con el formato "
                  "dd-mm-yyyy.".format(fecha_pago))
        self.__fecha_pago = fecha_pago

    @fecha_ven.setter
    def fecha_ven(self, fecha_ven: str):
        """
        Método que permite establecer la fecha de vencimiento de la tarjeta de un cliente.
        :param fecha_ven: Fecha de vencimiento de la tarjeta.
        """
        try:
            self.__fecha_ven = datetime.strptime(fecha_ven, "%d-%m-%Y").date()
        except ValueError:
            print("La fecha {} no corresponde con el formato "
                  "dd-mm-yyyy.".format(fecha_ven))
        self.__fecha_ven = fecha_ven

    def retirar(self, monto:float):
        """
        Método que permite a un cliente realizar un retiro (avance de efectivo).
        Aumenta la deuda (el monto a retira) y agrega una comisión del 5%
        :param monto: La cantidad de efectivo o dinero a retira.
        """
        if monto <= 0:
            raise ValueError("El monto debe ser positivo.")
        monto_con_comision = monto * 1.05
        if(self.__mon_credito + monto_con_comision) <= self.__imp_credito: #Ya que como no tenemos un límite de credito el cual sería lo mejor, utilizaremos imp_credito.
            self.__mon_credito += monto_con_comision
            print(f"Retiro de crédito exitoso.\nCargo total(incluye la comisión 5%): ${monto_con_comision}")
            print(f"El nuevo monto utilizado: ${self.__mon_credito}")
        else:
            raise ValueError(f"Limite de crédito insuficiente para realizar la operación")

    def realizar_pago_tarjeta(self, monto_pago:float):
        """
        Método que permite realizar un pago a ala tarjeta de crédito para reducir la deuda.
        Aplicando una penalización del 8% sobre el restante si al realizar el pago no es completo.
        :param monto_pago: La cantidad de dinero que el cliente pagará.
        """
        if monto_pago <= 0:
            raise ValueError("El monto a pagar debe ser positivo.")
        if monto_pago > self.__mon_credito:
            print(f"El pago excede a deuda. \nSe tomará ${self.__mon_credito:,.2f}. para liquidar la deuda.")
            monto_pago = self.__mon_credito
        deuda_anterior = self.__mon_credito
        self.__mon_credito -= monto_pago
        if self.__mon_credito > 0: # Si el pago no ha sido cubierto por completo
            penalizacion =self.__mon_credito * 0.08
            self.__mon_credito += penalizacion
            print(f"Pago recibido. \nDeuda restate: ${deuda_anterior - monto_pago:,.2f}.")
            print(f"Se aplicó la penalización del 8% sobre el restante: ${penalizacion:,.2f}.")
        else:
            print("¡Pago completo realizado! \nLa deuda ha sido liquidada.")
        print(f"Nuevo monto utilizado: ${self.__mon_credito:,.2f}")

    def __str__(self):
        """
        Método para imprimir una CuentaC en formato cadena.
        :return: Una CuentaC en formato cadena.
        :rtype: str
        """
        return "Cuenta de Crédito: Cliente: {} | # de cliente: {} | # de tarjeta: {} " \
        "| Importe de crédito: ${} | Monto de crédito utilizado: ${} | Fecha de apertura: {} " \
        "| Fecha de pago: {} | Fecha de vencimiento: {} | Sucursal: {} | Estado: {} | Email: {} " \
        "| Teléfono: {}".format(super().n_cliente, super().num_cliente, self.num_tarjeta, self.imp_credito, 
                                self.mon_credito, super().fecha_apertura, self.fecha_pago, self.fecha_ven, 
                                super().num_sucursal, super().estado, super().correo, super().telefono)

    def __iter__(self):
        """
        Método que devuelve una representación iterable del objeto.
        :return: Una representación iterable de la CuentaC.
        :rtype: iterable
        """
        return iter("C", super().n_cliente, super().num_cliente, self.__num_tarjeta, self.__imp_credito, self.__mon_credito, super().fecha_apertura, self.__fecha_pago, self.__fecha_ven, super().num_sucursal, super().estado, super().correo, super().telefono)

    def __llave(self) -> tuple:
        """
        Método privado que nos permite obtener la llave de un objeto CuentaC.
        :return: Una tuple con los atributos de la CuentaC.
        :rtype: tuple
        """
        return super().n_cliente, super().num_cliente, self.__num_tarjeta, self.__imp_credito, self.__mon_credito, super().fecha_apertura, self.__fecha_pago, self.__fecha_ven, super().num_sucursal, super().estado, super().correo, super().telefono

    def __hash__(self) -> int:
        """
        Método que llama internamente a la función hash() para obtener el valor hash del objeto CuentaC.
        :return: Un valor entero que corresponde al hash del objeto CuentaC.
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
        if isinstance(otro, CuentaC):
            respuesta = self.__llave() == otro.__llave()
        return respuesta
    
    def a_dict(self):
        return {
            "tipo": self.__class__.__name__,
            "n_cliente": super().n_cliente,
            "num_cliente": super().num_cliente,
            "num_tarjeta": self.__num_tarjeta,
            "imp_credito": self.__imp_credito,
            "mon_credito": self.__mon_credito,
            "fecha_apertura": super().fecha_apertura,
            "fecha_pago": self.fecha_pago,
            "fecha_ven": self.fecha_ven,
            "num_sucursal": super().num_sucursal,
            "estado": super().estado,
            "correo": super().correo,
            "telefono": super().telefono
        }
