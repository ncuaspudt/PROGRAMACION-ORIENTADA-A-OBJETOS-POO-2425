# Clase Persona
## El constructor __init__ permite inicializar el objeto, esto incluye asignar atributos.
###El constructor configura lo necesario para iniciar el funcionamiento del objeto.
####  A continuación detallaremos sobre la Clase Persona incluyendo el metodo saludar.

class Persona:
    def __init__(self, nombre, nacionalidad): # El constructor inicializa los atributos
        self.nombre = nombre
        self.nacionalidad = nacionalidad

# Metodo que permite a la persona saludar

    def saludar (self):
        print(f"¡Hola! Soy {self.nombre} y soy {self.nacionalidad}")

# Mediante la utilización del metodo __del__ se llama automáticamente para eliminar las referencias del objeto.
    # Este destructor invoca cuando un objeto está apunto de ser destruido.

    def __del__(self):
        print(f"{self.nombre} ha dejado el programa.") #Imprime cuando la persona ha dejado el programa.

# Creación de objetos

persona1= Persona("Javier", "ecuatoriano")
persona1.saludar()

# El destructor se ejecutará automáticamente cuando el objeto 'persona1' se destruya

