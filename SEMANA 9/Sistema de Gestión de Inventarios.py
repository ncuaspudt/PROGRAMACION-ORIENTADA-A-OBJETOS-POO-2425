
# Sistema de Gestión de Inventario

# Clase Producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Métodos Getters y Setters
    def get_id_producto(self):
        return self.id_producto

    def set_id_producto(self, id_producto):
        self.id_producto = id_producto

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio}"

# Clase Inventario
class Inventario:
    def __init__(self):
        # Usamos un diccionario para almacenar los productos, con id_producto como clave
        self.productos = {}

    def agregar_producto(self, producto):
        if producto.get_id_producto() in self.productos:
            print("Error: Producto con ese ID ya existe.")
        else:
            self.productos[producto.get_id_producto()] = producto
            print(f"Producto {producto.get_nombre()} agregado correctamente.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print(f"Producto con ID {id_producto} eliminado.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            if cantidad is not None:
                producto.set_cantidad(cantidad)
            if precio is not None:
                producto.set_precio(precio)
            print(f"Producto con ID {id_producto} actualizado.")
        else:
            print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        found = False
        for producto in self.productos.values():
            if nombre.lower() in producto.get_nombre().lower():
                print(producto)
                found = True
        if not found:
            print("No se encontró ningún producto con ese nombre.")

    def mostrar_inventario(self):
        if not self.productos:
            print("Inventario vacío.")
        else:
            for producto in self.productos.values():
                print(producto)

# Interfaz de usuario en la consola
def menu():
    inventario = Inventario()

    while True:
        print("\n1. Agregar Producto")
        print("2. Eliminar Producto")
        print("3. Actualizar Producto")
        print("4. Buscar Producto")
        print("5. Mostrar Inventario")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '6':
            break
        elif opcion == '1':
            # Agregar producto
            id_producto = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad: "))
            precio = float(input("Ingrese el precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
        elif opcion == '2':
            # Eliminar producto
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
        elif opcion == '3':
            # Actualizar producto
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Ingrese la nueva cantidad (deje en blanco para no cambiar): ")
            precio = input("Ingrese el nuevo precio (deje en blanco para no cambiar): ")

            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None

            inventario.actualizar_producto(id_producto, cantidad, precio)
        elif opcion == '4':
            # Buscar producto
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)
        elif opcion == '5':
            # Mostrar inventario
            inventario.mostrar_inventario()
        else:
            print("Opción inválida, intente de nuevo.")

# Punto de entrada principal
if __name__ == "__main__":
    menu()