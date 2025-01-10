#Sistema tienda
# Clase Producto, representa un producto en la tienda
class Producto:
    # Constructor de la clase, se inicializa con nombre, precio y cantidad
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre    # Nombre del producto
        self.precio = precio    # Precio del producto por unidad
        self.cantidad = cantidad  # Cantidad disponible del producto


    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio  # Asigna el nuevo precio al atributo 'precio'


    def __str__(self):
        # Se devuelve una cadena que describe el producto, mostrando el nombre, precio y cantidad
        return f'Producto {self.nombre}: {self.precio} dólares, cantidad: {self.cantidad}.'

# Clase CarritoDeCompras: Representa un carrito de compras para un cliente
class CarritoDeCompras:
    # Constructor de la clase, inicializa una lista vacía para almacenar productos
    def __init__(self):
        self.productos = []  # Lista donde se almacenarán los productos agregados al carrito


    def agregar_producto(self, producto):
        self.productos.append(producto)  # Se agrega el producto recibido al carrito



    def calcular_total(self):
        # Utiliza una expresión generadora para sumar el precio de cada producto multiplicado por su cantidad
        return sum(producto.precio * producto.cantidad for producto in self.productos)


    def __str__(self):
        # Se crea una cadena con los nombres de todos los productos en el carrito
        productos_str = ', '.join([producto.nombre for producto in self.productos])
        # Se devuelve una cadena que describe el carrito, con los productos y el total calculado
        return f'Carrito de Compras con los productos: {productos_str}. Total: {self.calcular_total()}'

# Crear objetos
Producto1 = Producto('Arroz', 1, 2)  # Creamos un producto llamado 'Arroz' con precio 1 y cantidad 2
Producto2 = Producto('Atun', 2, 3)  # Creamos otro producto llamado 'Atun' con precio 2 y cantidad 3

# Crear un carrito de compras vacío
carrito = CarritoDeCompras()

# Agregar productos al carrito
carrito.agregar_producto(Producto1)  # Se agrega el Producto1 (Arroz) al carrito
carrito.agregar_producto(Producto2)  # Se agrega el Producto2 (Atun) al carrito

# Imprimir el contenido del carrito
print(carrito)  # Esto imprimirá los productos en el carrito y el total calculado
