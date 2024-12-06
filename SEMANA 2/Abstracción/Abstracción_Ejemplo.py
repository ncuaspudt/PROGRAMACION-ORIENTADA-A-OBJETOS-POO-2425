# Ejemplo de la Técnica de programación_Abstracción

from abc import ABC, abstractmethod  # Importamos las clases necesarias para crear clases abstractas

# Clase base abstracta que representa un Vehiculo
class Vehiculo(ABC):

    # Constructor de la clase Vehiculo
    def __init__(self, nombre, velocidad_maxima):
        self.nombre = nombre
        self.velocidad_maxima = velocidad_maxima

    # Método abstracto (no implementado aquí) para que las clases hijas lo implementen
    @abstractmethod
    def mover(self):
        pass

    # Método para mostrar los detalles del vehículo
    def detalles(self):
        print(f"Vehículo: {self.nombre}")
        print(f"Velocidad máxima: {self.velocidad_maxima} km/h")


# Clase Coche que hereda de Vehiculo
class Coche(Vehiculo):

    def __init__(self, nombre, velocidad_maxima, tipo_combustible):
        super().__init__(nombre, velocidad_maxima)
        self.tipo_combustible = tipo_combustible

    # Implementación del método 'mover' específico para los coches
    def mover(self):
        print(
            f"El coche {self.nombre} está moviéndose a {self.velocidad_maxima} km/h utilizando {self.tipo_combustible}.")

    # Método para mostrar los detalles del coche
    def detalles(self):
        super().detalles()
        print(f"Tipo de combustible: {self.tipo_combustible}")


# Clase Bicicleta que hereda de Vehiculo
class Bicicleta(Vehiculo):

    def __init__(self, nombre, velocidad_maxima, tipo_ruedas):
        super().__init__(nombre, velocidad_maxima)
        self.tipo_ruedas = tipo_ruedas

    # Implementación del método 'mover' específico para las bicicletas
    def mover(self):
        print(
            f"La bicicleta {self.nombre} está pedaleando a {self.velocidad_maxima} km/h con ruedas {self.tipo_ruedas}.")

    # Método para mostrar los detalles de la bicicleta
    def detalles(self):
        super().detalles()
        print(f"Tipo de ruedas: {self.tipo_ruedas}")


# Crear instancias de Coche y Bicicleta
mi_coche = Coche("Toyota Corolla", 180, "Gasolina")
mi_bicicleta = Bicicleta("Mountain Bike", 50, "Montaña")

# Llamar al método 'detalles' para mostrar la información
mi_coche.detalles()
mi_bicicleta.detalles()

# Llamar al método 'mover' para simular el movimiento
mi_coche.mover()
mi_bicicleta.mover()