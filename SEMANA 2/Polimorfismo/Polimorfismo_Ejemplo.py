# Ejemplo de la Técnica de programación_Polimorfismo
# Posibilita que múltiples clases compartan una interfaz común, permitiendo que objetos deestas clases sean utilizados de manera intercambiable.


class Animal:

    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")


class Dog(Animal):

    def __init__(self, nombre, color):
        super().__init__(nombre)
        self.color = color
        self.sonido = "Guau"

    def hacer_sonido(self):
        return f"{self.nombre} dice: {self.sonido} ¡Guau! ¡Guau!"


class Cat(Animal):

    def __init__(self, nombre, sonido):
        super().__init__(nombre)
        self.sonido = sonido

    def hacer_sonido(self):
        return f"{self.nombre} dice: {self.sonido} ¡Miauuu!"


# Función para aplicar polimorfismo
def mostrar_sonido(animal):
    # Llama al método hacer_sonido del objeto de acuerdo al tipo
    print(animal.hacer_sonido())


# Crear los objetos
mi_perro1 = Dog("Tobi", "blanco")
mi_gato1 = Cat("Dogi", "Miauu")

# Llamar a la función de polimorfismo
mostrar_sonido(mi_perro1)  # Polimorfismo: el perro hace un sonido
mostrar_sonido(mi_gato1)  # Polimorfismo: el gato hace un sonido

        
             
        
