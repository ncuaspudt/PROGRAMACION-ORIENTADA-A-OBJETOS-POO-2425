# clase base vehiculo

class Vehiculo:
    def __init__(self, marca, precio):
        self.marca = marca
        self.__precio = precio #Atributo privado


    # Metodo para acceder al precio (encapsulación)
    def obtener_precio(self):
        return self.__precio

    # Metodo que puede ser sobreescrito (Polimorfismo)
    def descripcion(self):
        return f"Precio: {self.obtener_precio()}, Marca: {self.marca}"

# Clase derivada Camión que hereda de Vehiculo
class Camion(Vehiculo):
            def __init__(self, marca, precio,placa):
                super().__init__(marca, precio)
                self.placa = placa
            #Sobreescritura del metodo descripción
            def descripcion(self):
                # Se utiliza el metodo obtener_precio para acceder al precio privado
                return f"Marca: {self.marca}, Precio: {self.obtener_precio()}, Placa: {self.placa}"

# Funcion para mostrar el polimorfismo
def mostrar_descripcion(vehiculo):
    print(vehiculo.descripcion()) # Se llama al metodo descripción

#creación de objetos
vehiculo = Vehiculo(marca=" ISUZU", precio="$ 20000")
camion = Camion(marca="CHEVROLET", precio="50000", placa="ABC124")

#mostrar la encapsulación nos permite acceder al precio
print(vehiculo.obtener_precio())

#mostrar polimorfismo
mostrar_descripcion(vehiculo)
mostrar_descripcion(camion)




