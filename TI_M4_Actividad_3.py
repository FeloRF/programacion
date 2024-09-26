#-*- coding: utf-8 -*-
# TI_M4_Actividad_3 Felipe Rojas ingenieria en informatica

"""
3.- Se debe crear una clase llamada "Cuenta" que tenga las
propiedades número de cuenta, nombre del titular, saldo inicial y tipo de cuenta. La clase
debe tener tres métodos: depositar, retirar y obtener balance. El método depositar debe
recibir una cantidad y agregarla al saldo de la cuenta. El método retirar debe recibir una
cantidad y restarla del saldo de la cuenta. El método obtener balance debe devolver el
saldo actual de la cuenta. Para probar la clase, se debe crear una instancia de la misma,
hacer un depósito, un retiro y obtener el saldo actual. Finalmente, se debe imprimir la
información con todos los datos de usuarios y balances.
    """

class CuentaBancaria:
    # Atributos de la cuenta bancaria
    def __init__(self, num_cuenta, titular, saldo_inicial, tipo_cuenta):
        # Se asignan los valores de los atributos de la cuenta (número de cuenta, titular, saldo y tipo de cuenta)
        self.num_cuenta = num_cuenta
        self.titular = titular
        self.saldo = saldo_inicial
        self.tipo_cuenta = tipo_cuenta

    # Ingreso de saldo en la cuenta
    def agregar_dinero(self, monto):
        self.saldo += monto  # Sumar el monto depositado al saldo actual
        print("Has agregado {}. El saldo actual es: {}".format(monto, self.saldo))

    # Retiro de dinero de la cuenta
    def quitar_dinero(self, monto):
        if monto > self.saldo:  # Verificar si el monto que se quiere retirar es mayor que el saldo disponible
            print("Fondos insuficientes.")  # Imprimir mensaje si no hay suficiente dinero en la cuenta
        else:
            self.saldo -= monto  # Restar el monto retirado del saldo actual
            print("Has quitado {}. El saldo actual es: {}".format(monto, self.saldo))

    # Método para consultar el saldo actual
    def consultar_saldo(self):
        return self.saldo  # Devolver el saldo actual

    # Método para mostrar la información completa de la cuenta
    def mostrar_info(self):
        # Imprimir la información de la cuenta: número de cuenta, nombre del titular, tipo de cuenta y saldo actual
        print("Número de Cuenta: {}".format(self.num_cuenta))
        print("Titular: {}".format(self.titular))
        print("Tipo de Cuenta: {}".format(self.tipo_cuenta))
        print("Saldo Actual: {}".format(self.saldo))


# Crear una instancia de la clase CuentaBancaria
mi_cuenta = CuentaBancaria("12345678", "Felipe Rojas", 100, "Cuenta de Ahorro")

# Agregar dinero a la cuenta
mi_cuenta.agregar_dinero(100)  # Depósito de 500

# Retirar dinero de la cuenta
mi_cuenta.quitar_dinero(9000)   # Retiro de 200

# Consultar el saldo actual
saldo_actual = mi_cuenta.consultar_saldo()  # Obtener el saldo actual de la cuenta

# Mostrar la información completa de la cuenta
mi_cuenta.mostrar_info()

# Imprimir el saldo final
print("El saldo final es: {}".format(saldo_actual))
