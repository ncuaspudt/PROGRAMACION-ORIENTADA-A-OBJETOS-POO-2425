#Programa de calculo de area del circulo y rectangulo
# Importamos el módulo 'math' para poder usar el valor de PI en el cálculo del área del círculo.
import math

# Clases: CamelCase (cada palabra comienza con mayúscula)
# Clase que representa un Círculo
class Circulo:
    def __init__(self, radio):  # Corregido de _init_ a __init__
        # Inicializamos el objeto con el radio del círculo
        self.radio = radio

    def calcular_area(self):
        # Calculamos el área usando la fórmula: área = π * radio^2
        return math.pi * (self.radio ** 2)
#Funciones y variables: snake_case
# Clase que representa un Rectángulo
class Rectangulo:
    def __init__(self, base, altura):  # Corregido de _init_ a __init__
        # Inicializamos el objeto con la base y altura del rectángulo
        self.base = base
        self.altura = altura

    def calcular_area(self):
        # Calculamos el área usando la fórmula: área = base * altura
        return self.base * self.altura

# Funciones y variables: snake_case (palabras separadas por guiones bajos)
# Función para calcular el área de una figura cualquiera
def calcular_area_figura(figura):
    return figura.calcular_area()

# Constantes: MAYUSCULAS con guiones bajos
# Definimos la constante PI usando el valor de PI de la librería math
PI = math.pi

# Instancias de las clases
# Creamos un objeto de la clase 'Circulo' con un radio de 5 unidades
mi_circulo = Circulo(5)

# Creamos un objeto de la clase 'Rectangulo' con base de 4 y altura de 7 unidades
mi_rectangulo = Rectangulo(4, 7)

# Llamada a la función para calcular el área de cada figura
# Calculamos el área del círculo y la almacenamos en la variable 'area_circulo'
area_circulo = calcular_area_figura(mi_circulo)

# Calculamos el área del rectángulo y la almacenamos en la variable 'area_rectangulo'
area_rectangulo = calcular_area_figura(mi_rectangulo)

# Imprimimos los resultados de las áreas con un formato adecuado
# Para el círculo, mostramos el área con dos decimales
print(f"Área del círculo: {area_circulo:.2f} unidades cuadradas")

# Mostramos el área del rectángulo
print(f"Área del rectángulo: {area_rectangulo} unidades cuadradas")