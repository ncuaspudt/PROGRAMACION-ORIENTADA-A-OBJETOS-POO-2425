# Ejemplo de la Técnica de programación_Polimorfismo

class Animal:
    def hacer_sonido(self):
        print("El animal hace un sonido genérico")

# Clase hija (subclase) que hereda de Animal
class Perro(Animal):
    def hacer_sonido(self):
        print("¡Guau! (El perro hace un sonido característico)")

# Clase hija (subclase) que hereda de Animal
class Gato(Animal):
    def hacer_sonido(self):
        print("¡Miau! (El gato hace un sonido característico)")

# Clase hija (subclase) que hereda de Animal
class Vaca(Animal):
    def hacer_sonido(self):
        print("¡Muu! (La vaca hace un sonido característico)")

# Función que recibe un objeto de tipo Animal y hace que suene
def hacer_sonido_animal(animal):
    animal.hacer_sonido()

# Crear instancias de las clases hijas
mi_perro = Perro()
mi_gato = Gato()
mi_vaca = Vaca()

# Llamar a la función con diferentes tipos de animales
hacer_sonido_animal(mi_perro)  # Salida esperada: ¡Guau! (El perro hace un sonido característico)
hacer_sonido_animal(mi_gato)   # Salida esperada: ¡Miau! (El gato hace un sonido característico)
hacer_sonido_animal(mi_vaca)   # Salida esperada: ¡Muu! (La vaca hace un sonido característico)