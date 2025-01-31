# Ejemplo de la Técnica de programación_Abstracción
# Simplifica la realidad, concentrándose en los aspectos esenciales de un objeto y ocultando los detalles innecesarios.

# Clase base "Figura"
class Figura:
    def area(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase")

    def perimetro(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase")


# Clase Cuadrado que hereda de Figura
class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    # Implementación del cálculo del área
    def area(self):
        return self.lado * self.lado



    # Implementación del cálculo del perímetro
    def perimetro(self):
        return 4 * self.lado


# Crear un objeto de la clase Cuadrado
mi_cuadrado = Cuadrado(5)

# Llamamos a los métodos de la clase Cuadrado
print(f"Área del cuadrado: {mi_cuadrado.area()}")
print(f"Perímetro del cuadrado: {mi_cuadrado.perimetro()}")

