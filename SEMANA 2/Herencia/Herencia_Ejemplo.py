# Ejemplo de la Técnica de programación_Herencia
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        print("El animal hace un sonido")

# Clase hija (subclase) que hereda de Animal
class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)  # Llamamos al constructor de la clase base
        self.raza = raza

    # Sobrescribimos el método hacer_sonido para Perro
    def hacer_sonido(self):
        print(f"{self.nombre} (un {self.raza}) dice: ¡Guau!")

# Clase hija (subclase) que hereda de Animal
class Gato(Animal):
    def __init__(self, nombre, color):
        super().__init__(nombre)  # Llamamos al constructor de la clase base
        self.color = color

    # Sobrescribimos el método hacer_sonido para Gato
    def hacer_sonido(self):
        print(f"{self.nombre} (un gato {self.color}) dice: ¡Miau!")

# Crear instancias de Perro y Gato
mi_perro = Perro("Rex", "Labrador")
mi_gato = Gato("Whiskers", "blanco")

# Llamar al método hacer_sonido para cada uno
mi_perro.hacer_sonido()  # Salida esperada: Rex (un Labrador) dice: ¡Guau!
mi_gato.hacer_sonido()  # Salida esperada: Whiskers (un gato blanco) dice: ¡Miau!