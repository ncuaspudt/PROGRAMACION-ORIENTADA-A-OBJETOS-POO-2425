#Ejemplo de la Técnica de programación_Encapsulación



class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.__titular = titular  # Atributo privado: no accesible directamente desde fuera
        self.__saldo = saldo_inicial  # Atributo privado: no accesible directamente desde fuera

    # Getter para el saldo
    def obtener_saldo(self):
        return self.__saldo

    # Método para depositar dinero (modifica el saldo)
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Has depositado {cantidad} unidades. Nuevo saldo: {self.__saldo}")
        else:
            print("La cantidad a depositar debe ser mayor a cero.")

    # Método para retirar dinero (modifica el saldo)
    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Has retirado {cantidad} unidades. Nuevo saldo: {self.__saldo}")
        else:
            print("Fondos insuficientes o cantidad no válida.")

    # Getter para obtener el titular (se podría crear un setter si se quisiera cambiar el titular)
    def obtener_titular(self):
        return self.__titular

    # Getter y Setter para el titular (si se desea permitir modificar el titular)
    def set_titular(self, nuevo_titular):
        self.__titular = nuevo_titular
        print(f"El nuevo titular de la cuenta es: {self.__titular}")

# Crear una instancia de CuentaBancaria
cuenta = CuentaBancaria("Juan Pérez", 500)

# Mostrar el saldo inicial
print("Saldo inicial:", cuenta.obtener_saldo())

# Depositar dinero
cuenta.depositar(200)

# Retirar dinero
cuenta.retirar(100)

# Intentar retirar más dinero del disponible
cuenta.retirar(700)

# Cambiar el titular de la cuenta
cuenta.set_titular("Ana Gómez")

# Obtener el titular actual
print("Titular actual:", cuenta.obtener_titular())

# Verificar saldo final
print("Saldo final:", cuenta.obtener_saldo())