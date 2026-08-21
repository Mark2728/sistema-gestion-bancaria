# Programa: InstitucionBancaria.py
# Objetivo: Programa que va a manejar la funcionalidad del sistema.
# Autor: -Carolina Flores Zarraga
# -Ivana Martinez Hernandez
# -David Enrique Ortiz Gonzalez
# -Marcos Pérez Almazán

from Cuenta import Cuenta
from CuentaD import CuentaD
from CuentaC import CuentaC
from CuentaN import CuentaN
from Ejecutivo import Ejecutivo
import csv # Abrir y leer archivos csv
from datetime import datetime # Manejar fechas
import random # Usado en la creación de números de tarjeta
from validate_email import validate_email # Validación del email

class InstitucionBancaria:
    def __init__(self):
        """
        Método constructor por omisión que permite a la Institución Bancaria definir y leer una lista de Cuentas o Ejecutivos pero ambos son vacías.
        """
        self.__cuentas = []
        self.__ejecutivos = []
        self.__cuentas_borradas = []
        self.__ejecutivos_borrados = []
        self.__ejecutivo_cuenta = {}
        self.__encabezado_cuentas = ["tipo","n_cliente","num_cliente","num_cuenta","num_tarjeta","saldo","imp_credito","mon_credito","fecha_apertura","fecha_pago","fecha_dep","fecha_ven","fecha_corte","num_sucursal","estado","correo","telefono","rfc_empresa","n_empresa"]
        self.__encabezado_ejecutivos = ["num_empleado","rfc","n_empleado","fecha_nac","direccion","telefono","sueldo_m"]
    # Agregamos GETTERS y SETTERS
    # Agregamos GETTERS
    @property
    def cuentas(self):
        """
        Método que permite devolver la lista de Cuentas
        :return: La lista con las cuentas
        :rtype: list
        """
        return self.__cuentas
    
    @property
    def ejecutivos(self):
        """
        Método que permite devolver la lista de Ejecutivos
        :return: La lista con los ejecutivos
        :rtype: list
        """
        return self.__ejecutivos

    @property
    def ejecutivo_cuenta(self):
        """
        Método que permite devolver el diccionario de los Ejecutivos y que tipo de cuenta abrieron
        :return: El diccionario con los Ejecutivos : Cuentas
        :rtype: dict
        """
        return self.__ejecutivo_cuenta
    
    @property
    def encabezado_cuentas(self):
        """
        Método que permite devolver la lista con el encabezado del archivo cuentas.csv
        :return: La lista con el encabezado
        :rtype: list"""
        return self.__encabezado_cuentas
    
    @property
    def encabezado_ejecutivos(self):
        """
        Método que permite devolver la lista con el encabezado del archivo ejecutivos.csv
        :return: La lista con el encabezado
        :rtype: list"""
        return self.__encabezado_ejecutivos
    # Agregamos SETTERS
    @cuentas.setter
    def cuentas(self, cuentas: list):
        """
        Método que permite establecer la lista de Cuentas
        :param cuentas: Una lista de Cuentas para la inicialización
        """
        self.__cuentas = cuentas

    @ejecutivos.setter
    def ejecutivos(self, ejecutivos: list):
        """
        Método que permite establecer la lista de Ejecutivos
        :param ejecutivos: Una lista de Ejecutivos para la inicialización
        :return:
        """
        self.__ejecutivos = ejecutivos

    @ejecutivo_cuenta.setter
    def ejecutivo_cuenta(self, ejecutivo_cuenta: dict):
        """
        Método que permite establecer el diccionario de Ejecutivos : Cuentas
        :param ejecutivo_cuenta: Un Ejecutivo y Cuenta
        :return:
        """
        self.__ejecutivo_cuenta = ejecutivo_cuenta

    @encabezado_cuentas.setter
    def encabezado_cuentas(self, encabezado_cuentas: list):
        """
        Método que permite establecer el encabezado de cuentas.csv
        :param encabezado_cuentas: Una lista
        :return:
        """
        self.__encabezado_cuentas = encabezado_cuentas

    @encabezado_ejecutivos.setter
    def encabezado_ejecutivos(self, encabezado_ejecutivos: list):
        """
        Método que permite establecer el encabezado de ejecutivos.csv
        :param encabezado_ejecutivos: Una lista
        :return:
        """
        self.__encabezado_ejecutivos = encabezado_ejecutivos

    def cargar_cuentas(self):
        """
        Método el cual nos va a permitir leer y cargar a la lista de Cuentas
        """
        try:
            with open("cuentas.csv", encoding="UTF8", newline="",) as file:
                lector = csv.reader(file)
                for fila in lector:
                    if fila[0] == "CuentaD": #Es una Cuenta de Débito
                        self.__cuentas.append(CuentaD(fila[1], int(fila[2]), int(fila[3]), float(fila[5]), fila[8], fila[12], int(fila[13]),
                                                      fila[14], fila[15], fila[16]))
                    elif fila[0] == "CuentaC": #Es una Cuenta de Crédito
                        self.__cuentas.append(CuentaC(fila[1], int(fila[2]), fila[4], float(fila[6]), float(fila[7]), fila[8],
                                                      fila[9], fila[11], int(fila[13]), fila[14], fila[15], fila[16]))
                    elif fila[0] == "CuentaN": #Es una Cuenta de Nómina
                        self.__cuentas.append(CuentaN(fila[1], int(fila[2]), int(fila[3]), float(fila[5]), fila[8], fila[10], int(fila[13]),
                                                      fila[14], fila[15], fila[16], fila[17], fila[18]))
                print(f"El archivo cuentas.csv fue leído exitosamente!")
        except FileNotFoundError:
            print("El archivo cuentas.csv no existe!")
    
    def cargar_ejecutivos(self):
        """
        Método el cual nos va a permitir leer y cargar a la lista de Ejecutivos
        """
        try: # Lee el archivo ejecutivos.csv
            with open("ejecutivos.csv", encoding="UTF8", newline="") as file:
                lector = csv.reader(file)
                next(lector, None)
                for fila in lector:
                    self.__ejecutivos.append(Ejecutivo(int(fila[0]), fila[1], fila[2], fila[3], fila[4], fila[5], float(fila[6])))
                print(f"El archivo ejecutivos.csv fue leído exitosamente!")
        except FileNotFoundError: # Alza un error si no encuentra el archivo
            print("El archivo ejecutivos.csv no existe!")
        tipos = ["Débito", "Crédito", "Nómina"]
        for e in self.__ejecutivos: # Le asigna un tipo de cuenta a cada ejecutivo (cuenta que aperturó)
            c = random.choice(tipos)
            self.__ejecutivo_cuenta[e] = c

    def consultar_cliente(self):
        """
        Método para consultar los clientes por varios medios
        """
        while True: # Despliega el menú
            print("\nIndica el criterio de consulta:")
            print("1. Por número de cliente")
            print("2. Por tipo de cuenta")
            print("3. Por nombre de cliente")
            print("4. Por número de tarjeta (4 dígitos)")
            print("5. Por número de sucursal (1-6)")
            print("6. Por RFC del ejecutivo")
            print("7. Por RFC de la empresa")
            print("8. Por estado de la República Mexicana")
            print("9. Regresar")
            criterio = input("Selecciona el criterio de consulta: ")
            if criterio not in "123456789" or len(criterio) != 1: # Si no se indica un criterio válido vuelve a desplegar el menú
                print("¡No es un criterio de consulta válido!")
                continue
            busqueda = []
            match criterio:
                case "1": # Busqueda por número de cliente
                    while True:
                        try:
                            r = int(input("Ingresa el número de cliente: "))
                            break
                        except ValueError:
                            print("El valor ingresado no es un número")

                    for c in self.__cuentas:
                        if getattr(c, "num_cliente") == r:
                            busqueda.append(c)
                case "2": # Busqueda por tipo de cuenta
                    r = input("Ingresa el tipo de cuenta (Crédito, Débito o Nómina): ").title()
                    for c in self.__cuentas:
                        if r == "Débito" or r == "Debito":
                            if isinstance(c, CuentaD):
                                busqueda.append(c)
                        elif r == "Crédito" or r == "Credito":
                            if isinstance(c, CuentaC):
                                busqueda.append(c)
                        elif r == "Nómina" or r == "Nomina":
                            if isinstance(c, CuentaN):
                                busqueda.append(c)
                case "3": # Busqueda por nombre del cliente
                    r = input("Ingresa el nombre del cliente: ").title()
                    for c in self.__cuentas:
                        if getattr(c, "n_cliente") == r:
                            busqueda.append(c)
                case "4": # Busqueda por número de tarjeta
                    r = input("Ingresa el número de tarjeta de crédito: ")
                    for c in self.__cuentas:
                        if isinstance(c, CuentaC):
                            if getattr(c, "num_tarjeta") == r:
                                busqueda.append(c)
                case "5": # Busqueda por número de sucursal
                    while True:
                        try:
                            r = int(input("Ingresa el número de sucursal (1-6): "))
                            break
                        except ValueError:
                            print(f"El valor ingresado no es un número")

                    for c in self.__cuentas:
                        if getattr(c, "num_sucursal") == r:
                            busqueda.append(c)
                    busqueda = sorted(busqueda, key=lambda cuenta: type(cuenta).__name__)
                case "6": # Busqueda por RFC del ejecutivo
                    r = input("Ingresa el RFC del ejecutivo(a): ").upper()
                    for e in self.__ejecutivos:
                        if getattr(e, "rfc") == r:
                            busqueda.append(e)
                case "7": # Busqueda por RFC de la empresa
                    r = input("Ingresa el RFC de la empresa: ").upper()
                    for c in self.__cuentas:
                        if isinstance(c, CuentaN):
                            if getattr(c, "rfc_empresa") == r:
                                busqueda.append(c)
                case "8": # Busqueda por estado de memexico
                    r = input("Ingresa el estado de la República Mexicana (Hidalgo, Jalisco, Puebla, Guerrero, Morelos, Tlaxcala): ").title()
                    for c in self.__cuentas:
                        if getattr(c, "estado") == r:
                            busqueda.append(c)
                    busqueda = sorted(busqueda, key=lambda cuenta: type(cuenta).__name__)
                case "9": # Regresa al menú anterior
                    break
            if len(busqueda) == 0: # Si la busqueda no dio resultados
                print("Los datos colocados no coinciden con ningun cliente")
            else: # Imprimir los resultados de busqueda
                for res in busqueda:
                    print(res)
    
    def consultar_cuenta(self):
        """
        Método para consultar las cuentas por varios medios
        """
        while True: # Despliega el menú
            print("\nIndica el criterio de consulta:")
            print("1. Por tipo de cuenta y número de sucursal (1-6)")
            print("2. Por número de sucursal (1-6) y rango de saldo")
            print("3. Por fecha de apertura e importe mayor a...")
            print("4. Por número de sucursal (1-6) y RFC de la empresa")
            print("5. Por mes y año de apertura")
            print("6. Regresar")
            criterio = input("Selecciona el criterio de consulta: ")
            if criterio not in "123456" or len(criterio) != 1: # Si no se indica un criterio válido se vuelve a desplegar el menú
                print("¡No es un criterio de consulta válido!")
                continue
            busqueda = []
            match criterio:
                case "1": # Busqueda por tipo de cuenta y número de sucursal
                    r1 = input("Ingresa el tipo de Cuenta (Débito, Crédito o Nómina): ").title()
                    while True:
                        try:
                            r2 = int(input("Ingresa el número de sucursal (1-6): "))
                            break
                        except ValueError:
                            print(f"El valor ingresado no es un número")

                    for c in self.__cuentas:
                        if r1 == "Débito" or r1 == "Debito":
                            if isinstance(c, CuentaD) and getattr(c, "num_sucursal") == r2:
                                busqueda.append(c)
                        elif r1 == "Crédito" or r1 == "Credito":
                            if isinstance(c, CuentaC) and getattr(c, "num_sucursal") == r2:
                                busqueda.append(c)
                        elif r1 == "Nómina" or r1 == "Nomina":
                            if isinstance(c, CuentaN) and getattr(c, "num_sucursal") == r2:
                                busqueda.append(c)
                case "2": # Busqueda por número de sucursal y rango de saldo
                    while True:
                        try:
                            r1 = int(input("Ingresa el número de sucursal (1-6): "))
                            r2 = float(input("Ingresa el saldo mínimo: "))
                            r3 = float(input("Ingresa el saldo máximo: "))
                            break
                        except ValueError:
                            print(f"El valor ingresado no es un número")

                    for c in self.__cuentas:
                        if isinstance(c, CuentaD) or isinstance(c, CuentaN):
                            if getattr(c, "num_sucursal") == r1 and r3 >= getattr(c, "saldo") >= r2:
                                busqueda.append(c)
                    busqueda = sorted(busqueda, key=lambda cuenta: type(cuenta).__name__)
                case "3": # Busqueda por fecha de apertura e importe mayor a un número dado
                    r1 = input("Ingresa la Fecha de apertura (dd-mm-yyyy): ")
                    while True:
                        try:
                            r2 = float(input("Ingresa el importe mayor a... "))
                            break
                        except ValueError:
                            print(f"El valor ingresado no es un número")

                    for c in self.__cuentas:
                        if isinstance(c, CuentaC):
                            if getattr(c, "fecha_apertura") == r1 and getattr(c, "imp_credito") > r2:
                                busqueda.append(c)
                case "4": # Busqueda por número de sucursal y RFC de la empresa
                    while True:
                        try:
                            r1 = int(input("Ingresa el número de sucursal (1-6): "))
                            break
                        except ValueError:
                            print(f"El valor ingresado no es un número")
                    
                    r2 = input("Ingresa el RFC de la empresa: ").upper()
                    for c in self.__cuentas:
                        if isinstance(c, CuentaN):
                            if getattr(c, "num_sucursal") == r1 and getattr(c, "rfc_empresa") == r2:
                                busqueda.append(c)
                case "5": # Busqueda por mes y año de apertura
                    r1 = input("Ingresa el mes de apertura: ")
                    r2 = input("Ingresa el año de apertura: ")
                    for c in self.__cuentas:
                        fecha = getattr(c, "fecha_apertura")
                        if fecha[3:5] == r1 and fecha[6:] == r2:
                            busqueda.append(c)
                    busqueda = sorted(busqueda, key=lambda cuenta: type(cuenta).__name__)
                case "6": # Regresa al menú anterior
                    break
            if len(busqueda) == 0: # Si la busqueda no dio resultados
                print("Los datos colocados no coinciden con ninguna cuenta")
            else: # Imprime los resultados de busqueda
                for res in busqueda:
                    print(res)

    def consultar_ejecutivo(self):
        """
        Método para consultar los ejecutivos por varios médios
        """
        while True: # Despliega el menú
            print("\nIndica el criterio de consulta:")
            print("1. Por nombre del ejecutivo(a)")
            print("2. Por número y rango de sueldo")
            print("3. Por nombre y tipo de cuenta que han abierto")
            print("4. Por día y mes de cumpleaños")
            print("5. Por rango de edad")
            print("6. Por tipo de cuenta que pueden abrir")
            print("7. Regresar")
            criterio = input("Selecciona el criterio de consulta: ")
            if criterio not in "1234567" or len(criterio) != 1: # Si no se indica un criterio de busqueda válido vuelve a desplegar el menú
                print("¡No es un criterio de consulta válido!")
                continue
            busqueda = []
            match criterio:
                case "1": # Busqueda por nombre de ejecutivo
                    r = input("Ingresa el nombre del ejecutivo(a): ").title()
                    for e in self.__ejecutivos:
                        if getattr(e, "n_empleado") == r:
                            busqueda.append(e)
                case "2": # Busqueda por número de ejecutivo y rango de sueldo
                    while True:
                        try:
                            r1 = int(input("Ingresa el número del ejecutivo(a): "))
                            r2 = float(input("Ingresa el sueldo mínimo: "))
                            r3 = float(input("Ingresa el sueldo máximo: "))
                            break
                        except ValueError:
                            print(f"El valor ingresado no es un número")
                    
                    for e in self.__ejecutivos:
                        if getattr(e, "num_empleado") == r1 and r3 >= getattr(e, "sueldo_m") >= r2:
                            busqueda.append(e)
                case "3": # Busqueda por nombre de ejecutivo y tipo de cuenta que abrio
                    r1 = input("Ingresa el nombre del ejecutivo(a): ").title()
                    r2 = input("Ingresa el tipo de cuenta (Débito, Crédito o Nómina): ").title()
                    if r2 == "Debito":
                        r2 = "Débito"
                    elif r2 == "Credito":
                        r2 = "Crédito"
                    elif r2 == "Nomina":
                        r2 = "Nómina"
                    for e in self.__ejecutivo_cuenta:
                        if getattr(e, "n_empleado") == r1 and self.__ejecutivo_cuenta[e] == r2:
                            busqueda.append(e)
                            busqueda.append("Tipo de cuenta abierta: ")
                            busqueda.append(self.__ejecutivo_cuenta[e])
                case "4": # Busqueda por dia y mes de cumpleaños
                    r1 = input("Ingresa el día de cumpleaños: ")
                    r2 = input("Ingresa el mes de cumpleaños: ")
                    for e in self.__ejecutivos:
                        fecha = getattr(e, "fecha_nac")
                        if fecha[:2] == r1 and fecha[3:5] == r2:
                            busqueda.append(e)
                case "5": # Busqueda por rango de edad
                    while True:
                        try:
                            r1 = int(input("Ingresa la edad mínima: "))
                            r2 = int(input("Ingresa la edad máxima: "))
                            break
                        except ValueError:
                            print(f"El valor ingresado no es un número")
                    
                    hoy = datetime.today()
                    for e in self.__ejecutivos:
                        cum = getattr(e, "fecha_nac")
                        fecha_cum = datetime(int(cum[6:]), int(cum[3:5]), int(cum[:2]))
                        edad = hoy.year - fecha_cum.year - ((hoy.month, hoy.day) < (fecha_cum.month, fecha_cum.day))
                        if r2 >= edad >= r1:
                            busqueda.append(e)
                case "6": # Busqueda por tipo de cuenta que puede abrir
                    r1 = input("Ingresa el tipo de cuenta (Débito, Crédito o Nómina): ").title()
                    if r1 == "Debito":
                        r1 = "Débito"
                    elif r1 == "Credito":
                        r1 = "Crédito"
                    elif r1 == "Nomina":
                        r1 = "Nómina"
                    for e in self.__ejecutivo_cuenta:
                        if self.__ejecutivo_cuenta[e] == r1:
                            busqueda.append(e)
                case "7": # Regresa al menú anterior
                    break
            if len(busqueda) == 0: # Si la busqueda no dio resultados
                print("Los datos colocados no coinciden con ningun ejecutivo")
            else: # Imprime los resultados de busqueda
                for res in busqueda:
                    print(res)

    def alta_actualizar_cuenta(self):
        """
        Método para dar de alta una cuenta o actualizar una existente
        """
        while True: # Despliega el menú
            print("\nEscoge una opción:")
            print("1. Dar de alta")
            print("2. Actualizar")
            print("3. Regresar")
            criterio = input("Selecciona la opción deseada: ")
            if criterio not in "123" or len(criterio) != 1: # Si la opción seleccionada no es válida se vuelve a desplegar el menú
                print("¡No es una opción válida!")
                continue
            match criterio:
                case "1": # Da de alta una cuenta
                    while True:
                        tipo = input("Ingresa el tipo de cuenta (Débito, Crédito o Nómina): ").title()
                        if tipo not in {"Débito", "Debito", "Crédito", "Credito", "Nómina", "Nomina"}:
                            print("No es un tipo de cuenta")
                            continue
                        n_cliente = input("Ingresa el nombre del cliente: ").title()
                        if not isinstance(n_cliente, str) or not n_cliente.strip():
                            print("El nombre del cliente de la cuenta no puede estar vacío")
                            continue
                        fecha_apertura = input("Ingresa la fecha de apertura (dd-mm-yyyy): ")
                        correo = input("Ingresa el email: ")
                        if not validate_email(correo):  # Si devuelve True el correo no es válido
                            print("El correo no es válido")
                            continue
                        telefono = input("Ingresa el teléfono (10 dígitos): ")
                        if len(telefono) != 10:
                            print("El número de teléfono debe ser de 10 dígitos.")
                            continue
                        break

                    num_cliente = getattr(self.__cuentas[-1], "num_cliente") + 1
                    num_sucursal = random.randint(1, 6)
                    match num_sucursal:
                        case 1:
                            estado = "Hidalgo"
                        case 2:
                            estado = "Jalisco"
                        case 3:
                            estado = "Puebla"
                        case 4:
                            estado = "Guerrero"
                        case 5:
                            estado = "Morelos"
                        case 6:
                            estado = "Tlaxcala"

                    if tipo == "Débito" or tipo == "Debito":
                        while True:
                            try:
                                num_cuenta = int(input("Ingresa el número de cuenta: "))
                                saldo = float(input("Ingresa el saldo: "))
                            except ValueError:
                                print("El valor ingresado no es un número")
                                continue
                            fecha_corte = input("Ingresa la fecha de corte (dd-mm-yyyy): ")
                            break
                        self.__cuentas.append(CuentaD(n_cliente, num_cliente, num_cuenta, saldo, fecha_apertura, fecha_corte, num_sucursal, estado, correo, telefono))
                    elif tipo == "Crédito" or tipo == "Credito":
                        while True:
                            try:
                                imp_credito = float(input("Ingresa el importe de crédito: "))
                                mon_credito = float(input("Ingresa el monto de crédito: "))
                                if imp_credito < mon_credito:
                                    print("El importe de crédito debe de ser mayor al monto de crédito")
                                    continue
                            except ValueError:
                                print("El valor ingresado no es un número")
                                continue
                            fecha_pago = input("Ingresa la fecha de pago (dd-mm-yyyy): ")
                            fecha_ven = input("Ingresa la fecha de vencimiento (dd-mm-yyyy): ")
                            break
                        unico = False
                        while unico == False:
                            num_tarjeta = random.randint(1000, 9999)
                            unico = True
                            for c in self.__cuentas:
                                if isinstance(c, CuentaC):
                                    if getattr(c, "num_tarjeta") != num_tarjeta and unico == True:
                                        unico = True
                                    else:
                                        unico = False
                        num_tarjeta = str(num_tarjeta)
                        self.__cuentas.append(CuentaC(n_cliente, num_cliente, num_tarjeta, imp_credito, mon_credito, fecha_apertura, fecha_pago, fecha_ven, num_sucursal, estado, correo, telefono))
                    elif tipo == "Nómina" or tipo == "Nomina":
                        while True:
                            try:
                                num_cuenta = int(input("Ingresa el número de cuenta: "))
                                saldo = float(input("Ingresa el saldo: "))
                            except ValueError:
                                print("El valor ingresado no es un número")
                                continue
                            fecha_dep = input("Ingresa la fecha de depósito (dd-mm-yyyy): ")
                            rfc_empresa = input("Ingresa el RFC de la empresa: ")
                            if not rfc_empresa.strip():
                                print("El RFC de la empresa no puede estar vacío")
                                continue
                            n_empresa = input("Ingresa el Nombre de la empresa: ")
                            if not n_empresa.strip():
                                print("El nombre de la empresa no puede estar vacío")
                                continue
                            break
                        self.__cuentas.append(CuentaN(n_cliente, num_cliente, num_cuenta, saldo, fecha_apertura, fecha_dep, num_sucursal, estado, correo, telefono, rfc_empresa, n_empresa))
                    print("Se ha dado de alta la nueva cuenta")

                case "2": # Actualiza una cuenta
                    while True:
                        try:
                            cuenta = int(input("Ingresa la cuenta a actualizar (número de cliente): "))
                            break
                        except ValueError:
                            print("El valor ingresado no es un número")
                    for c in self.__cuentas:
                        if getattr(c, "num_cliente") == cuenta:
                            while True:
                                c.n_cliente = input("Ingresa el nombre del cliente: ").title()
                                if not c.n_cliente.strip():
                                    print("El nombre del cliente no puede estar vacío")
                                    continue
                                c.fecha_apertura = input("Ingresa la Fecha de apertura (dd-mm-yyyy): ")
                                c.correo = input("Ingresa el email: ")
                                if not validate_email(c.correo):  # Si devuelve True el correo no es válido
                                    print("El correo no es válido")
                                    continue
                                c.telefono = input("Ingresa el teléfono (10 dígitos): ")
                                if len(c.telefono) != 10:
                                    print("El número de teléfono debe ser de 10 dígitos.")
                                    continue
                                break
                            if isinstance(c, CuentaD):
                                while True:
                                    try:
                                        c.num_cuenta = int(input("Ingresa el número de cuenta: "))
                                        c.saldo = float(input("Ingresa el saldo: "))
                                    except ValueError:
                                        print("El valor ingresado no es un número")
                                    c.fecha_corte = input("Ingresa la fecha de corte (dd-mm-yyyy): ")
                                    break
                            elif isinstance(c, CuentaC):
                                while True:
                                    try:
                                        c.imp_credito = float(input("Ingresa el importe de crédito: "))
                                        c.mon_credito = float(input("Ingresa el monto de crédito: "))
                                    except ValueError:
                                        print("El valor ingresado no es un número")
                                    c.fecha_pago = input("Ingresa la fecha de pago (dd-mm-yyyy): ")
                                    c.fecha_ven = input("Ingresa el fecha de vencimiento (dd-mm-yyyy): ")
                                    break
                            elif isinstance(c, CuentaN):
                                while True:
                                    try:
                                        c.num_cuenta = int(input("Ingresa el número de cuenta: "))
                                        c.saldo = float(input("Ingresa el saldo: "))
                                    except ValueError:
                                        print("El valor ingresado no es un número")
                                    c.fecha_dep = input("Ingresa la fecha de depósito (dd-mm-yyyy): ")
                                    c.rfc_empresa = input("Ingresa el RFC de la empresa: ").upper()
                                    if not c.rfc_empresa.strip():
                                        print("El nombre del cliente no puede estar vacío")
                                        continue
                                    c.n_empresa = input("Ingresa el nombre de la empresa: ").title()
                                    if not c.n_empresa.strip():
                                        print("El nombre del cliente no puede estar vacío")
                                        continue
                                    break
                    print("Se ha actualizado la cuenta")
                    with open("cuentas.csv", "w", encoding="UTF8", newline="",) as file:
                        escritor = csv.DictWriter(file, fieldnames=self.encabezado_cuentas)
                        escritor.writeheader()
                        for obj in self.__cuentas:
                            escritor.writerow(obj.a_dict())
                        print("Se ha registrado la cuenta actualizada en cuentas.csv")

                case "3": # Regresa al menú anterior
                    break

    def registrar(self):
        """
        Método para registrar las nuevas cuentas en cuentas.csv
        """
        with open("cuentas.csv", "w", encoding="UTF8", newline="",) as file: # Abre el archivo cuentas.csv y sobreescribe con la lista actualizada
            escritor = csv.DictWriter(file, fieldnames=self.encabezado_cuentas)
            escritor.writeheader()
            for obj in self.__cuentas:
                escritor.writerow(obj.a_dict())
            print("Se ha(n) registrado la(s) cuenta(s) en cuentas.csv")

    def alta_actualizar_ejecutivo(self):
        """
        Método para dar de alta un ejecutivo o actualizar uno existente
        """
        while True: # Despliega el menú
            print("\nEscoge una opción:")
            print("1. Dar de alta")
            print("2. Actualizar")
            print("3. Regresar")
            criterio = input("Ingresa la opción deseada: ")
            if criterio not in "123" or len(criterio) != 1: # Si la opción dada no es válida vuelve a desplegar el menú
                print("¡No es una opción válida!\n")
                continue
            match criterio:
                case "1": # Da de alta un ejecutivo
                    while True:
                        rfc = input("Ingresa el RFC del ejecutivo(a): ")
                        if not rfc.strip():
                            print("El RFC del ejecutivo no puede estar vacío")
                            continue
                        n_empleado = input("Ingresa el nombre del ejecutivo(a): ")
                        if not n_empleado.strip():
                            print("El nombre del ejecutivo no puede estar vacío")
                            continue
                        fecha_nac = input("Ingresa la fecha de nacimiento (dd-mm-yyyy): ")
                        direccion = input("Ingresa la dirección: ")
                        if not direccion.strip():
                            print("La direccion no puede estar vacía")
                            continue
                        telefono = input("Ingresa el teléfono (10 dígitos): ")
                        if len(telefono) != 10:
                            print("El número de teléfono debe ser de 10 dígitos.")
                            continue
                        try:
                            sueldo_m = float(input("Ingresa el sueldo mensual: "))
                        except ValueError:
                            print("El valor ingresado no es un número")
                        break

                    num_empleado = getattr(self.__ejecutivos[-1], "num_empleado") + 1
                    self.__ejecutivos.append(Ejecutivo(num_empleado, rfc, n_empleado, fecha_nac, direccion, telefono, sueldo_m))
                    
                case "2": # Actualiza un ejecutivo
                    while True:
                        try:
                            ejecutivo = int(input("Ingresa el ejecutivo(a) a actualizar (número de ejecutivo): "))
                            break
                        except ValueError:
                            print("El valor ingresado no es un número")
                    for e in self.__ejecutivos:
                        if getattr(e, "num_empleado") == ejecutivo:
                            while True:
                                try:
                                    e.rfc = input("Ingresa el RFC del ejecutivo(a): ")
                                except ValueError:
                                    print("El RFC no puede estar vacío")
                                    continue
                                try:
                                    e.n_empleado = input("Ingresa el nombre del ejecutivo(a): ")
                                except ValueError:
                                    print("El nombre del empleado no puede estar vacío")
                                    continue
                                e.fecha_nac = input("Ingresa la fecha de nacimiento (dd-mm-yyyy): ")
                                try:
                                    e.direccion = input("Ingresa la dirección: ")
                                except ValueError:
                                    print("La direccion no puede estar vacía")
                                    continue
                                try:
                                    e.telefono = input("Ingresa el teléfono (10 dígitos): ")
                                except ValueError:
                                    print("El número de teléfono debe ser de 10 dígitos.")
                                    continue
                                try:
                                    e.sueldo_m = float(input("Ingresa el sueldo mensual:"))
                                    break
                                except ValueError:
                                    print("El valor ingresado no es un número")
                
                case "3": # Regresa al menú anterior
                    break

            with open("ejecutivos.csv", "w", encoding="UTF8", newline="",) as file: # Abre el archivo ejecutivos.csv y sobreescribe con la lista actualizada
                escritor = csv.DictWriter(file, fieldnames=self.encabezado_ejecutivos)
                escritor.writeheader()
                for obj in self.__ejecutivos:
                    escritor.writerow(obj.a_dict())
                print("Se ha registrado el/la ejecutivo(a) en ejecutivos.csv")
            self.__ejecutivo_cuenta.clear()
            tipos = ["Débito", "Crédito", "Nómina"]
            for e in self.__ejecutivos: # Asigna una cuenta a un ejecutivo (cuenta de apertura)
                c = random.choice(tipos)
                self.__ejecutivo_cuenta[e] = c

    def eliminar_cuentas(self):
        """
        Método para eliminar cuentas y registrarlas a cuentas_borradas.csv
        """
        while True: # Despliega el menú
            print("\nIndica el criterio de eliminación")
            print("1. Por nombre del cliente")
            print("2. Por número de cliente")
            print("3. Por fecha de apertura")
            print("4. Por tipo de cuenta")
            print("5. Por rango de saldo")
            print("6. Por número de sucursal (1-6)")
            print("7. Regresar")
            criterio = input("Selecciona el criterio de eliminación: ")
            if criterio not in "1234567" or len(criterio) != 1: # Si el criterio no es válido vuelve a desplegar el menú
                print("¡No es una opción válida!\n")
            match criterio:
                case "1": # Busqueda por nombre de cliente
                    r = input("Ingresa el nombre del cliente: ")
                    for c in self.__cuentas:
                        if getattr(c, "n_cliente") == r:
                            self.__cuentas_borradas.append(c)
                            self.__cuentas.remove(c)
                case "2": # Busqueda por número de cliente
                    try:
                        r = int(input("Ingresa el número de cliente: "))
                    except ValueError:
                        print("El valor ingresado no es un número")
                        continue
                    for c in self.__cuentas:
                        if getattr(c, "num_cliente") == r:
                            self.__cuentas_borradas.append(c)
                            self.__cuentas.remove(c)
                case "3": # Busqueda por fecha de apertura
                    r = input("Ingresa la fecha de apertura: ")
                    for c in self.__cuentas:
                        if getattr(c, "fecha_apertura") == r:
                            self.__cuentas_borradas.append(c)
                            self.__cuentas.remove(c)
                case "4": # Busqueda por tipo de cuenta
                    tipo = input("Ingresa el tipo de cuenta (Débito, Crédito o Nómina): ").title()
                    for c in self.__cuentas:
                        if tipo == "Débito" or tipo == "Debito":
                            if isinstance(c, CuentaD):
                                self.__cuentas_borradas.append(c)
                                self.__cuentas.remove(c)
                        elif tipo == "Crédito" or tipo == "Credito":
                            if isinstance(c, CuentaC):
                                self.__cuentas_borradas.append(c)
                                self.__cuentas.remove(c)
                        elif tipo == "Nómina" or tipo == "Nomina":
                            if isinstance(c, CuentaN):
                                self.__cuentas_borradas.append(c)
                                self.__cuentas.remove(c)
                case "5": # Busqueda por rango de saldo
                    try:
                        r1 = float(input("Ingresa el saldo mínimo: "))
                        r2 = float(input("Ingresa el saldo máximo: "))
                    except ValueError:
                        print("El valor ingresado no es un número")
                        continue
                    for c in self.__cuentas:
                        if r2 > getattr(c, "saldo") > r1:
                            self.__cuentas_borradas.append(c)
                            self.__cuentas.remove(c)
                case "6": # Busqueda por número de sucursal
                    try:
                        r = int(input("Ingresa el número de sucursal (1-6): "))
                    except ValueError:
                        print("El valor ingresado no es un número")
                        continue
                    for c in self.__cuentas:
                        if getattr(c, "num_sucursal") == r:
                            self.__cuentas_borradas.append(c)
                            self.__cuentas.remove(c)
                case "7": # Regresa al menú anterior
                    break
            if len(self.__cuentas_borradas) != 0: # Si la busqueda dio resultados
                with open("cuentas_borradas.csv", "w", encoding="UTF8", newline="",) as file: # Abre el archivo cuentas_borradas.csv y sobreescribe con la lista de cuentas borradas
                    escritor = csv.DictWriter(file, fieldnames=self.encabezado_cuentas)
                    escritor.writeheader()
                    for obj in self.__cuentas_borradas:
                        escritor.writerow(obj.a_dict())
                    print("La(s) cuenta(s) borrada(s) se ha(n) registrado en cuentas_borradas.csv")

                with open("cuentas.csv", "w", encoding="UTF8", newline="",) as file: # Abre el archivo cuentas.csv y borra las cuentas seleccionadas
                    escritor = csv.DictWriter(file, fieldnames=self.encabezado_cuentas)
                    escritor.writeheader()
                    for obj in self.__cuentas:
                        escritor.writerow(obj.a_dict())
                    print("Se ha(n) registrado la(s) cuenta(s) en cuentas.csv")
            else:
                print("Los datos ingresados no coinciden con ningúna cuenta")

    def eliminar_ejecutivos(self):
        """
        Método para eliminar ejecutivos y registrarlos a ejecutivos_borrados.csv
        """
        while True: # Despliega el menú
            print("\nIndica el criterio de eliminación")
            print("1. Por número del ejecutivo(a)")
            print("2. Por RFC del ejecutivo(a)")
            print("3. Por nombre del ejecutivo(a)")
            print("4. Por fecha de nacimiento del ejecutivo(a)")
            print("5. Por rango de edad")
            print("6. Por rango de sueldo")
            print("7. Regresar")
            criterio = input("Ingresa el criterio de eliminación: ")
            if criterio not in "1234567" or len(criterio) != 1: # Si el criterio seleccionado no es válido vuelve a desplegar el menú
                print("¡No es una opción válida!\n")
            match criterio:
                case "1": # Busqueda por número de ejecutivo
                    try:
                        r = int(input("Ingresa el ejecutivo(a) a eliminar (número de ejecutivo) : "))
                    except ValueError:
                        print("El valor ingresado no es un número")
                        continue
                    for e in self.__ejecutivos:
                        if getattr(e, "num_empleado") == r:
                            self.__ejecutivos_borrados.append(e)
                            self.__ejecutivos.remove(e)
                case "2": # Busqueda por RFC del ejecutivo
                    r = input("Ingresa el RFC del ejecutivo(a): ")
                    for e in self.__ejecutivos:
                        if getattr(e, "rfc") == r:
                            self.__ejecutivos_borrados.append(e)
                            self.__ejecutivos.remove(e)
                case "3": # Busqueda por nombre del ejecutivo
                    r = input("Ingresa el nombre del ejecutivo(a): ")
                    for e in self.__ejecutivos:
                        if getattr(e, "n_empleado") == r:
                            self.__ejecutivos_borrados.append(e)
                            self.__ejecutivos.remove(e)
                case "4": # Busqueda por fecha de nacimiento
                    r = input("Ingresa la fecha de nacimiento del ejecutivo(a): ")
                    for e in self.__ejecutivos:
                        if getattr(e, "fecha_nac") == r:
                            self.__ejecutivos_borrados.append(e)
                            self.__ejecutivos.remove(e)
                case "5": # Busqueda por rango de edad
                    try:
                        r1 = int(input("Ingresa la edad máxima: "))
                        r2 = int(input("Ingresa la edad mínima: "))
                    except ValueError:
                        print("El valor ingresado no es un número")
                        continue
                    hoy = datetime.today() 
                    for e in self.__ejecutivos:
                        cum = getattr(e, "fecha_nac")
                        fecha_cum = datetime(cum[6:], cum[3:5], cum[:2])
                        edad = hoy.year - fecha_cum.year - ((hoy.month, hoy.day) < (fecha_cum.month, fecha_cum.day))
                        if r2 >= edad >= r1:
                            self.__ejecutivos_borrados.append(e)
                            self.__ejecutivos.remove(e)
                case "6": # Busqueda por rango de sueldo mensual
                    try:
                        r1 = float(input("Ingresa el sueldo máximo: "))
                        r2 = float(input("Ingresa el sueldo mínimo: "))
                    except ValueError:
                        print("El valor ingresado no es un número")
                        continue
                    for e in self.__ejecutivos:
                        if r1 > getattr(e, "sueldo_m") > r2:
                            self.__ejecutivos_borrados.append(e)
                            self.__ejecutivos.remove(e)
                case "7": # Regresa al menú anterior
                    break

            if len(self.__ejecutivos_borrados) != 0:
                with open("ejecutivos_borrados.csv", "w", encoding="UTF8", newline="",) as file: # Si la busqueda dio resultados abre el archivo ejecutivos_borrados.csv y sobreescribe con la lista de ejecutivos borrados
                    escritor = csv.DictWriter(file, fieldnames=self.encabezado_ejecutivos)
                    escritor.writeheader()
                    for obj in self.__ejecutivos_borrados:
                        escritor.writerow(obj.a_dict())
                    print("Se ha(n) registrado el/la/los ejecutivo(a)(s) borrado(s) en ejecutivos_borrados.csv")
                
                with open("ejecutivos.csv", "w", encoding="UTF8", newline="",) as file: # Abre el archivo ejecutivos.csv y borra los ejecutivos borrados
                    escritor = csv.DictWriter(file, fieldnames=self.encabezado_ejecutivos)
                    escritor.writeheader()
                    for obj in self.__ejecutivos:
                        escritor.writerow(obj.a_dict())
                    print("Se ha registrado el/la ejecutivo(a) en ejecutivos.csv")
                self.__ejecutivo_cuenta.clear()
                tipos = ["Débito", "Crédito", "Nómina"]
                for e in self.__ejecutivos:
                    c = random.choice(tipos)
                    self.__ejecutivo_cuenta[e] = c
            else:
                print("Los datos ingresados no coinciden con ningún ejecutivo")
    #Inciso c y d:
    def buscar_cuenta_operacion(self, identificador:str) -> Cuenta | None:
        """
        Método que permite buscar una cuneta en la lista de cuentas del sistema por su número de cuenta (para cuentas de Débito/Nómina)
        o por su número de tarjeta(para cuentas de Crédito)
        :param identificador: El número de cuenta o el número de tarjeta de la cuenta a buscar.
        :return: Cuenta | None: El objeto Cuenta si se encuentra una coincidencia, de lo contrario, None.
        """
        for cuenta in self.__cuentas:
            # Para CuentaC (Crédito), el identificador es el num_tarjeta (string)
            if (isinstance(cuenta, CuentaC) and cuenta.num_tarjeta == identificador) or \
               (hasattr(cuenta, 'num_cuenta') and str(cuenta.num_cuenta) == identificador):
                # Para CuentaD y CuentaN, el num_cuenta es un int, se convierte a string para comparar
                return cuenta
        return None

    def realizar_deposito_deb(self):
        """
        Método que se encarga de gestionar el proceso de depósito de dinero en una cuenta de Débito.
        Este método solicita al usuario el número de cuenta de débito y el monto a depositar.
        Realiza las validaciones necesarias para asegurar que la cuenta existe y es de tipo Débito,
        y luego llama al método ⁠ depositar ⁠ del objeto CuentaD correspondiente.
        """
        try:
            identificador = input("Ingrese el número de cuenta de Débito a depositar: ")
            monto = float(input("Ingrese el monto a depositar: "))
            cuenta = self.buscar_cuenta_operacion(identificador)
            if not cuenta:
                print("Error: Número de cuenta no encontrado.")
                return

            if isinstance(cuenta, CuentaD):
                cuenta.depositar(monto)  # <--- Esta línea DEBE estar indentada dentro del if
                print("El depósito ha sido concretado exitosamente en la cuenta de Débito.")
            elif isinstance(cuenta, CuentaN):
                print("Error: Para cuentas de Nómina, use la opción 'Registrar Pago de Nómina'.")
                # Añadir un return aquí para salir y evitar que se ejecute más código
                return
            elif isinstance(cuenta, CuentaC):
                print("Error: Para Tarjetas de Crédito, use la opción 'Realizar Pago de Crédito'.")
                # Añadir un return aquí para salir y evitar que se ejecute más código
                return
            else:  # Si por alguna razón es una Cuenta base o de otro tipo no esperado
                print("Error: Tipo de cuenta no válida para esta operación de depósito.")

        except ValueError as ve:
            print(f"Error de entrada: {ve}")
        except Exception as e:
            print(f"Ocurrió un error: {e}")

    def realizar_pago_nomina(self):
        """
        Método que se encarga de procesar el pago de la Nómina.
        Método diseñado para ser utilizado por un ejecutivo.Utilizando el numero de cuenta de la Nómina,
        el RFC de la empresa que realiza el pago y el monto a depositar.
        Valida que la cuenta exista y sea de tipo Nómina,
        y luego delega la lógica de recepción de nómina al método `recibir_pago_nomina` de la CuentaN.
        """
        try:
            identificador = input("Ingresa el número de la cuenta de NÓMINA: ")
            rfc_empresa = input("Ingresa el RFC de la empresa que realiza el pago: ")
            monto = float(input("Ingresa el monto a depositar: "))
            cuenta =self.buscar_cuenta_operacion(identificador)
            if not cuenta:
                print("Error. Número de cuenta no encontrado.")
                return
            if not isinstance(cuenta, CuentaN):
                print("Error. La cúenta especificada no es una cuenta de nómina")
                return
            cuenta.recibir_pago_nomina(monto, rfc_empresa)
        except ValueError as ve:
            print(f"Error : {ve}")
        except Exception as e:
            print(f"Ocurrió un error: {e}")

    def realizar_retiro(self):
        """
        Método que permite gestionar la operación de retiro de dinero de cualquier tipo de cuenta (Débito, Nómina, Crédito).
        Este método solicita al usuario el número de cuenta o de tarjeta (para crédito) y el monto a retirar.
        Busca la cuenta correspondiente y utiliza el polimorfismo para llamar al método "retirar"
        específico de la clase de cuenta (CuentaD, CuentaN o CuentaC).
        Las validaciones de saldo/límite y condiciones de retiro se manejan dentro de cada clase de Cuenta.
        """
        try:
            identificador = input("Ingresa el número de cuenta o de tarjeta (4 dígitos para crédito): ")
            monto = float(input("Ingresa el monto a retirar: "))
            cuenta =self.buscar_cuenta_operacion(identificador)
            if not cuenta:
                print("Error: Número de cuenta o tarjeta no encontrado.")
                return
            cuenta.retirar(monto) # El polimorfismo permite llamar al 'retirar' correcto
        except ValueError as ve:
            print(f"\nError: {ve}")
        except Exception as e:
            print(f"\nOcurrió un error inesperado: {e}")

    def realizar_pago_credito(self):
        """
        Método que se encarga de gestionar el proceso de pago a una tarjeta de crédito.
        Este método solicita al usuario el número de la tarjeta de crédito y le presenta opciones de pago:
        monto específico, 8% del monto utilizado, o monto total utilizado. Calcula el monto a pagar según
        la opción seleccionada y luego llama al método `realizar_pago_tarjeta` del objeto CuentaC
        correspondiente para aplicar el pago.
        """
        try:
            identificador_tarjeta = input("Ingresa el número de tarjeta de CRÉDITO: ")
            cuenta = self.buscar_cuenta_operacion(identificador_tarjeta)
            if not cuenta:
                print("Error: Tarjeta de crédito no encontrada.")
                return
            if not isinstance(cuenta, CuentaC):
                print("Error: La cuenta especificada no es una tarjeta de crédito.")
                return

            print("Opciones de pago:")
            print("1. Pagar monto específico")
            print("2. Pagar 8% del monto utilizado")
            print("3. Pagar monto total utilizado")
            opcion_pago = input("Seleccione la opción deseada: ")

            monto_pago = 0.0
            if opcion_pago == '1':
                monto_pago = float(input("Ingresa el monto a pagar: $"))
            elif opcion_pago == '2':
                monto_pago = cuenta.mon_credito * 0.08
                print(f"Se pagará el 8% de la deuda: ${monto_pago:,.2f}")
            elif opcion_pago == '3':
                monto_pago = cuenta.mon_credito
                print(f"Se pagará el monto total utilizado: ${monto_pago:,.2f}")
            else:
                print("Opción de pago no válida.")
                return

            cuenta.realizar_pago_tarjeta(monto_pago)
        except ValueError as ve:
            print(f"\nError de entrada: {ve}")
        except Exception as e:
            print(f"\nOcurrió un error inesperado: {e}")

if __name__ == '__main__':
    admin = InstitucionBancaria()
    admin.cargar_cuentas()
    admin.cargar_ejecutivos()
    while True: # Despliega el menú principal
        print("\nIndica si eres cliente o ejecutivo: ")
        print("1. Ejecutivo") #Inciso b
        print("2. Cliente") #Inciso c, d y e
        print("3. Salir")
        menu = input("Selecciona la opción deseada: ")
        if menu not in "123" or len(menu) != 1: # Si la opción no es válida vuelve a desplegar el menú
            print("¡No es una opción válida!")
        match menu:
            case "1": # Menú de ejecutivos
                while True:
                    print("\nOpciones:")
                    print("1. Consultar los clientes")
                    print("2. Consultar las cuentas")
                    print("3. Consultar los ejecutivos")
                    print("4. Dar de alta una nueva cuenta o actualizar una existente")
                    print("5. Registrar el alta de una nueva cuenta")
                    print("6. Dar de alta un(s) nuevo(a) ejecutivo(a) o actualizar uno(a) existente")
                    print("7. Eliminar cuenta(s)")
                    print("8. Eliminar ejecutivo(s)")
                    print("9. Realizar pago a nómina")
                    print("10. Regresar")
                    opcion = input("Selecciona la opción deseada: ")
                    if opcion not in {"1", "2", "3", "4", "5", "6", "7", "8", "9", "10"}: # Si la opción no es válida vuelve a desplegar el menú
                        print("¡No es una opción válida!\n")
                    match opcion:
                        case "1": # Llama al método para consultar clientes
                            admin.consultar_cliente()
                        case "2": # Llama al método para consultar cuentas
                            admin.consultar_cuenta()
                        case "3": # Llama al método para consultar ejecutivos
                            admin.consultar_ejecutivo()
                        case "4": # Llama al método para dar de alta o actualizar cuentas
                            admin.alta_actualizar_cuenta()
                        case "5": # Llama al método para registrar el alta de una cuenta
                            admin.registrar()
                        case "6": # Llama al método para dar de alta o actualizar ejecutivos
                            admin.alta_actualizar_ejecutivo()
                        case "7": # Llama al método para eliminar cuentas
                            admin.eliminar_cuentas()
                        case "8": # Llama al método para eliminar ejecutivos
                            admin.eliminar_ejecutivos()
                        case "9": # Llama al método para realizar pago a nómina
                            admin.realizar_pago_nomina()
                        case "10": # Regresa al menú anterior
                            break
            case "2": # Menú de clientes
                while True:
                    print("\nOpciones:")
                    print("1. Depositar dinero a cuenta de débito")
                    print("2. Retirar dinero")
                    print("3. Pago de tarjeta")
                    print("4. Regresar")
                    opcion = input("Selecciona la opción deseada: ")
                    if opcion not in "1234" or len(opcion) != 1: # Si la opción no es válida vuelve a desplegar el menú
                        print("¡No es una opción válida!")
                    match opcion:
                        case "1": # Llama a los métodos para depositar a una cuenta de débito
                            admin.realizar_deposito_deb() 
                            admin.registrar()
                        case "2": # Llama al método para realizar retiros
                            admin.realizar_retiro()
                            admin.registrar()
                        case "3": # Llama al método para realizar pagos
                            admin.realizar_pago_credito()
                            admin.registrar()
                        case "4": # Regresa al menú anterior
                            break
            case "3": # Salir del programa
                print("Cerrando sistema...")
                break