"""
Rafael Zerpa, V-31.148.991
"""

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        if saldo_inicial >= 0:
            self.__saldo = saldo_inicial
        else:
            self.__saldo = 0
            print("El saldo inicial no puede ser negativo. Se inició en 0.")

    def ver_saldo(self):
        return self.__saldo

    def depositar(self, monto):
        if monto > 0:
            self.__saldo = self.__saldo + monto
            print(f"[{self.titular}] Depósito de ${monto} exitoso.")
        else:
            print("Error: El monto a depositar debe ser mayor a 0.")

    def retirar(self, monto):
        if monto > 0 and monto <= self.__saldo:
            self.__saldo = self.__saldo - monto
            print(f"[{self.titular}] Retiro de ${monto} exitoso.")
        else:
            print(f"[{self.titular}] Error: Fondos insuficientes o monto inválido.")


class CuentaAhorro(CuentaBancaria):
    def __init__(self, titular, saldo_inicial, tasa_interes):
        super().__init__(titular, saldo_inicial)
        self.tasa_interes = tasa_interes

    def aplicar_interes(self):
        ganancia = self.ver_saldo() * (self.tasa_interes / 100)
        self.depositar(ganancia)
        print(f"Interés del {self.tasa_interes}% aplicado.")


print("--- USUARIO 1 ---")
cuenta_normal = CuentaBancaria("Carlos", 100)
cuenta_normal.retirar(150)  
cuenta_normal.depositar(50)
print(f"Saldo final de Carlos: ${cuenta_normal.ver_saldo()}")

print("\n--- USUARIO 2 ---")
cuenta_ahorro = CuentaAhorro("Ana", 1000, 5) 
cuenta_ahorro.aplicar_interes()
print(f"Saldo final de Ana: ${cuenta_ahorro.ver_saldo()}")