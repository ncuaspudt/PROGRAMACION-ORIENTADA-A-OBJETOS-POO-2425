#Programación orientada a objetos.
#La POO se basa en el concepto central de "objeto", entidades que encapsulan datos y funciones.
# Información diaria del clima y promedio semanal de la ciudad a y Ciudad B.
# Clase base Clima (representa el clima de una ciudad)

class Clima:
    def __init__(self):
        # Lista privada que contiene las temperaturas diarias (inicialmente vacía)
        # La lista de días será una lista de tuplas (día, temperatura)
        self.__temperaturas = []
        self.__dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    # Métodoingreso de temperaturas
    def ingresar_temperaturas(self, temperaturas):
        if len(temperaturas) == 7:
            self.__temperaturas = list(zip(self.__dias, temperaturas))  # Empareja los días con las temperaturas
        else:
            print("Error: Deben ser exactamente 7 temperaturas.")

    # MétodoPromedio semanal
    def calcular_promedio(self):
        if self.__temperaturas:
            total_temperature = sum([temp[1] for temp in self.__temperaturas])  # Suma solo las temperaturas
            return total_temperature / len(self.__temperaturas)
        else:
            return 0

    # Métodopara obtener las temperaturas (getter)
    def obtener_temperaturas(self):
        return self.__temperaturas

# Clase hija Clima Ciudad (hereda de Clima y agrega el nombre de la ciudad)
class ClimaCiudad(Clima):
    def __init__(self, nombre_ciudad):
        super().__init__()  # Llama al constructor de la clase base (Clima)
        self.nombre_ciudad = nombre_ciudad  # Atributo adicional: nombre de la ciudad

    # Sobrescribimos el métodocalcular_promedio si fuera necesario (ejemplo de polimorfismo)
    def calcular_promedio(self):
        promedio = super().calcular_promedio()  # Llama al métodode la clase base
        return f"Promedio semanal en {self.nombre_ciudad}: {promedio:.2f}°C"

    # Métodopara mostrar las temperaturas con los días de la semana
    def mostrar_temperaturas(self):
        print(f"Temperaturas de la semana en {self.nombre_ciudad}:")
        for dia, temp in self.obtener_temperaturas():
            print(f"{dia}: {temp}°C")

# Uso de la Programación Orientada a Objetos
# Creamos objetos para diferentes ciudades
ciudad1 = ClimaCiudad("Ciudad A")
ciudad2 = ClimaCiudad("Ciudad B")

# Ingresamos las temperaturas para cada ciudad
ciudad1.ingresar_temperaturas([18.0, 20.0, 22.0, 19.0, 21.0, 23.0, 20.0])
ciudad2.ingresar_temperaturas([15.0, 17.5, 16.0, 18.0, 19.5, 17.0, 18.5])

# Mostramos las temperaturas para cada ciudad
ciudad1.mostrar_temperaturas()
print()  # Imprimir una línea vacía entre ciudades
ciudad2.mostrar_temperaturas()

# Calculamos y mostramos el promedio semanal para cada ciudad
print(ciudad1.calcular_promedio())  # Resultado para Ciudad A
print(ciudad2.calcular_promedio())  # Resultado para Ciudad